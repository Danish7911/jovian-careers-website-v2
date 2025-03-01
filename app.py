from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database'
}

def get_jobs():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, title, location, salary FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    connection.close()
    return jobs

@app.route("/")
def hello_world():
    jobs = get_jobs()
    return render_template('index.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = get_jobs()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)