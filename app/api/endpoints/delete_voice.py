from fastapi import APIRouter, Depends, HTTPException, status
from dashscope.audio.tts_v2 import VoiceEnrollmentException

from app.services.voice_service import VoiceCloneService
from app.utils.response import success_response
from app.core.exceptions import handle_dashscope_exception

router = APIRouter()

def get_voice_service() -> VoiceCloneService:
    return VoiceCloneService()

@router.delete("/voices/{voice_id}")
async def delete_voice(
    voice_id: str,
    service: VoiceCloneService = Depends(get_voice_service)
):
    """删除声音"""
    try:
        request_id = service.delete_voice(voice_id=voice_id)
        return success_response(
            data={"request_id": request_id},
            message="声音删除成功"
        )
    except VoiceEnrollmentException as e:
        raise handle_dashscope_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"删除声音失败: {str(e)}"
        ) 