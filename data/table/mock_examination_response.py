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



# 模擬試験の回答情報を持つテーブル
class MockExaminationResponse(Base):
    __tablename__ = "mock_examination_response"
    mock_examination_response_id: Mapped[int] = mapped_column(primary_key=True)
    mock_examination_id: Mapped[int] = mapped_column(ForeignKey("mock_examination.mock_examination_id"))
    interruption: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[dt] = mapped_column(default=dt.now())
    updated_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    # question_responses: Mapped[List["QuestionResponse"]] = relationship("QuestionResponse", back_populates="mock_examination_responses", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"MockExaminationResponse(mock_examination_id={self.mock_examination_id!r}, interruption={self.interruption!r}, mock_examination_response_id={self.mock_examination_response_id!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
