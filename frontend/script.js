document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
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
    });
});
