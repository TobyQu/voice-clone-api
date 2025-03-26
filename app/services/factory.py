from app.core.config import settings
from app.services.providers.base import VoiceProviderBase
from app.services.providers.dashscope_provider import DashScopeProvider

def get_voice_provider() -> VoiceProviderBase:
    """获取声音服务提供者实例
    
    根据配置决定使用哪个服务提供者，默认使用 DashScope
    """
    provider_name = settings.VOICE_PROVIDER.lower()
    
    if provider_name == "dashscope":
        return DashScopeProvider()
    
    # 未来可以在这里添加更多的提供者
    # elif provider_name == "other_provider":
    #     return OtherProvider()
    
    # 默认使用 DashScope
    return DashScopeProvider() 