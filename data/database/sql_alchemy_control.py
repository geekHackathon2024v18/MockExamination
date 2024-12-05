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

            with self.__session as session:
                subject = Subject(subject_name=subject_name)
                session.add(subject)
                session.commit()

        def question_stack(self,
            mock_examination_id: int,
            question_sentence: str,
            question_type: int,
            answer: str
        ) -> None:
            # 型チェック
            if not isinstance(mock_examination_id, int):
                raise TypeError("mock_examination_idはint型で入れてね")
            if not isinstance(question_sentence, str):
                raise TypeError("question_sentenceはstr型で入れてね")
            if not isinstance(question_type, int):
                raise TypeError("question_typeはint型で入れてね")
            if not isinstance(answer, str):
                raise TypeError("answerはstr型で入れてね")

            self.question_list.append(
                Question(
                    mock_examination_id=mock_examination_id,
                    question_sentence=question_sentence,
                    question_type=question_type,
                    answer=answer
                )
            )

        # 模擬試験の情報を追加する関数
        def mock_examination(self,
            subject_id: int,
            mock_examination_name: str,
            time_limit: int = None,
        ) -> None:
            # questionをスタックしたかを確認
            if len(self.question_list) == 0:
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
            self.__insert_subject(
                self.question_list + [
                    MockExamination(
                        subject_id=subject_id,
                        mock_examination_name=mock_examination_name,
                        time_limit=time_limit
                    )
                ]
            )
            self.question_list = []

        # 問題の回答をスタックする関数
        def question_response_stack(self,
            mock_examination_response_id: int,
            question_id: int,
            answer: str
        ):
            # 型チェック
            if not isinstance(mock_examination_response_id, int):
                raise TypeError("mock_examination_response_idはint型で入れてね")
            if not isinstance(question_id, int):
                raise TypeError("question_idはint型で入れてね")
            if not isinstance(answer, str):
                raise TypeError("answerはstr型で入れてね")
            if len(self.question_list) == 0:
                raise ValueError("insert.question_stack()で問題を入れてから実行してね")
            self.response_list.append(
                QuestionResponse(
                    mock_examination_response_id=mock_examination_response_id,
                    question_id=question_id,
                    response_content=answer
                )
            )

        # 模擬試験の回答を追加する関数
        def mock_examination_response(self,
            mock_examination_id: int,
            user_id: int,
            score: int,
            time: int
        ):
            # 型チェック
            if not isinstance(mock_examination_id, int):
                raise TypeError("mock_examination_idはint型で入れてね")
            if not isinstance(user_id, int):
                raise TypeError("user_idはint型で入れてね")
            if not isinstance(score, int):
                raise TypeError("scoreはint型で入れてね")
            if not isinstance(time, int):
                raise TypeError("timeはint型で入れてね")
            if score < 0:
                raise ValueError("scoreは0以上で入れてね")
            if time < 0:
                raise ValueError("timeは0以上で入れてね")

            if len(self.response_list) == 0:
                # すでに追加されている問題の数分、未回答として追加する
                pass
            self.__insert_subject(
                self.response_list + [
                    MockExaminationResponse(
                        mock_examination_id=mock_examination_id,
                        user_id=user_id,
                        score=score,
                        time=time
                    )
                ]
            )
            self.response_list = []


    # オブジェクト取得の関数
    def get_object(self, table_type: tableType, id: int):
        with self.__session as session:
            if table_type == tableType.SUBJECT:
                return session.execute(select(Subject)).scalars().all()
            elif table_type == tableType.MOCK_EXAMINATION:
                return session.get(MockExamination, id)
            elif table_type == tableType.QUESTION:
                return session.get(Question, id)
            elif table_type == tableType.MOCK_EXAMINATION_RESPONSE:
                return session.get(MockExaminationResponse, id)
            elif table_type == tableType.QUESTION_RESPONSE:
                return session.get(QuestionResponse, id)
            else:
                return None

    # デバッグ用の関数
    def main(self):
        # シンプルなセレクト
        stmt = select(Subject)
        for subject in self.__session.execute(stmt).scalars():
            print(subject)



# # subjectオブジェクト削除の関数
# def delete_subject_object_by_id(engine, subject_id: int):
#     with Session(engine) as session:
#         session.query(Subject).\
#             filter(Subject.subject_id==subject_id).\
#             delete()
#         session.commit()
