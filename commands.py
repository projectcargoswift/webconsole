from webconsole.webserver import start_web_server  # Absolutní import

def register_commands(command_registry):  
    """Registruje příkazy pro spuštění webové konzole."""  
    command_registry['start-web-console'] = start_web_server

