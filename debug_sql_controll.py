from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question

database = SqlAlchemyControl()

database.insert.mock_examination(1, "模擬試験1", [
    Question(question_sentence="問題1", answer="回答1", question_type=1),
    Question(question_sentence="問題2", answer="回答2", question_type=1),
    Question(question_sentence="問題3", answer="回答3", question_type=1)
], 60)

