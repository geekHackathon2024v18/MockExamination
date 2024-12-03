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


class QuestionResponse(Base):
    __tablename__ = "question_response"
    mock_examination_id: Mapped[int] = mapped_column(ForeignKey("mock_examination.mock_examination_id"), primary_key=True)
    mock_examination_response_id: Mapped[int] = mapped_column(ForeignKey("mock_examination_response.mock_examination_response_id"), primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.question_id"), primary_key=True)
    response_content: Mapped[str]
    correction: Mapped[bool]
    created_at: Mapped[dt] = mapped_column(default=dt.now())
    updated_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    question_response: Mapped["MockExaminationResponse"] = relationship("QuestionResponse", back_populates="question_response")

    def __repr__(self) -> str:
        return f"QuestionResponse(mock_examination_id={self.mock_examination_id!r}, mock_examination_response_id={self.mock_examination_response_id!r}, question_id={self.question_id!r}, response_content={self.response_content!r}, correction={self.correction!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
