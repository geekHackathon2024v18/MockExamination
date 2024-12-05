from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question

database = SqlAlchemyControl()

subject_data = database.read.subject()
[print(subject) for subject in subject_data]
