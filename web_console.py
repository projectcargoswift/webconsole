from flask import Flask, request, jsonify, render_template  
import os  
import threading  
import json  
from console_output import print_message  

app = Flask(__name__)  

class CommandExecutor:  
    def __init__(self):  
        self.command_registry = {}  # Registr pro příkazy  

    def process_command(self, command):  
        """Zpracovává příkazy zadané uživateli."""  
        try:  
            # Rozdělení příkazu na části  
            parts = command.split()  
            cmd_name = parts[0]  
            args = parts[1:]  

            # Zde implementujte logiku pro zpracování různých příkazů  
            # Například:  
            if command == "exit":  
                print_message("INFO", "Shutting down the application...")  
                return "System is shutting down..."  
            else:  
                return f"Executed command: {command}"  
        except Exception as e:  
            return f"Error: {e}"  

command_executor = CommandExecutor()  

@app.route('/')  
def index():  
    return render_template('index.html')  

@app.route('/command', methods=['POST'])  
def command_endpoint():  
    """Endpoint pro příjem příkazů přes HTTP POST."""  
    data = request.json  
    command = data.get('command')  
    if command:  
        result = command_executor.process_command(command)  
        return jsonify({"status": "success", "message": result}), 200  
    else:  
        return jsonify({"status": "error", "message": "No command provided"}), 400  

def run_server():  
    app.run(host='0.0.0.0', port=5000, use_reloader=False)  

if __name__ == "__main__":  
    # Spusťte server ve vlákně  
    threading.Thread(target=run_server).start()
