# !bin/bash
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
echo "dir: $SCRIPT_DIR"
PYTHON_SCRIPT="$SCRIPT_DIR/main.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
	echo "main.py not found in $PYTHON_SCRIPT"
	exit 1
fi

python3 "$PYTHON_SCRIPT" "$@"
