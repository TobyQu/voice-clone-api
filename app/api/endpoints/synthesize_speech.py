from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from io import BytesIO
from dashscope.audio.tts_v2 import VoiceEnrollmentException

from app.models.voice import SynthesizeSpeechRequest
from app.core.exceptions import handle_dashscope_exception
from app.api.dependencies import get_voice_service

router = APIRouter()

@router.post("/synthesize")
async def synthesize_speech(
    request: SynthesizeSpeechRequest,
    service = Depends(get_voice_service)
):
    """语音合成
    
    将文本转换为语音，可以是单个文本或文本数组。
    支持多种格式、音量、语速和语调的配置。
    """
    try:
        # 提取请求参数
        audio, request_id = service.synthesize_speech(
            voice_id=request.voice_id,
            text=request.text,
            model=request.model,
            format=request.format.value if request.format else None,
            volume=request.volume,
            speech_rate=request.speech_rate,
            pitch_rate=request.pitch_rate
        )
        
        # 创建一个内存文件对象来存储音频数据
        audio_stream = BytesIO(audio)
        
        # 确定正确的媒体类型
        media_type = "audio/mp3"  # 默认
        if request.format:
            if request.format.value.startswith("wav"):
                media_type = "audio/wav"
            elif request.format.value.startswith("pcm"):
                media_type = "audio/pcm"
        
        # 返回流式响应
        return StreamingResponse(
            audio_stream, 
            media_type=media_type,
            headers={"X-Request-ID": request_id}
        )
    except VoiceEnrollmentException as e:
        raise handle_dashscope_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"语音合成失败: {str(e)}"
        ) 