from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializar banco de dados (SQLite)
def init_db():
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       sender TEXT,
                       message TEXT)''')
    conn.commit()
    conn.close()

# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint para receber mensagens do chat
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data['message']

    # Aqui você pode adicionar lógica de IA ou resposta automática
    bot_response = "Estou aqui para ajudar!"

    # Salvar mensagens no banco de dados
    save_message("user", user_message)
    save_message("bot", bot_response)

    return jsonify({'response': bot_response})

# Função para salvar mensagens no banco de dados
def save_message(sender, message):
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

#http://127.0.0.1:5000/