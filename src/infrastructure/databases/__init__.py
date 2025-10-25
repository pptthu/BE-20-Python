from infrastructure.databases.mssql import init_mssql
from infrastructure.models import course_register_model, todo_model, user_model, course_model, consultant_model, appointment_model

def init_db(app):
    init_mssql(app)
    
from infrastructure.databases.mssql import Base