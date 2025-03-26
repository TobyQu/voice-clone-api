from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from dashscope.audio.tts_v2 import VoiceEnrollmentException

from app.models.voice import ListVoicesResponse, VoiceInfo
from app.services.voice_service import VoiceCloneService
from app.core.exceptions import handle_dashscope_exception

router = APIRouter()

def get_voice_service() -> VoiceCloneService:
    return VoiceCloneService()

@router.get("/voices", response_model=ListVoicesResponse)
async def list_voices(
    prefix: Optional[str] = None,
    page_index: int = Query(0, ge=0),
    page_size: int = Query(10, ge=1, le=100),
    service: VoiceCloneService = Depends(get_voice_service)
):
    """获取声音列表"""
    try:
        voices = service.list_voices(
            prefix=prefix,
            page_index=page_index,
            page_size=page_size
        )
        return ListVoicesResponse(
            voices=[VoiceInfo(**voice) for voice in voices]
        )
    except VoiceEnrollmentException as e:
        raise handle_dashscope_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"获取声音列表失败: {str(e)}"
        ) 