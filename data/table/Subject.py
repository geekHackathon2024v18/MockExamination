from datetime import datetime as dt
from TableInterface import TableInterface

# 科目の情報を持つテーブル
class Subject(TableInterface):
    def __init__(self,
        subject_name: str,
        subject_id: int = None,
        created_at: dt = dt.now(),
        updated_at: dt = dt.now()
    ):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.created_at = created_at
        self.updated_at = updated_at
    def getDictData(self) -> dict:
        return {
            "subject_id": self.subject_id,
            "subject_name": self.subject_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }