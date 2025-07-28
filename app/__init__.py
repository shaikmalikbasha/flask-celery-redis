from flask import Flask, request, jsonify
from app.tasks import process_match

app = Flask(__name__)


@app.route("/match", methods=["POST"])
def match():
    data = request.get_json()
    task = process_match.delay(data)
    return jsonify({"task_id": task.id}), 202


@app.route("/status/<task_id>", methods=["GET"])
def task_status(task_id):
    print("Checking status for task:", task_id)
    task = process_match.AsyncResult(task_id)
    if task.state == "PENDING":
        response = {"state": task.state, "status": "Pending..."}
    elif task.state != "FAILURE":
        response = {"state": task.state, "result": task.result}
    else:
        response = {"state": task.state, "status": str(task.info)}  # Exception info
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
