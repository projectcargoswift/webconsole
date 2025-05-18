const output = document.getElementById('output');  
const commandInput = document.getElementById('commandInput');  

// Simulace příkazů  
const commands = [  
    "Server marked as running...",  
    "Internal Database optimized. This applies only for the internal database.",  
    "0 players that haven't connected in the past 16 days and had less than 2 hours of playtime.",  
    "0 whitelist requests older than a week.",  
    "0 whitelist approvals older than a week."  
];  

// Zobrazit výstup  
function displayOutput(message) {  
    output.innerHTML += message + '<br>';  
    output.scrollTop = output.scrollHeight; // Posuňte na konec  
}  

commandInput.addEventListener('keydown', (event) => {  
    if (event.key === 'Enter') {  
        const command = commandInput.value;  
        commandInput.value = ''; // Vymazat vstup  

        displayOutput(`> ${command}`); // Zobrazit příkaz  

        // Zobrazit simulaci výstupu  
        commands.forEach((msg, index) => {  
            setTimeout(() => {  
                displayOutput(msg);  
            }, index * 1000); // Časový interval pro simulaci  
        });  
    }  
});
