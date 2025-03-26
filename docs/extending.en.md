# Extension Guide

The Voice Clone API is designed with an extensible architecture, allowing integration with various voice service providers. This document will guide you on how to add a new service provider.

## Architecture Overview

The project uses an abstract base class (`VoiceProviderBase`) to define the interface for voice service providers and a factory pattern to create concrete service provider instances. This design makes it simple to add new service providers without modifying the existing API endpoint code.

## Adding a New Service Provider

### 1. Create a New Provider Class

Create a new file in the `app/services/providers/` directory, e.g., `my_provider.py`, and implement the `VoiceProviderBase` interface:

```python
from typing import Dict, List, Any, Optional, Tuple, Union, ByteString
from app.services.providers.base import VoiceProviderBase

class MyProvider(VoiceProviderBase):
    """Custom voice service provider"""
    
    def __init__(self):
        # Initialization logic, e.g., setting API key, creating client
        self.api_key = "your_api_key"
        self.client = YourServiceClient(self.api_key)
    
    def create_voice(self, url: str, prefix: str, target_model: str) -> Dict[str, str]:
        """Create a cloned voice"""
        # Implement voice creation logic
        voice_id = self.client.create_voice(url, prefix, target_model)
        return {
            "voice_id": voice_id,
            "request_id": "your-request-id"
        }
        
    def list_voices(self, prefix: Optional[str] = None, page_index: int = 0, page_size: int = 10) -> List[Dict[str, Any]]:
        """Get voice list"""
        # Implement logic to get voice list
        return self.client.list_voices(prefix, page_index, page_size)
        
    def query_voice(self, voice_id: str) -> Dict[str, Any]:
        """Get voice details"""
        # Implement logic to get voice details
        return self.client.get_voice(voice_id)
        
    def update_voice(self, voice_id: str, url: str) -> str:
        """Update voice"""
        # Implement voice update logic
        self.client.update_voice(voice_id, url)
        return "your-request-id"
        
    def delete_voice(self, voice_id: str) -> str:
        """Delete voice"""
        # Implement voice deletion logic
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
        """Speech synthesis using a cloned voice"""
        # Implement speech synthesis logic
        if isinstance(text, list):
            # Handle text array
            combined_audio = bytearray()
            for text_item in text:
                audio = self.client.synthesize(voice_id, text_item, model, format, volume, speech_rate, pitch_rate)
                combined_audio.extend(audio)
            return bytes(combined_audio), "your-request-id"
        else:
            # Handle single text string
            audio = self.client.synthesize(voice_id, text, model, format, volume, speech_rate, pitch_rate)
            return audio, "your-request-id"
        
    @property
    def provider_name(self) -> str:
        """Get provider name"""
        return "MyProvider"
```

### 2. Update the Factory Function

Modify the `app/services/factory.py` file to add support for the new provider:

```python
from app.core.config import settings
from app.services.providers.base import VoiceProviderBase
from app.services.providers.dashscope_provider import DashScopeProvider
from app.services.providers.my_provider import MyProvider  # Import the new provider class

def get_voice_provider() -> VoiceProviderBase:
    """Get voice service provider instance"""
    provider_name = settings.VOICE_PROVIDER.lower()
    
    if provider_name == "dashscope":
        return DashScopeProvider()
    elif provider_name == "myprovider":  # Add new provider option
        return MyProvider()
    
    # Default to DashScope
    return DashScopeProvider()
```

### 3. Add Configuration Options

Update the `.env.example` file to add descriptions for the new provider: 