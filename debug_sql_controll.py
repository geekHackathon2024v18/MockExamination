from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question
from data.table.subject import Subject
from data.table.question import QuestionType

database = SqlAlchemyControl()
# database.debug.mock_examination(subject_id=7)
# print(database.read.subject())
# mock1 = database.read.mock_examination_by_id(id=1)
# print(mock1)

# subjectの追加
# database.insert.subject(subject_name="mock_subject")
# print(database.read.subject())

# mock_examinationの追加
# insert_questions = [
#     {
#     "question_sentence": "問題文1",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "答え1"
#     },
#     {
#     "question_sentence": "問題文2",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "答え2"
#     },
#     {
#     "question_sentence": "問題文3",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "答え3"
#     }
# ]

# for insert_question in insert_questions:
#     database.insert.question_stack(
#         question_sentence=insert_question["question_sentence"],
#         question_type=insert_question["question_type"],
#         answer=insert_question["answer"]
#     )

# database.insert.mock_examination(
#     subject_id=1,
#     mock_examination_name="mock_examination",
# )

# [print(i) for i in database.read.mock_examination()]
[print(i) for i in database.read.question(mock_examination_id=3)]
