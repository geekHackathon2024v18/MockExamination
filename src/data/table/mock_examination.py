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





# どんな模擬試験かの情報を持つテーブル
class MockExamination(Base):
    __tablename__ = "mock_examination"
    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"))
    mock_examination_name: Mapped[str]
    time_limit: Mapped[Optional[int]]
    updated_at: Mapped[dt] = mapped_column(default=dt.now())
    created_at: Mapped[dt] = mapped_column(default=dt.now(), onupdate=dt.now())

    def __repr__(self) -> str:
        return f"MockExamination(subject_id={self.subject_id!r}, mock_examination_name={self.mock_examination_name!r}, time_limit={self.time_limit!r}, mock_examination_id={self.id!r}, updated_at={self.updated_at!r}, created_at={self.created_at!r})"
