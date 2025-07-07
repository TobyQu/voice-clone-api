from fastapi import HTTPException, status
from dashscope.audio.tts_v2 import VoiceEnrollmentException

class VoiceAPIException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

def handle_dashscope_exception(e: VoiceEnrollmentException) -> VoiceAPIException:
    """处理 DashScope API 异常并转换为 HTTP 异常"""
    return VoiceAPIException(
        status_code=e._status_code if e._status_code < 600 else status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Error: {e._code} - {e._error_message}"
    ) 