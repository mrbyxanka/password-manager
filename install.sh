INSTALL_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PASSWORD_SCRIPT="$INSTALL_SCRIPT_DIR/pm.sh"

if [ ! -f "$PASSWORD_SCRIPT" ]; then
	echo "pm.sh not found in $PASSWORD_SCRIPT"
	exit 1
fi

chmod +x $PASSWORD_SCRIPT
sudo ln -s $PASSWORD_SCRIPT /usr/local/bin
