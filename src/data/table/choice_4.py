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
from src.data.table.base import Base


class Choice4(Base):
    __tablename__ = "choice_4"
    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    choice_1: Mapped[str]
    choice_2: Mapped[str]
    choice_3: Mapped[str]
    choice_4: Mapped[str]
    created_at: Mapped[dt] = mapped_column(default=dt.now())
    updated_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    def __repr__(self) -> str:
        return f"Choice4(choice_4_id={self.id!r}, question_id={self.question_id!r}, choice_1={self.choice_1!r}, choice_2={self.choice_2!r}, choice_3={self.choice_3!r}, choice_4={self.choice_4!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"