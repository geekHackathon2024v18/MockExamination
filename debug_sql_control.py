from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question
from data.table.subject import Subject
from data.table.question import QuestionType

db = SqlAlchemyControl()
# database.create_table()
# database.debug.mock_examination(subject_id=7)
# print(database.read.subject())
# mock1 = database.read.mock_examination_by_id(id=1)
# print(mock1)

# subjectの追加
# database.insert.subject(subject_name="共通")
# print(database.read.subject())

# mock_examinationの追加
# insert_questions = [
#     {
#     "question_sentence": "インターネット層のプロトコルではないものは？",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "PPP"
#     },
#     {
#     "question_sentence": "有線LANで使用される搬送波感知多重アクセス/衝突検知方式は？",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "CSMA/CD"
#     },
#     {
#     "question_sentence": "IPv4アドレス表記として正しくないのはどれか",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "192.168.15.256"
#     },
#     {
#     "question_sentence": "ネットワーク部を25ビットとするときのサブネットマスクはどれか",
#     "question_type": QuestionType.DESCRIPTIVE,
#     "answer": "255.255.255.128"
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
#     mock_examination_name="情報ネットワークの問題",
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

# choice4を操作
# data = {
# "mock_examination_name": "情報ネットワーク 第9回 模擬試験",
#   "question_list": [
#    {
#       "question_sentence": "VRRP (Virtual Router Redundancy Protocol) の主な目的は？",
#       "choice_1": "IPアドレスの動的な割り当て",
#       "choice_2": "ルーターの冗長化",
#       "choice_3": "ネットワークのセキュリティ強化",
#       "choice_4": "通信品質の制御",
#       "answer": "2"
#     },
#     {
#       "question_sentence": "IPマルチキャストで利用されるアドレスクラスはどれか？",
#       "choice_1": "クラスA",
#       "choice_2": "クラスB",
#       "choice_3": "クラスC",
#       "choice_4": "クラスD",
#       "answer": "4"
#     }
#   ]
# }

# for question in data["question_list"]:
#     db.insert.question_stack(
#         question_sentence=question["question_sentence"],
#         question_type=QuestionType.CHOICE_4,
#         answer=question["answer"]
#     )

#     db.insert.choice4_stack(
#         choice_1=question["choice_1"],
#         choice_2=question["choice_2"],
#         choice_3=question["choice_3"],
#         choice_4=question["choice_4"]
#     )

# db.insert.mock_examination(
#     subject_id=1,
#     mock_examination_name=data["mock_examination_name"],
# )

for mock_examination in db.read.mock_examination():
    print('\n[mock_examination]')
    print(mock_examination)
    for question in db.read.question(mock_examination_id=mock_examination.id):
        print("\n[question]")
        print(question)
        for choice4 in db.read.choice4(question_id=question.id):
            print("\n[choice4]")
            print(choice4)
