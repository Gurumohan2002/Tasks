from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from urllib.parse import quote

#used encoded for the password since it contains the @ symbol in it
password = "Guru@2607"
encoded_password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{encoded_password}@localhost:5433/studentsdetails"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

uploads = Blueprint('uploads', __name__)

db = SQLAlchemy(app)

# Student Class contains details of the student
class students(db.Model):
    __tablename__ = 'Students'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000))
    addr = db.Column(db.String(1000))
    dept = db.Column(db.String(100))
    phone =db.Column(db.String(15))    
    
with app.app_context():
    db.create_all()

#API for adding students using JSON format and the user have to give the details of the student by using POST method
@app.route('/addstudents', methods=['POST'])
def add_students():
    try:
        data = request.get_json()
        new_student = students(id=data['id'],name=data['name'], addr=data['addr'], dept=data['dept'], phone=data['phone'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message':'Student added successfully'})
    
    except KeyError as e:
        return jsonify({'error': f'Missing key in data: {e}'}), 400
    
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

# API for displaying the students list which was given by the user using GET method
@app.route('/showlist', methods=['GET'])
def get_details():
    try:
        stud = students.query.all()
        student_list = []
        for student in stud:
            student_list.append({'id': student.id, 'name': student.name, 'addr': student.addr, 'dept' : student.dept , 'phone':student.phone})
        return jsonify({'stud': student_list })
    
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

#API for updating the details of the student using PUT method
@app.route('/update/<int:id>',methods=['PUT'])
def update_list(id):
    try:
        data=request.get_json()
        print(data)
        name = data.get('name')
        addr = data.get('addr')
        dept=data.get('dept')
        phone=data.get('phone')
        
        new_student = students.query.get(id)
        if not new_student:
            return jsonify({'error': 'Student not found'}), 404
        new_student.name = name
        new_student.addr = addr
        new_student.dept = dept
        new_student.phone = phone
        db.session.commit()
        
        return 'User updated successfully'
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

#API for deleting the student record using the input id given by the user in the URL using DELETE method
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = students.query.get(id)
        if not student:
            return jsonify({'Student not found'}), 404
        
        db.session.delete(student)
        db.session.commit()
        
        return jsonify({'message':'Student deleted successfully'})
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500
    
#Main function
if __name__ == '_main_':
    app.run(debug=True)