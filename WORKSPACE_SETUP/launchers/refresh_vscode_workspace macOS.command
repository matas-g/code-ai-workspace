#!/bin/sh
# Terminal opens .command files. Work beside this launcher, independent of Finder's initial cwd.
launch_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P) || exit 1
cd "$launch_dir" || exit 1
status=2
found=no
for candidate in python3 python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 /usr/bin/python3; do
    if command -v "$candidate" >/dev/null 2>&1 && "$candidate" -I -S -B -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' >/dev/null 2>&1; then
        found=yes
        "$candidate" -I -S -B "$launch_dir/{{ai_work}}/tools/workspace_manager.py" refresh --interactive "$@"
        status=$?
        break
    fi
done
if [ "$found" = no ]; then
    printf '\nNo installed Python 3.9+ interpreter was found. Use an approved interpreter; nothing was installed.\n'
fi
printf '\n------------------------------------------------------------\n'
printf '  Refresh finished (exit code: %s)\n' "$status"
printf '  Review the output above before closing.\n'
printf '  Type q or quit to finish refresh.\n'
printf '  Terminal may retain a finished window under its current profile.\n'
printf '%s\n\n' '------------------------------------------------------------'
while :; do
    printf '  Close refresh [q/quit]: '
    if ! read -r reply; then
        printf '\nInput closed. You may close this window manually.\n'
        exit "$status"
    fi
    case "$reply" in
        [qQ]|[qQ][uU][iI][tT])
            printf '\nRefresh closed.\n'
            # A clean exit allows Terminal profiles with close-on-exit to close the window.
            exit 0
            ;;
        *) printf '  Type q or quit when you are ready; the output stays here.\n\n' ;;
    esac
done
