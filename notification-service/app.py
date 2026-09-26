from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "notification-service"
    })


@app.route("/notify", methods=["POST"])
def notify():

    data = request.get_json()

    print("\n🚨 NEW INCIDENT")
    print(f"ID: {data.get('id')}")
    print(f"Title: {data.get('title')}")
    print(f"Severity: {data.get('severity')}")
    print("Notification processed successfully.\n")

    return jsonify({
        "message": "Notification processed successfully",
        "incident_id": data.get("id")
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )