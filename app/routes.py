from flask import jsonify, request, abort
from app import app, db
from app.models import Student

# Get all students
@app.route('/api/v1/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.serialize() for student in students])

# Get a student by ID
@app.route('/api/v1/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify(student.serialize())

# Add a new student
@app.route('/api/v1/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Missing name or email field'}), 400
    student = Student(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify(student.serialize()), 201

# Update existing student information
@app.route('/api/v1/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    data = request.get_json()
    if 'name' in data:
        student.name = data['name']
    if 'email' in data:
        student.email = data['email']
    db.session.commit()
    return jsonify(student.serialize())

# Delete a student record
@app.route('/api/v1/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
