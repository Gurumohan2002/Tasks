from functools import wraps
from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from urllib.parse import quote

#used encoded for the password since it contains the @ symbol in it
password = "Guru@2607"
encoded_password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{encoded_password}@localhost:5433/employeedetails"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

uploads = Blueprint('uploads', __name__)
db = SQLAlchemy(app)

# Employee Class contains details of the employees
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50),nullable = False)
    
with app.app_context():
    db.create_all()

# Decorators for the API
def log_api_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"API call: {request.method} {request.url}")
        return func(*args, **kwargs)
    return wrapper

# Exceptional Handling for the API
def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return wrapper

#API for Displaying the employee details using GET method
@app.route('/employeesshow', methods=['GET'])
@log_api_call
@handle_exceptions
def get_employees():
    employees = Employee.query.all()
    employee_list = [{"id": emp.id, "name": emp.name, "age": emp.age, "designation": emp.designation , "team":emp.team} for emp in employees]
    return jsonify(employee_list)

#API for getting a specific employee detail from the employee list using GET method
@app.route('/employeeshow/<int:employee_id>', methods=['GET'])
@log_api_call
@handle_exceptions
def get_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        return jsonify({"id": employee.id, "name": employee.name, "age": employee.age, "designation": employee.designation , "team" : employee.team})
    else:
        raise ValueError(f"Employee with ID {employee_id} not found")

#API for Adding the employees in the Employee list using the POST method
@app.route('/employeeadd', methods=['POST'])
@log_api_call
@handle_exceptions
def add_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], age=data['age'], designation=data['designation'], team=data['team'] )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": f"Employee added with ID {new_employee.id}"}), 201

#API for Updating the employee details using their id and PUT method
@app.route('/employeeupdate/<int:employee_id>', methods=['PUT'])
@log_api_call
@handle_exceptions
def update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        data = request.get_json()
        employee.name = data['name']
        employee.age = data['age']
        employee.designation = data['designation']
        employee.team = data['team']
        db.session.commit()
        return jsonify({"message": f"Employee with ID {employee_id} updated"})
    else:
        raise ValueError(f"Employee with ID {employee_id} not found")

#API for deleting an employee record from the Employee table using DELETE method
@app.route('/employeedelete/<int:employee_id>', methods=['DELETE'])
@log_api_call
@handle_exceptions
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": f"Employee with ID {employee_id} deleted"})
    else:
        raise ValueError(f"Employee with ID {employee_id} not found")

#Main function
if __name__ == '__main__':
    app.run()