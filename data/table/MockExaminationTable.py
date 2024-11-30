from datetime import datetime as dt

# どんな模擬試験かの情報を持つテーブル
class MockExaminationTable:
    def __init__(self,
        subject_id: int,
        mock_examination_name: str,
        time_limit: int,
        mock_examination_id: int = None
    ):
        self.mock_examination_id = None
        self.subject_id = subject_id
        self.mock_examination_name = mock_examination_name
        self.time_limit = time_limit
        self.created_at = dt.now()
        self.updated_at = dt.now()
