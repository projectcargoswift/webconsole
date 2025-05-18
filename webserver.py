from flask import Flask, render_template, request, jsonify  

app = Flask(__name__)  

@app.route('/')  
def index():  
    return render_template('main/index.html')  

@app.route('/command', methods=['POST'])  
def command_endpoint():  
    command = request.json.get('command')  
    # Zpracování příkazu  
    response_message = f"Received command: {command}"  
    # Tady by mělo být volání ke zpracování příkazu na straně SwiftOS  
    return jsonify({"message": response_message})  

def start_web_server():  
    """Spouští webový server."""  
    app.run(host='0.0.0.0', port=8001, use_reloader=False)
