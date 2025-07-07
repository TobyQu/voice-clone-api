from typing import List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl

class CreateVoiceRequest(BaseModel):
    url: HttpUrl = Field(..., description="用于克隆的音频文件URL")
    prefix: str = Field(..., description="音色自定义前缀，仅允许数字和小写字母，小于十个字符")
    target_model: str = Field("cosyvoice-v2", description="克隆音色对应的语音合成模型版本")

class CreateVoiceResponse(BaseModel):
    voice_id: str
    request_id: str

class VoiceInfo(BaseModel):
    voice_id: str
    gmt_create: str
    gmt_modified: str
    status: str
    
class VoiceDetailInfo(VoiceInfo):
    resource_link: Optional[str] = None
    target_model: Optional[str] = None

class ListVoicesResponse(BaseModel):
    voices: List[VoiceInfo]
    
class VoiceDetailResponse(BaseModel):
    voice: VoiceDetailInfo

class UpdateVoiceRequest(BaseModel):
    url: HttpUrl = Field(..., description="用于克隆的音频文件URL")

class AudioFormat(str, Enum):
    """音频格式枚举"""
    # WAV 格式
    WAV_8000HZ_MONO_16BIT = "wav_8k"
    WAV_16000HZ_MONO_16BIT = "wav_16k"
    WAV_22050HZ_MONO_16BIT = "wav_22k"
    WAV_24000HZ_MONO_16BIT = "wav_24k"
    WAV_44100HZ_MONO_16BIT = "wav_44k"
    WAV_48000HZ_MONO_16BIT = "wav_48k"
    
    # MP3 格式
    MP3_8000HZ_MONO_128KBPS = "mp3_8k"
    MP3_16000HZ_MONO_128KBPS = "mp3_16k"
    MP3_22050HZ_MONO_256KBPS = "mp3_22k"
    MP3_24000HZ_MONO_256KBPS = "mp3_24k"
    MP3_44100HZ_MONO_256KBPS = "mp3_44k"
    MP3_48000HZ_MONO_256KBPS = "mp3_48k"
    
    # PCM 格式
    PCM_8000HZ_MONO_16BIT = "pcm_8k"
    PCM_16000HZ_MONO_16BIT = "pcm_16k"
    PCM_22050HZ_MONO_16BIT = "pcm_22k"
    PCM_24000HZ_MONO_16BIT = "pcm_24k"
    PCM_44100HZ_MONO_16BIT = "pcm_44k"
    PCM_48000HZ_MONO_16BIT = "pcm_48k"

class SynthesizeSpeechRequest(BaseModel):
    """语音合成请求模型"""
    voice_id: str = Field(..., description="指定用于语音合成的音色ID")
    text: Union[str, List[str]] = Field(..., description="要转换为语音的文本，可以是单个字符串或字符串数组")
    model: str = Field(..., description="用于语音合成的模型")
    
    # 以下是可选参数
    format: Optional[AudioFormat] = Field(None, description="指定音频编码格式及采样率")
    volume: Optional[int] = Field(50, description="合成音频的音量，取值范围：0~100", ge=0, le=100)
    speech_rate: Optional[float] = Field(1.0, description="合成音频的语速，取值范围：0.5~2", ge=0.5, le=2.0)
    pitch_rate: Optional[float] = Field(1.0, description="合成音频的语调，取值范围：0.5~2", ge=0.5, le=2.0) 