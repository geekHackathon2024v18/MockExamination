from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question
from data.table.subject import Subject
from data.table.question import QuestionType

database = SqlAlchemyControl()
# database.create_table()
# database.debug.mock_examination(subject_id=7)
# print(database.read.subject())
# mock1 = database.read.mock_examination_by_id(id=1)
# print(mock1)

# subjectの追加
# database.insert.subject(subject_name="mock_subject1")
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
# [print(i) for i in database.read.question(mock_examination_id=1)]


# mock_examination_responseの追加
# insert_question_responses = [
#     {
#     "question_id": 1,
#     "response_content": "答え1",
#     },
#     {
#     "question_id": 2,
#     "response_content": "答え2",
#     },
#     {
#     "question_id": 3,
#     "response_content": "答え3",
#     }
# ]

# for insert_question_response in insert_question_responses:
#     database.insert.question_response_stack(
#         question_id=insert_question_response["question_id"],
#         response_content=insert_question_response["response_content"],
#     )

# database.insert.mock_examination_response(
#     mock_examination_id=1,
#     interruption=False
# )
# [print(i) for i in database.read.mock_examination_response()]
# [print(i) for i in database.read.question_response(mock_examination_response_id=1)]


# # mock_examinationとquestionテーブルの操作

# insert_question_stack = [
#     {
#         "question_sentence": "サンプルの問題1の問題文です",
#         "question_type": QuestionType.DESCRIPTIVE,
#         "answer": "サンプルの問題1の答え"
#     },
#     {
#         "question_sentence": "サンプルの問題2の問題文です",
#         "question_type": QuestionType.DESCRIPTIVE,
#         "answer": "サンプルの問題2の答え"
#     },
# ]

# for insert_question in insert_question_stack:
#     database.insert.question_stack(
#         question_sentence=insert_question["question_sentence"],
#         question_type=insert_question["question_type"],
#         answer=insert_question["answer"]

#     )
# database.insert.mock_examination(
#     subject_id=1,
#     mock_examination_name="削除と編集を検証するサンプルの問題",
#     time_limit=50
# )
# obj = database.read.mock_examination_by_id(id=4)
# database.update.mock_examination(
#     mock_examination_id=4,
#     mock_examination_name="編集は検証しました",
#     time_limit=obj.time_limit
# )

# obj = database.read.question_by_id(question_id=8)
# database.update.question(
#     question_id=8,
#     question_sentence="変更しました",
#     question_type=obj.question_type,
#     answer="変更しました"
# )


# # 出力
# for mock_examination in database.read.mock_examination():
#     print(mock_examination)
#     print("question ↓")
#     [print(question) for question in database.read.question(mock_examination_id=mock_examination.id)]



# mock_examination_responseとquestion_responseの操作

# for mock_examination_response in database.read.mock_examination_response():
#     print(mock_examination_response)
#     print("response ↓")
    # [database.delete.question_response_by_id(question_response_id=question_response.id) for question_response in database.read.question_response(mock_examination_response_id=mock_examination_response.id)]
    # database.delete.mock_examination_response_by_id(mock_examination_response_id=mock_examination_response.id)

# database.delete.question_response_by_id(question_response_id=3)
# try:
#     i = database.read.question_response_by_id(question_response_id=3)
#     print(i)
# except Exception as e:
#     print(e)
