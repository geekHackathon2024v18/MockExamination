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
from ..database.sql_alchemy_control import Base


# 科目の情報を持つテーブル
class Subject(Base):
    __tablename__ = "subject"
    subject_id: Mapped[int] = mapped_column(primary_key=True)
    subject_name: Mapped[str]
    created_at: Mapped[dt] = mapped_column(default=dt.now())
    updated_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    def __repr__(self) -> str:
        return f"Subject(subject_id={self.subject_id!r}, subject_name={self.subject_name!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
