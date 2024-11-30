from datetime import datetime as dt

class QuestionResponseTable:
    def __init__(self,
        mock_examination_id: int,
        mock_examination_response_id: int,
        question_id: int,
        response_content: str,
        correction: bool,
        created_at: dt = dt.now(),
        updated_at: dt = dt.now()
    ):
        self.mock_examination_id = mock_examination_id
        self.mock_examination_response_id = mock_examination_response_id
        self.question_id = question_id
        self.response_content = response_content
        self.correction = correction
        self.created_at = created_at
        self.updated_at = updated_at
