from flask import Flask, render_template, request, jsonify  

app = Flask(__name__, static_folder='packages/webconsole/static')  # Ujistěte se, že je správná cesta  

@app.route('/')  
def index():  
    return render_template('main/index.html')  

@app.route('/command', methods=['POST'])  
def command_endpoint():  
    command = request.json.get('command')  
    # Zpracování příkazu (můžete přidat vlastní logiku zde)  
    response_message = f"Received command: {command}"  
    return jsonify({"message": response_message})  

def start_web_server():  
    """Spouští webový server."""  
    app.run(host='0.0.0.0', port=8001, use_reloader=False)  

if __name__ == "__main__":  
    start_web_server()
