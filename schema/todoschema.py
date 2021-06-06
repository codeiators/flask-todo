
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from model.todomodel import Todo
from config.config import db

class TodoSchema(SQLAlchemySchema):
   class Meta:
       model = Todo
       sqla_session = db.session
   id = auto_field()
   title = auto_field()
   todo_description = auto_field()