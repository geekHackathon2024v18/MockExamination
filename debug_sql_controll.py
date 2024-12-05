from data.database.sql_alchemy_control import SqlAlchemyControl
from data.table.question import Question
from data.table.subject import Subject
from data.table.question import QuestionType

database = SqlAlchemyControl()
# database.debug.mock_examination(subject_id=7)
# database.debug.question_all()
# mock1 = database.read.mock_examination_by_id(id=1)
# print(mock1)

insert_questions = [
    {
    "question_sentence": "問題文1",
    "question_type": QuestionType.DESCRIPTIVE,
    "answer": "答え1"
    },
    {
    "question_sentence": "問題文2",
    "question_type": QuestionType.DESCRIPTIVE,
    "answer": "答え2"
    },
    {
    "question_sentence": "問題文3",
    "question_type": QuestionType.DESCRIPTIVE,
    "answer": "答え3"
    }
]

for insert_question in insert_questions:
    database.insert.question_stack(
        mock_examination_id=,
        question_sentence=insert_question["question_sentence"],
        question_type=insert_question["question_type"],
        answer=insert_question["answer"]
    )

database.insert.mock_examination(
    subject_id=7,
    mock_examination_name="db検証: 模擬試験2",
)
