from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple, Union, ByteString

class VoiceProviderBase(ABC):
    """声音服务提供者基类"""
    
    @abstractmethod
    def create_voice(self, url: str, prefix: str, target_model: str) -> Dict[str, str]:
        """创建克隆音色"""
        pass
        
    @abstractmethod
    def list_voices(self, prefix: Optional[str] = None, page_index: int = 0, page_size: int = 10) -> List[Dict[str, Any]]:
        """获取声音列表"""
        pass
        
    @abstractmethod
    def query_voice(self, voice_id: str) -> Dict[str, Any]:
        """获取指定声音详情"""
        pass
        
    @abstractmethod
    def update_voice(self, voice_id: str, url: str) -> str:
        """更新声音"""
        pass
        
    @abstractmethod
    def delete_voice(self, voice_id: str) -> str:
        """删除声音"""
        pass
        
    @abstractmethod
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
        """使用克隆的声音进行语音合成
        
        Args:
            voice_id: 声音ID
            text: 要转换为语音的文本，可以是单个字符串或字符串数组
            model: 语音合成模型
            format: 音频格式和采样率
            volume: 音量 (0-100)
            speech_rate: 语速 (0.5-2.0)
            pitch_rate: 语调 (0.5-2.0)
            
        Returns:
            包含合成音频数据和请求ID的元组
        """
        pass
        
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """获取提供者名称"""
        pass 