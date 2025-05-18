document.getElementById('sendCommand').addEventListener('click', function() {  
    const command = document.getElementById('commandInput').value;  
    fetch('/command', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/json',  
        },  
        body: JSON.stringify({ command: command }),  
    })  
    .then(response => response.json())  
    .then(data => {  
        document.getElementById('output').innerText = data.message;  
    })  
    .catch((error) => {  
        document.getElementById('output').innerText = 'Error: ' + error;  
    });  
});
