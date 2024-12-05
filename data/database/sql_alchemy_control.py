from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from datetime import datetime
from data.table.subject import Subject
from data.table.mock_examination import MockExamination
from data.table.question import Question
from data.table.mock_examination_response import MockExaminationResponse
from data.table.question_response import QuestionResponse
from data.table.base import Base
from typing import List

# interface継承してカプセル化して、この部分に関してやり切りたい
class SqlAlchemyControl:
    def __init__(self) -> None:
        self.__engine = create_engine("sqlite:///data/database/app.db", echo=True, future=True)
        self.__session = Session(self.__engine)
        self.insert = self.Insert(self.__session)

    # テーブル作成の関数
    def create_table(self) -> None:
        Base.metadata.create_all(self.engine)

    class Insert:
        def __init__(self, session) -> None:
            self.__session = session
            self.question_list: list[Question] = []
            self.response_list: list[QuestionResponse] = []

        # insertテンプレート関数
        def __insert_subject(self, obj) -> None:
            with self.__session as session:
                if type(obj) == list:
                    session.add_all(obj)
                else:
                    session.add(obj)
                session.commit()

        # 科目の情報を追加の関数
        def subject(self, subject_name: str) -> None:
            #型チェック
            if not isinstance(subject_name, str):
                raise TypeError("subject_name must be str")

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

