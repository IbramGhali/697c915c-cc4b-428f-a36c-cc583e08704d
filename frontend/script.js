document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') {
        return; // Do nothing if the input is empty
    }

    document.getElementById('user-input').value = '';
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p>User: ${userInput}</p>`;

    fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p>Bot: ${data.answer}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
        chatBox.innerHTML += `<p>Error: Could not reach the server</p>`;
    });
}
