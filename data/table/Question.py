from datetime import datetime as dt
from enum import Enum

# 回答タイプの定義
class QuestionType(Enum):
    CHOICE_4 = 1
    CHOICE_2 = 2
    DESCRIPTIVE = 3

# 模擬試験の問いの情報を持つテーブル
class Question:
    def __init__(self,
        mock_examination_id: int,
        question_sentence: str,
        question_type: QuestionType,
        answer: str,
        question_id: int = None,
        created_at: dt = dt.now(),
        updated_at: dt = dt.now()
    ):
        self.question_id = question_id
        self.mock_examination_id = mock_examination_id
        self.question_sentence = question_sentence
        self.question_type = question_type
        self.answer = answer
        self.created_at = created_at
        self.updated_at = updated_at

