import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Settings:
    API_V1_PREFIX = "/api/v1"
    PROJECT_NAME = "Voice Clone API"
    
    # API Key
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    
    # 默认声音合成模型
    DEFAULT_TTS_MODEL = "cosyvoice-v1"
    
    # 声音服务提供者，默认使用 DashScope
    VOICE_PROVIDER = os.getenv("VOICE_PROVIDER", "dashscope")

settings = Settings() 