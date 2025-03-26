from fastapi import APIRouter, Depends, HTTPException, status
from dashscope.audio.tts_v2 import VoiceEnrollmentException

from app.models.voice import CreateVoiceRequest, CreateVoiceResponse
from app.services.voice_service import VoiceCloneService
from app.core.exceptions import handle_dashscope_exception

router = APIRouter()

def get_voice_service() -> VoiceCloneService:
    return VoiceCloneService()

@router.post("/voices", response_model=CreateVoiceResponse, status_code=status.HTTP_201_CREATED)
async def create_voice(
    request: CreateVoiceRequest,
    service: VoiceCloneService = Depends(get_voice_service)
):
    """创建声音克隆"""
    try:
        result = service.create_voice(
            url=str(request.url),
            prefix=request.prefix,
            target_model=request.target_model
        )
        return CreateVoiceResponse(
            voice_id=result["voice_id"],
            request_id=result["request_id"]
        )
    except VoiceEnrollmentException as e:
        raise handle_dashscope_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"创建声音克隆失败: {str(e)}"
        ) 