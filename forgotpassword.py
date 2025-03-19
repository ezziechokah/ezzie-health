from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    security_question = db.Column(db.String(200), nullable=False)
    security_answer = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'security_question': user.security_question})
    return jsonify({'message': 'Email not found'}), 404

@app.route('/verify_answer', methods=['POST'])
def verify_answer():
    data = request.get_json()
    email = data.get('email')
    answer = data.get('securityAnswer')
    user = User.query.filter_by(email=email).first()
    if user and user.security_answer == answer:
        return jsonify({'message': 'Correct answer. You can now reset your password.'})
    return jsonify({'message': 'Incorrect answer'}), 400

@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('newPassword')
    user = User.query.filter_by(email=email).first()
    if user:
        user.password = new_password
        db.session.commit()
        return jsonify({'message': 'Password reset successfully'})
    return jsonify({'message': 'Email not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('users.db'):
            db.create_all()
    app.run(debug=True)
