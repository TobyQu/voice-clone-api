from app.services.voice_service import VoiceCloneService

def get_voice_service() -> VoiceCloneService:
    """获取声音克隆服务的依赖函数
    
    用于所有需要声音克隆服务的API端点
    """
    return VoiceCloneService() 