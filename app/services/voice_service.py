import os
import dashscope
from typing import List, Dict, Any, Optional, Tuple, ByteString, Union
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer
from app.services.factory import get_voice_provider
from app.services.providers.base import VoiceProviderBase

from app.core.config import settings

# 设置 API Key
dashscope.api_key = settings.DASHSCOPE_API_KEY

class VoiceCloneService:
    """声音克隆服务
    
    统一的服务接口，内部使用不同的服务提供者实现
    """
    
    def __init__(self, provider: Optional[VoiceProviderBase] = None):
        """初始化声音克隆服务
        
        Args:
            provider: 服务提供者实例，如果未提供则使用工厂创建默认提供者
        """
        self.provider = provider or get_voice_provider()
        
    def create_voice(self, url: str, prefix: str, target_model: str) -> Dict[str, str]:
        """创建克隆音色"""
        return self.provider.create_voice(url, prefix, target_model)
        
    def list_voices(self, prefix: Optional[str] = None, page_index: int = 0, page_size: int = 10) -> List[Dict[str, Any]]:
        """获取声音列表"""
        return self.provider.list_voices(prefix, page_index, page_size)
        
    def query_voice(self, voice_id: str) -> Dict[str, Any]:
        """获取指定声音详情"""
        return self.provider.query_voice(voice_id)
        
    def update_voice(self, voice_id: str, url: str) -> str:
        """更新声音"""
        return self.provider.update_voice(voice_id, url)
        
    def delete_voice(self, voice_id: str) -> str:
        """删除声音"""
        return self.provider.delete_voice(voice_id)
        
    def synthesize_speech(
        self, 
        voice_id: str, 
        text: Union[str, List[str]], 
        model: str,
        format: Optional[str] = None,
        volume: Optional[int] = 50,
        speech_rate: Optional[float] = 1.0,
        pitch_rate: Optional[float] = 1.0
    ) -> Tuple[ByteString, str]:
        """使用克隆的声音进行语音合成"""
        return self.provider.synthesize_speech(
            voice_id=voice_id,
            text=text, 
            model=model,
            format=format,
            volume=volume,
            speech_rate=speech_rate,
            pitch_rate=pitch_rate
        )
        
    @property
    def provider_name(self) -> str:
        """获取当前使用的服务提供者名称"""
        return self.provider.provider_name 