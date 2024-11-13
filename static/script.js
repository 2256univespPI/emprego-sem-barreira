// script.js
function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value;
    if (message.trim() === '') return;

    // Adiciona a mensagem do usuário no chat
    addMessage(message, 'user');
    input.value = '';

    // Envia a mensagem para o servidor Flask
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        // Adiciona a resposta do bot no chat
        addMessage(data.response, 'bot');
    });
}