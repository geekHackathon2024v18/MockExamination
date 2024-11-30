from datetime import datetime as dt

# 模擬試験の回答情報を持つテーブル
class MockExaminationResponse:
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
