"""
DashScope 声音服务提供者实现

基于阿里云语音合成服务，详细文档：
https://help.aliyun.com/zh/model-studio/developer-reference/speech-synthesis-and-speech-recognition/
"""

import dashscope
from typing import Dict, List, Any, Optional, Tuple, Union, ByteString
from dashscope.audio.tts_v2 import VoiceEnrollmentService, SpeechSynthesizer, AudioFormat

from app.core.config import settings
from app.services.providers.base import VoiceProviderBase

class DashScopeProvider(VoiceProviderBase):
    """DashScope 声音服务提供者
    
    使用阿里云 DashScope 平台的语音合成服务
    官方文档: https://help.aliyun.com/zh/model-studio/developer-reference/cosyvoice
    """
    
    def __init__(self):
        # 设置 API Key
        dashscope.api_key = settings.DASHSCOPE_API_KEY
        self.service = VoiceEnrollmentService()
    
    def create_voice(self, url: str, prefix: str, target_model: str) -> Dict[str, str]:
        """创建克隆音色"""
        voice_id = self.service.create_voice(
            target_model=target_model,
            prefix=prefix,
            url=url
        )
        
        return {
            "voice_id": voice_id,
            "request_id": self.service.get_last_request_id()
        }
        
    def list_voices(self, prefix: Optional[str] = None, page_index: int = 0, page_size: int = 10) -> List[Dict[str, Any]]:
        """获取声音列表"""
        return self.service.list_voices(
            prefix=prefix,
            page_index=page_index,
            page_size=page_size
        )
        
    def query_voice(self, voice_id: str) -> Dict[str, Any]:
        """获取指定声音详情"""
        return self.service.query_voices(voice_id=voice_id)
        
    def update_voice(self, voice_id: str, url: str) -> str:
        """更新声音"""
        self.service.update_voice(voice_id=voice_id, url=url)
        return self.service.get_last_request_id()
        
    def delete_voice(self, voice_id: str) -> str:
        """删除声音"""
        self.service.delete_voice(voice_id=voice_id)
        return self.service.get_last_request_id()
        
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
        # 创建合成器配置参数
        synth_params = {
            "model": model,
            "voice": voice_id,
            "volume": volume,
            "speech_rate": speech_rate,
            "pitch_rate": pitch_rate
        }
        
        # 如果指定了格式，添加到参数中
        if format:
            # 将我们的格式转换为 DashScope 的格式
            dash_format = getattr(AudioFormat, format.upper(), None)
            if dash_format:
                synth_params["format"] = dash_format
        
        # 创建合成器
        synthesizer = SpeechSynthesizer(**synth_params)
        
        # 处理文本输入
        if isinstance(text, list):
            # 如果是文本数组，合并所有结果
            combined_audio = bytearray()
            request_id = None
            
            for text_item in text:
                audio = synthesizer.call(text_item)
                combined_audio.extend(audio)
                # 保存最后一个请求ID
                request_id = synthesizer.get_last_request_id()
                
            return bytes(combined_audio), request_id
        else:
            # 单个文本字符串
            audio = synthesizer.call(text)
            return audio, synthesizer.get_last_request_id()
        
    @property
    def provider_name(self) -> str:
        """获取提供者名称"""
        return "DashScope" 