# /files/packages/webconsole/web_console.py  

from flask import Flask, request, render_template  
import subprocess  
import threading  

app = Flask(__name__)  

console_output = []  

@app.route('/')  
def index():  
    return render_template('index.html', output=console_output)  

@app.route('/execute', methods=['POST'])  
def execute_command():  
    command = request.form.get('command')  
    console_output.append(f"> {command}")  # Uchování příkazu  

    # Zpracování příkazu a uchování výstupu  
    try:  
        result = subprocess.check_output(command, shell=True, universal_newlines=True)  
        console_output.append(result)  
    except subprocess.CalledProcessError as e:  
        console_output.append(f"Error: {e}")  

    return render_template('index.html', output=console_output)  

def run_server():  
    app.run(host='0.0.0.0', port=5000)  # Spuštění serveru na portu 5000  

def start_web_console():  
    threading.Thread(target=run_server, daemon=True).start()  # Spustí server v novém vlákně
