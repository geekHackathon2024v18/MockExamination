from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
from data.table.subject import Subject
from data.table.mock_examination import MockExamination
from data.table.question import Question
from data.table.mock_examinationResponse import MockExaminationResponse
from data.table.question_response import QuestionResponse
from data.table.base import Base

# テーブル作成の関数
def create_table(engine):
    Base.metadata.create_all(engine)

engine = create_engine("sqlite:///app.db", echo=True, future=True)

create_table(engine)