from datetime import datetime as dt

# 科目の情報を持つテーブル
class Subject:
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