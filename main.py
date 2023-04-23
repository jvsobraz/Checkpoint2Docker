from flask import Flask, jsonify, request
import mysql.connector
import os

db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_auth_plugin = os.environ['AUTH_PLUGIN']

db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    auth_plugin=db_auth_plugin
)

cursor = db.cursor()
cursor.execute("CREATE TABLE contas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), saldo FLOAT)")

app = Flask(__name__)

@app.route('/contas', methods=['POST'])
def adicionar_conta():
    nome = request.json['nome']
    saldo = request.json['saldo']
    cursor = db.cursor()
    cursor.execute("INSERT INTO contas (nome, saldo) VALUES (%s, %s)", (nome, saldo))
    db.commit()
    return jsonify({'mensagem': 'Conta adicionada com sucesso'})

@app.route('/contas/<int:id>', methods=['PUT'])
def atualizar_conta(id):
    nome = request.json['nome']
    saldo = request.json['saldo']
    cursor = db.cursor()
    cursor.execute("UPDATE contas SET nome=%s, saldo=%s WHERE id=%s", (nome, saldo, id))
    db.commit()
    return jsonify({'mensagem': 'Conta atualizada com sucesso'})

@app.route('/contas', methods=['GET'])
def ler_contas():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM contas")
    contas = []
    for (id, nome, saldo) in cursor:
        contas.append({'id': id, 'nome': nome, 'saldo': saldo})
    return jsonify(contas)

@app.route('/contas/<int:id>', methods=['DELETE'])
def excluir_conta(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM contas WHERE id=%s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Conta excluída com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)


# pip install Flask
# pip install mysql-connector-python
