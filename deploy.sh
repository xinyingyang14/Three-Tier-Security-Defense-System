#!/bin/bash
cd /home/jocelyn/project

echo "[+] Starting automated deployment..."
echo "[+] Cleaning Python code indentation (Tabs -> 4 Spaces)..."
sed -i 's/\t/    /g' *.py 2>/dev/null
sed -i 's/\t/    /g' auth/*.py 2>/dev/null
sed -i 's/\t/    /g' crypto/*.py 2>/dev/null
sed -i 's/\t/    /g' database/*.py 2>/dev/null
mkdir -p logs

source /home/jocelyn/myenv/bin/activate
echo "[+] Virtual environment 'myenv' activated successfully."
if [ -f "requirements.txt" ]; then
	echo "[+] Installing dependencies from requirements.txt..."
	pip install -r requirements.txt
fi
echo "[+] Checking database connection..."
python3 -c "import sqlite3; conn=sqlite3.connect('users.db'); print('-> Database connection successful!'); conn.close()"
echo "[+] Starting Flask backend server..."
export FLASK_APP=app.py
export FLASK_ENV=production

python3 app.py
