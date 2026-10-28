"""Read VS Code JSONC and replace only its top-level folders value.

Comments and trailing commas are accepted. Duplicate keys and malformed input
are refused. Offsets refer to the original text; unrelated bytes are retained.
"""
import json
import re


TOKEN = re.compile(r'\s+|//[^\r\n]*|/\*[\s\S]*?\*/|"(?:[^"\\\x00-\x1f]|\\.)*"|[{}\[\],:]|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null')


def document(data):
    bom = b'\xef\xbb\xbf' if data.startswith(b'\xef\xbb\xbf') else b''
    text = data[len(bom):].decode('utf-8')
    tokens, position = [], 0
    while position < len(text):
        match = TOKEN.match(text, position)
        if match is None:
            raise ValueError('Invalid workspace JSONC near character ' + str(position))
        value = match.group()
        if not value.isspace() and not value.startswith(('//', '/*')):
            tokens.append((value, match.start(), match.end()))
        position = match.end()
    index = 0
    spans = {}

    def parse(depth=0):
        nonlocal index
        if depth > 100 or index >= len(tokens):
            raise ValueError('Incomplete or excessively nested workspace JSONC')
        token = tokens[index][0]
        index += 1
        if token in ('{', '['):
            result = {} if token == '{' else []
            close = '}' if token == '{' else ']'
            if index < len(tokens) and tokens[index][0] == close:
                index += 1
                return result
            while True:
                if token == '{':
                    if index >= len(tokens) or not tokens[index][0].startswith('"'):
                        raise ValueError('Expected a workspace property name')
                    key = json.loads(tokens[index][0])
                    index += 1
                    if key in result:
                        raise ValueError('Duplicate workspace property: ' + key)
                    if index >= len(tokens) or tokens[index][0] != ':':
                        raise ValueError('Expected a colon after workspace property')
                    index += 1
                    if index >= len(tokens):
                        raise ValueError('Missing workspace property value')
                    start = tokens[index][1]
                    result[key] = parse(depth + 1)
                    if depth == 0:
                        spans[key] = (start, tokens[index - 1][2])
                else:
                    result.append(parse(depth + 1))
                if index >= len(tokens):
                    raise ValueError('Incomplete workspace JSONC')
                separator = tokens[index][0]
                index += 1
                if separator == close:
                    return result
                if separator != ',':
                    raise ValueError('Expected a comma in workspace JSONC')
                if index < len(tokens) and tokens[index][0] == close:
                    index += 1
                    return result
        if token.startswith('"') or token in ('true', 'false', 'null') or token[0] in '-0123456789':
            return json.loads(token)
        raise ValueError('Unexpected workspace JSONC token')

    value = parse()
    if index != len(tokens) or not isinstance(value, dict):
        raise ValueError('Workspace must contain one JSONC object')
    if 'folders' in value and not isinstance(value['folders'], list):
        raise ValueError('Workspace folders must be an array')
    for folder in value.get('folders', []):
        if not isinstance(folder, dict) or not isinstance(folder.get('path'), str) or not folder['path']:
            raise ValueError('Each local workspace root must contain a nonempty path')
        if 'name' in folder and not isinstance(folder['name'], str):
            raise ValueError('Workspace folder names must be strings')
    return text, value, spans, bom


def replace_folders(data, folders):
    text, value, spans, bom = document(data)
    if value.get('folders') == folders:
        return data
    newline = '\r\n' if '\r\n' in text else '\n'
    if 'folders' in spans:
        start, end = spans['folders']
        line = text[text.rfind('\n', 0, start) + 1:start]
        indent = re.match(r'[ \t]*', line).group()
    else:
        start = end = next(match.end() for match in TOKEN.finditer(text) if match.group() == '{')
        indent = '  '
    rendered = json.dumps(folders, indent=2, ensure_ascii=False, allow_nan=False)
    rendered = rendered.replace('\n', newline + indent)
    if 'folders' not in spans:
        rendered = newline + indent + '"folders": ' + rendered + (',' if value else '') + newline
    return bom + (text[:start] + rendered + text[end:]).encode('utf-8')
