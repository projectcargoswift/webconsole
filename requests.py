import requests  

# Funkce pro odeslání příkazu na webový server  
def send_command(command):  
    response = requests.post('http://localhost:8001/command', json={'command': command})  
    return response.json()
