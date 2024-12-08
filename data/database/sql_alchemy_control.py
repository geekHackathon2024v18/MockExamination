from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import Session
from datetime import datetime
from data.table.subject import Subject
from data.table.mock_examination import MockExamination
from data.table.question import Question, QuestionType
from data.table.choice_4 import Choice4
from data.table.mock_examination_response import MockExaminationResponse
from data.table.question_response import QuestionResponse
from data.table.base import Base
from typing import List
import time

# interface継承してカプセル化して、この部分に関してやり切りたい
class SqlAlchemyControl:
    def __init__(self) -> None:
        self.__engine = create_engine("sqlite:///data/database/app.db", echo=True, future=True)
        self.__session = Session(self.__engine)
        self.debug = self.__DebugPrint(self.__session)
        self.insert = self.__Insert(self.__session)
        self.read = self.__Read(self.__session)
        self.update = self.__Update(self.__session)
        self.delete = self.__Delete(self.__session)

    # テーブル作成の関数
    def create_table(self) -> None:
        Base.metadata.create_all(self.__engine)

    class __DebugPrint:
        def __init__(self, session) -> None:
            self.__session = session

        def subject(self) -> None:
            with self.__session as session:
                stmt = select(Subject)
                for subject in session.scalars(stmt).all():
                    print(subject)

        def mock_examination(self, subject_id: int) -> None:
            with self.__session as session:
                stmt = select(MockExamination).where(MockExamination.subject_id == subject_id)
                for mock_examination in session.scalars(stmt).all():
                    print(mock_examination)

        def question(self, mock_examination_id: int) -> None:
            with self.__session as session:
                stmt = select(Question).where(Question.mock_examination_id == mock_examination_id)
                questions = session.scalars(stmt).all()
                if len(questions) == 0:
                    print("問題がありません")
                else :
                    print(len(questions))
                for question in questions:
                    print(question)
        def question_all(self) -> None:
            with self.__session as session:
                stmt = select(Question)
                for question in session.scalars(stmt).all():
                    print(question)

        def mock_examination_response(self, mock_examination_id: int) -> None:
            with self.__session as session:
                stmt = select(MockExaminationResponse).where(MockExaminationResponse.mock_examination_id == mock_examination_id)
                for mock_examination_response in session.scalars(stmt).all():
                    print(mock_examination_response)

        def question_response(self, mock_examination_response_id: int) -> None:
            with self.__session as session:
                stmt = select(QuestionResponse).where(QuestionResponse.mock_examination_response_id == mock_examination_response_id)
                for question_response in session.scalars(stmt).all():
                    print(question_response)

    class __Insert:
        def __init__(self, session) -> None:
            self.__session = session
            self.__question_list: list[Question] = []
            self.__choice4_list: list[Choice4] = []
            self.__response_list: list[QuestionResponse] = []

        # insertテンプレート関数
        def __insert_obj(self, obj) -> int|list[int]:
            id = None
            with self.__session as session:
                if type(obj) == list:
                    session.add_all(obj)
                    session.commit()
                    id  = [o.id for o in obj]
                else:
                    session.add(obj)
                    session.commit()
                    id = obj.id
            return id

        # 科目の情報を追加の関数
        def subject(self, subject_name: str) -> None:
            #型チェック
            if not isinstance(subject_name, str):
                raise TypeError("subject_name must be str")

            self.__insert_obj(Subject(subject_name=subject_name))

        def question_stack(self,
            question_sentence: str,
            question_type: QuestionType,
            answer: str
        ) -> None:
            # 型チェック
            if not isinstance(question_sentence, str):
                raise TypeError("question_sentenceはstr型で入れてね")
            if not isinstance(question_type, QuestionType):
                raise TypeError("question_typeはQuestionType型で入れてね")
            if not isinstance(answer, str):
                raise TypeError("answerはstr型で入れてね")

            self.__question_list.append(
                Question(
                    mock_examination_id=None,
                    question_sentence=question_sentence,
                    question_type=question_type,
                    answer=answer
                )
            )

        def choice4_stack(self,
            choice_1: str,
            choice_2: str,
            choice_3: str,
            choice_4: str,
        ) -> None:
            # 型チェック
            if not isinstance(choice_1, str):
                raise TypeError("choice_1はstr型で入れてね")
            if not isinstance(choice_2, str):
                raise TypeError("choice_2はstr型で入れてね")
            if not isinstance(choice_3, str):
                raise TypeError("choice_3はstr型で入れてね")
            if not isinstance(choice_4, str):
                raise TypeError("choice_4はstr型で入れてね")
            self.__choice4_list.append(
                Choice4(
                    question_id=None,
                    choice_1=choice_1,
                    choice_2=choice_2,
                    choice_3=choice_3,
                    choice_4=choice_4,
                )
            )

        # 模擬試験の情報を追加する関数
        def mock_examination(self,
            subject_id: int,
            mock_examination_name: str,
            time_limit: int = None,
        ) -> None:
            # questionをスタックしたかを確認
            if len(self.__question_list) == 0:
                raise ValueError("insert.question_stack()か、insert.question_list_stack()で問題を入れてから実行してね")
            # 型チェック
            if not isinstance(subject_id, int):
                raise TypeError("subject_idはint型で入れてね")
            if not isinstance(mock_examination_name, str):
                raise TypeError("mock_examination_nameはstr型で入れてね")
            if time_limit is not None and not isinstance(time_limit, int):
                raise TypeError("time_limitはint型で入れてね")
            if time_limit != None and time_limit < 0:
                    raise ValueError("time_limitは0以上で入れてね")

            mock_examination_obj = MockExamination(
                subject_id=subject_id,
                mock_examination_name=mock_examination_name,
                time_limit=time_limit
            )
            mock_examination_id = self.__insert_obj(mock_examination_obj)

            for question in self.__question_list:
                question.mock_examination_id = mock_examination_id
                question_id = self.__insert_obj(question)
                if question.question_type == QuestionType.CHOICE_4:
                    choice4 = self.__choice4_list.pop(0)
                    choice4.question_id = question_id
                    self.__insert_obj(choice4)

            self.__question_list = []

        # 問題の回答をスタックする関数
        def question_response_stack(self,
            question_id: int,
            response_content: str,
        ) -> None:
            # 型チェック
            if not isinstance(question_id, int):
                raise TypeError("question_idはint型で入れてね")
            if not isinstance(response_content, str):
                raise TypeError("answerはstr型で入れてね")
            self.__response_list.append(
                QuestionResponse(
                    mock_examination_response_id=None,
                    question_id=question_id,
                    response_content=response_content,
                )
            )

        # 模擬試験の回答を追加する関数
        def mock_examination_response(self,
            mock_examination_id: int,
            interruption: bool,
        ) -> None:
            # 型チェック
            if not isinstance(mock_examination_id, int):
                raise TypeError("mock_examination_idはint型で入れてね")
            if not isinstance(interruption, bool):
                raise TypeError("interruptionはbool型で入れてね")

            if len(self.__response_list) == 0:
                raise ValueError("insert.question_response_stack()で回答を入れてから実行してね")

            mock_examination_response_id = self.__insert_obj(MockExaminationResponse(
                mock_examination_id=mock_examination_id,
                interruption=interruption
            ))
            for response in self.__response_list:
                response.mock_examination_response_id = mock_examination_response_id

            self.__insert_obj(self.__response_list)

            self.__response_list = []

    class __Read:
        def __init__(self, session) -> None:
            self.__session = session

        # 科目の保存データ全てを取得
        def subject(self) -> List[Subject]:
            stmt = select(Subject)
            return self.__session.scalars(stmt).all()

        # 科目の保存データをid指定で取得
        def subject_by_id(self, id: int) -> Subject:
            stmt = select(Subject).where(Subject.id == id)
            return self.__session.scalars(stmt).one()

        # 模擬試験の保存データ全てを取得
        def mock_examination(self) -> list[MockExamination]:
            stmt = select(MockExamination)
            return self.__session.scalars(stmt).all()
        # 模擬試験の保存データをid指定で取得
        def mock_examination_by_id(self, id: int) -> MockExamination:
            stmt = select(MockExamination).where(MockExamination.id == id)
            return self.__session.scalars(stmt).one()

        # 問題の保存データ全てを取得
        def question(self, mock_examination_id: int) -> list[Question]:
            stmt = select(Question).where(Question.mock_examination_id == mock_examination_id)
            return self.__session.scalars(stmt).all()

        # 問題の保存データをid指定で取得
        def question_by_id(self,
                question_id: int
            ) -> Question:
            stmt = select(Question).\
                where(Question.id == question_id)
            return self.__session.scalars(stmt).one()

        # 模擬試験の回答の保存データ全てを取得
        def mock_examination_response(self) -> list[MockExaminationResponse]:
            stmt = select(MockExaminationResponse)
            return self.__session.scalars(stmt).all()

        # 模擬試験の回答の保存データをid指定で取得
        def mock_examination_response_by_id(self, mock_examination_response_id: int) -> MockExaminationResponse:
            stmt = select(MockExaminationResponse).where(MockExaminationResponse.id == id)
            return self.__session.scalars(stmt).one()

        # 問題の回答の保存データ全てを取得
        def question_response(self, mock_examination_response_id: int) -> list[QuestionResponse]:
            stmt = select(QuestionResponse).\
                where(QuestionResponse.mock_examination_response_id == mock_examination_response_id)
            return self.__session.scalars(stmt).all()

        # 問題の解答の保存データをid指定で取得
        def question_response_by_id(self,
            question_response_id: int,
        ) -> QuestionResponse:
            stmt = select(QuestionResponse).\
                where(QuestionResponse.id == question_response_id)
            return self.__session.scalars(stmt).one()

    class __Update:
        def __init__(self, session) -> None:
            self.__session = session

        def subject(self,
            subject_id: int,
            subject_name:str
        ) -> None:
            with self.__session as session:
                obj = session.get(Subject, subject_id)
                obj.subject_name = subject_name

                session.commit()

        def mock_examination(self,
            mock_examination_id: int,
            mock_examination_name: str,
            time_limit: int = None,
        ) -> None:
            with self.__session as session:
                obj = session.get(MockExamination, mock_examination_id)
                obj.mock_examination_name = mock_examination_name
                obj.time_limit = time_limit

                session.commit()

        def question(self,
            question_id: int,
            question_sentence: str,
            question_type: QuestionType,
            answer: str
        ) -> None:
            with self.__session as session:
                obj = session.get(Question, question_id)
                obj.question_sentence = question_sentence
                obj.question_type = question_type
                obj.answer = answer
                session.commit()

        def mock_examination_response(self,
            mock_examination_response_id: int,
            mock_examination_id: int,
            interruption: bool,
        ) -> None:
            with self.__session as session:
                obj = session.get(MockExaminationResponse, mock_examination_response_id)
                obj.mock_examination_id = mock_examination_id
                obj.interruption = interruption
                session.commit()

        def question_response(self,
            question_response_id: int,
            mock_examination_response_id:int,
            question_id: int,
            response_content: str,
        ) -> None:
            with self.__session as session:
                obj = session.get(QuestionResponse, question_response_id)
                obj.mock_examination_response_id = mock_examination_response_id
                obj.question_id = question_id
                obj.response_content = response_content
                session.commit()




    class __Delete:
        def __init__(self, session) -> None:
            self.__session = session

        def subject_by_id(self, subject_id: int) -> None:
            with self.__session as session:
                subject = session.get(Subject, subject_id)
                session.delete(subject)
                session.commit()

        def mock_examination_by_id(self, mock_examination_id: int) -> None:
            with self.__session as session:
                obj = session.get(MockExamination, mock_examination_id)
                session.delete(obj)
                session.commit()

        def question_by_id(self, question_id: int) -> None:
            with self.__session as session:
                obj = session.get(Question, question_id)
                session.delete(obj)
                session.commit()

        def mock_examination_response_by_id(self, mock_examination_response_id: int) -> None:
            with self.__session as session:
                obj = session.get(MockExaminationResponse, mock_examination_response_id)
                session.delete(obj)
                session.commit()

        def question_response_by_id(self, question_response_id: int) -> None:
            with self.__session as session:
                obj = session.get(QuestionResponse, question_response_id)
                session.delete(obj)
                session.commit()