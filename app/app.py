from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="kind"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello, World!'")
    message = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return message

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
