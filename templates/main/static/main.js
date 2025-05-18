const output = document.getElementById('output');  
const commandInput = document.getElementById('commandInput');  

function displayOutput(message) {  
    output.innerHTML += message + '<br>';  
    output.scrollTop = output.scrollHeight; // Posuňte na konec  
}  

commandInput.addEventListener('keydown', async (event) => {  
    if (event.key === 'Enter') {  
        const command = commandInput.value;  
        commandInput.value = ''; // Vymazat vstup  
        displayOutput(`> ${command}`); // Zobrazit příkaz  

        try {  
            const response = await fetch('/command', {  
                method: 'POST',  
                headers: {  
                    'Content-Type': 'application/json'  
                },  
                body: JSON.stringify({ command: command })  
            });  

            const data = await response.json();  
            displayOutput(data.message); // Zobrazit odpověď serveru  
        } catch (error) {  
            displayOutput('Error: ' + error.message);  
        }  
    }  
});
