from flask import Flask, jsonify, request

app = Flask(__name__)

incidents = [
    {
        "id": "INC001",
        "title": "Website Down",
        "severity": "HIGH",
        "status": "OPEN"
    },
    {
        "id": "INC002",
        "title": "Database Error",
        "severity": "MEDIUM",
        "status": "OPEN"
    }
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)


@app.route("/incidents", methods=["POST"])
def create_incident():

    data = request.get_json()

    incident = {
        "id": f"INC{len(incidents) + 1:03d}",
        "title": data.get("title"),
        "severity": data.get("severity", "LOW"),
        "status": "OPEN"
    }

    incidents.append(incident)

    return jsonify(incident), 201


@app.route("/incidents/<incident_id>", methods=["GET"])
def get_incident(incident_id):

    for incident in incidents:
        if incident["id"] == incident_id:
            return jsonify(incident)

    return jsonify({
        "error": "Incident not found"
    }), 404


@app.route("/incidents/<incident_id>", methods=["PUT"])
def update_incident(incident_id):

    data = request.get_json()

    for incident in incidents:
        if incident["id"] == incident_id:

            if "title" in data:
                incident["title"] = data["title"]

            if "severity" in data:
                incident["severity"] = data["severity"]

            if "status" in data:
                incident["status"] = data["status"]

            return jsonify(incident)

    return jsonify({
        "error": "Incident not found"
    }), 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )