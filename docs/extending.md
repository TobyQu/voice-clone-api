# 扩展指南

声音复刻 API 设计为可扩展架构，允许集成多种声音服务提供者。本文档将指导您如何添加新的服务提供者。

## 架构概览

项目使用抽象基类 (`VoiceProviderBase`) 定义了声音服务提供者的接口，并使用工厂模式创建具体的服务提供者实例。这种设计使得添加新的服务提供者非常简单，无需修改现有的 API 端点代码。

## 添加新的服务提供者

### 1. 创建新的提供者类

在 `app/services/providers/` 目录中创建一个新文件，例如 `my_provider.py`，并实现 `VoiceProviderBase` 接口：

```python
from typing import Dict, List, Any, Optional, Tuple, Union, ByteString
from app.services.providers.base import VoiceProviderBase

class MyProvider(VoiceProviderBase):
    """自定义声音服务提供者"""
    
    def __init__(self):
        # 初始化逻辑，例如设置API密钥、创建客户端等
        self.api_key = "your_api_key"
        self.client = YourServiceClient(self.api_key)
    
    def create_voice(self, url: str, prefix: str, target_model: str) -> Dict[str, str]:
        """创建克隆音色"""
        # 实现创建声音的逻辑
        voice_id = self.client.create_voice(url, prefix, target_model)
        return {
            "voice_id": voice_id,
            "request_id": "your-request-id"
        }
        
    def list_voices(self, prefix: Optional[str] = None, page_index: int = 0, page_size: int = 10) -> List[Dict[str, Any]]:
        """获取声音列表"""
        # 实现获取声音列表的逻辑
        return self.client.list_voices(prefix, page_index, page_size)
        
    def query_voice(self, voice_id: str) -> Dict[str, Any]:
        """获取指定声音详情"""
        # 实现获取声音详情的逻辑
        return self.client.get_voice(voice_id)
        
    def update_voice(self, voice_id: str, url: str) -> str:
        """更新声音"""
        # 实现更新声音的逻辑
        self.client.update_voice(voice_id, url)
        return "your-request-id"
        
    def delete_voice(self, voice_id: str) -> str:
        """删除声音"""
        # 实现删除声音的逻辑
        self.client.delete_voice(voice_id)
        return "your-request-id"
        
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
        # 实现语音合成的逻辑
        if isinstance(text, list):
            # 处理文本数组
            combined_audio = bytearray()
            for text_item in text:
                audio = self.client.synthesize(voice_id, text_item, model, format, volume, speech_rate, pitch_rate)
                combined_audio.extend(audio)
            return bytes(combined_audio), "your-request-id"
        else:
            # 处理单个文本
            audio = self.client.synthesize(voice_id, text, model, format, volume, speech_rate, pitch_rate)
            return audio, "your-request-id"
        
    @property
    def provider_name(self) -> str:
        """获取提供者名称"""
        return "MyProvider"
```

### 2. 更新工厂函数

修改 `app/services/factory.py` 文件，添加对新提供者的支持：

```python
from app.core.config import settings
from app.services.providers.base import VoiceProviderBase
from app.services.providers.dashscope_provider import DashScopeProvider
from app.services.providers.my_provider import MyProvider  # 导入新的提供者类

def get_voice_provider() -> VoiceProviderBase:
    """获取声音服务提供者实例"""
    provider_name = settings.VOICE_PROVIDER.lower()
    
    if provider_name == "dashscope":
        return DashScopeProvider()
    elif provider_name == "myprovider":  # 添加新的提供者选项
        return MyProvider()
    
    # 默认使用 DashScope
    return DashScopeProvider()
```

### 3. 添加配置选项

更新 `.env.example` 文件，添加对新提供者的说明： 