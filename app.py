from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample doctor data
doctors = [
    {"id": 1, "name": "Dr. Rahul Kapoor", "specialty": "Cardiologist"},
    {"id": 2, "name": "Dr. Ananya Sharma", "specialty": "Dermatologist"},
    {"id": 3, "name": "Dr. Sanjay Verma", "specialty": "Orthopedic"},
    {"id": 4, "name": "Dr. Priya Gupta", "specialty": "Gynecologist"},
    {"id": 5, "name": "Dr. Amit Joshi", "specialty": "Neurologist"}
]

# In-memory appointments list
appointments = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/doctors", methods=["GET"])
def get_doctors():
    return jsonify(doctors)

@app.route("/api/appointments", methods=["POST"])
def book_appointment():
    data = request.get_json()

    doctor_id = data.get("doctor_id")
    patient_name = data.get("patient_name")
    day = data.get("day")
    time = data.get("time")

    if not all([doctor_id, patient_name, day, time]):
        return jsonify({"error": "Missing fields"}), 400

    appointment = {
        "doctor_id": doctor_id,
        "patient_name": patient_name,
        "day": day,
        "time": time
    }

    appointments.append(appointment)

    return jsonify({"message": "Appointment booked successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
