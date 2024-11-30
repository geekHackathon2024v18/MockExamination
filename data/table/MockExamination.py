from datetime import datetime as dt

from TableInterface import TableInterface


# どんな模擬試験かの情報を持つテーブル
class MockExamination(TableInterface):
    def __init__(self,
        subject_id: int,
        mock_examination_name: str,
        time_limit: int,
        mock_examination_id: int = None,
        updated_at: dt = dt.now(),
        created_at: dt = dt.now()
    ):
        self.mock_examination_id = None
        self.subject_id = subject_id
        self.mock_examination_name = mock_examination_name
        self.time_limit = time_limit
        self.created_at = created_at
        self.updated_at = updated_at

    def getDictData(self) -> dict:
        return {
            "mock_examination_id": self.mock_examination_id,
            "subject_id": self.subject_id,
            "mock_examination_name": self.mock_examination_name,
            "time_limit": self.time_limit,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

if __name__ == "__main__":
    print(MockExamination(subject_id=1, mock_examination_name="test", time_limit=60).getDictData())