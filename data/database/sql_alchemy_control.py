from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from datetime import datetime
from data.table.subject import Subject
from data.table.mock_examination import MockExamination
from data.table.question import Question
from data.table.mock_examination_response import MockExaminationResponse
from data.table.question_response import QuestionResponse
from data.table.base import Base

# テーブル作成の関数
def create_table(engine):
    Base.metadata.create_all(engine)

# オブジェクト追加の関数
def insert_object(engine, obj):
    with Session(engine) as session:
        add_obj = obj
        session.add(add_obj)
        session.commit()

engine = create_engine("sqlite:///data/database/app.db", echo=True, future=True)

# create_table(engine)

# subjectテーブル追加の例
# insert_object(
#     engine = engine,
#     obj = Subject(
#         subject_name = "線形代数"
#     )
# )

