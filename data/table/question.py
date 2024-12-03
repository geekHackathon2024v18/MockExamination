from datetime import datetime as dt
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from data.table.base import Base

from enum import Enum

# 回答タイプの定義
class QuestionType(Enum):
    CHOICE_4 = 1
    CHOICE_2 = 2
    DESCRIPTIVE = 3

# 模擬試験の問いの情報を持つテーブル
class Question(Base):
    __tablename__ = "question"
    question_id: Mapped[int] = mapped_column(primary_key=True)
    mock_examination_id: Mapped[int] = mapped_column(ForeignKey("mock_examination.mock_examination_id"))
    question_sentence: Mapped[str]
    question_type: Mapped[QuestionType]
    answer: Mapped[str]
    created_at: Mapped[dt] = mapped_column(default=dt.now())
    updated_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    mock_examination: Mapped["MockExamination"] = relationship(back_populates="question")

    def __repr__(self) -> str:
        return f"Question(question_id={self.question_id!r}, mock_examination_id={self.mock_examination_id!r}, question_sentence={self.question_sentence!r}, question_type={self.question_type!r}, answer={self.answer!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"

