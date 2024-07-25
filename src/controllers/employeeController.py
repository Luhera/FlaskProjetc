from flask import Blueprint, render_template, request, redirect
from models.employeeModel import EmployeeModel, db
 
employee_blueprint = Blueprint('employee', __name__)
 
@employee_blueprint.route('/')
def index():
    return render_template('mainpage.html')
 
@employee_blueprint.route('/create', methods=["GET", "POST"])
def create():
   
    if request.method == 'GET':
        return render_template('createpage.html')
   
    if request.method == 'POST':
        cpf = request.form['cpf']
        name = request.form['name']
        position = request.form['position']
        employee = EmployeeModel(cpf = cpf, name = name, position=position)
       
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')
   
@employee_blueprint.route('/data')
def DataView():
    employee = EmployeeModel.query.all()
    return render_template('datalist.html',employee=employee)