from datetime import datetime as dt

# 科目の情報を持つテーブル
class SubjectTable:
    def __init__(self,
        subject_name: str,
        subject_id: int = None
    ):
        self.subject_id = None
        self.subject_name = subject_name
        self.created_at = dt.now()
        self.updated_at = dt.now()