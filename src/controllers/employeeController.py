from flask import Blueprint, render_template, request, redirect,abort
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


@employee_blueprint.route('/data/<int:id>')
def findEmployee(id): #Fazendo uma busca pelo id do employee
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee: #tratamento de erro para caso nao exista o ID
     return render_template('data.html',employee=employee)
    return f"Empregado com id={id} não existe"

@employee_blueprint.route("/data/<int:id>/update},", methods=['GET', 'POST'])
def update(id):
    employee = EmployeeModel.query.get(id)
    if not employee:
        return f"Empregado com id={id} não existe"

    if request.method == 'POST':
        employee.cpf = request.form["cpf"]
        employee.name = request.form["name"]
        employee.position = request.form["position"]

        db.session.commit() #fazem os dados irem para o banco de dados
        return redirect(f'/data/{id}')

    return render_template('update.html',employee=employee)

@employee_blueprint.route("/data/<int:id>/delete", methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()

            return redirect('/data')
        abort(404)
    return render_template('delete.html',employee=employee)