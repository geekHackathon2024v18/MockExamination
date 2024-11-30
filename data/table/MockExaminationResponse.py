from datetime import datetime as dt
import TableInterface

# 模擬試験の回答情報を持つテーブル
class MockExaminationResponse(TableInterface):
    def __init__(self,
        mock_examination_id: int,
        interruption: bool,
        mock_examination_response_id: int = None,
        created_at: dt = dt.now(),
        updated_at: dt = dt.now()
    ):
        self.mock_examination_id = mock_examination_id
        self.interruption = interruption
        self.mock_examination_response_id = mock_examination_response_id
        self.created_at = created_at
        self.updated_at = updated_at
    def getDictData(self) -> dict:
        return {
            "mock_examination_id": self.mock_examination_id,
            "interruption": self.interruption,
            "mock_examination_response_id": self.mock_examination_response_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
