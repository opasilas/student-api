from crypt import methods
from flask import jsonify, request, abort
from app import app, db
from app.models import Student
from sqlalchemy import text

# Get all students
@app.route('/api/v1/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    if students:
        return jsonify([student.serialize() for student in students])
    else:
        return jsonify({'message': 'No student records found'})
    
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
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'message': 'Student does not exist'})
        

@app.route('/api/v1/students', methods=['DELETE'])
def clear():
    Student.query.delete()
    db.session.commit()

    db.session.execute(text("ALTER SEQUENCE student_id_seq RESTART WITH 1"))
    db.session.commit()
    return jsonify({'message': 'Deleted all students'})

@app.route('/api/v1/students/health', methods=['GET'])
def healthcheck():
    return jsonify({'status': 'ok'})
