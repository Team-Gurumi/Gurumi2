from flask import Flask, request, jsonify
from service import perform_dummy_task

app = Flask(__name__)

@app.route('/task', methods=['POST'])
def receive_task():
    task_result = perform_dummy_task()
    return jsonify(task_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)