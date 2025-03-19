from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    medical_schools = db.Column(db.Text, nullable=False)
    degrees = db.Column(db.Text, nullable=False)
    specialization = db.Column(db.Text, nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    licensing_authority = db.Column(db.String(100), nullable=False)
    license_expiry = db.Column(db.String(20), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    previous_employment = db.Column(db.Text, nullable=False)
    current_workplace = db.Column(db.String(100), nullable=False)
    security_question = db.Column(db.String(100), nullable=False)
    security_answer = db.Column(db.String(100), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    medical_schools = ','.join(data.getlist('medicalSchool[]'))
    degrees = ','.join(f"{d},{g}" for d, g in zip(data.getlist('degree[]'), data.getlist('graduationYear[]')))
    new_doctor = Doctor(
        full_name=data['fullName'],
        email=data['email'],
        password=data['password'],
        contact_number=data['contactNumber'],
        gender=data['gender'],
        medical_schools=medical_schools,
        degrees=degrees,
        specialization=','.join(data.getlist('specialization[]')),
        license_number=data['licenseNumber'],
        licensing_authority=data['licensingAuthority'],
        license_expiry=data['licenseExpiry'],
        years_of_experience=data['yearsOfExperience'],
        previous_employment=data['previousEmployment'],
        current_workplace=data['currentWorkplace'],
        security_question=data['securityQuestion'],
        security_answer=data['securityAnswer']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor registered successfully!'})

if __name__ == '__main__':
    if not os.path.exists('doctors.db'):
        db.create_all()
    app.run(debug=True)
