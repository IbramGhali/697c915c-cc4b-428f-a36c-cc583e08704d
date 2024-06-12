// Add event listener for the send button
document.getElementById("send-button").addEventListener("click", sendMessage);

// Add event listener for the Enter key in the input field
document
  .getElementById("user-input")
  .addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

// Function to send a message
function sendMessage() {
  const userInput = document.getElementById("user-input").value;
  if (userInput.trim() === "") {
    return; // Do nothing if the input is empty
  }

  // Clear the input field
  document.getElementById("user-input").value = "";

  // Get the chat box element and append the user's message
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<p>User: ${userInput}</p>`;

  // Send the user's message to the backend
  fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question: userInput }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Append the bot's response to the chat box
      chatBox.innerHTML += `<p>Bot: ${data.answer}</p>`;
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch((error) => {
      console.error("Error:", error);
      chatBox.innerHTML += `<p>Error: Could not reach the server</p>`;
    });
}
