from fastapi import APIRouter, Depends, HTTPException, status
from dashscope.audio.tts_v2 import VoiceEnrollmentException

from app.models.voice import VoiceDetailResponse, VoiceDetailInfo
from app.services.voice_service import VoiceCloneService
from app.core.exceptions import handle_dashscope_exception

router = APIRouter()

def get_voice_service() -> VoiceCloneService:
    return VoiceCloneService()

@router.get("/voices/{voice_id}", response_model=VoiceDetailResponse)
async def get_voice(
    voice_id: str,
    service: VoiceCloneService = Depends(get_voice_service)
):
    """获取指定声音详情"""
    try:
        voice = service.query_voice(voice_id=voice_id)
        return VoiceDetailResponse(voice=VoiceDetailInfo(**voice))
    except VoiceEnrollmentException as e:
        raise handle_dashscope_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"获取声音详情失败: {str(e)}"
        ) 