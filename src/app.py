from flask import Flask 
from models.employeeModel import db
from controllers.employeeController import employee_blueprint

app = Flask ( __name__, template_folder="views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(employee_blueprint, url_prefix='/') #ta avisando que tem um gerenciador de rotas

if __name__ =="__main__":
 with app.app_context(): #criação do banco ja quando o aplicativo é inicializado. 
      db.create_all()
 app.run()