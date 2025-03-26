from fastapi import APIRouter
from app.api.endpoints import (
    create_voice, 
    list_voices,
    get_voice,
    update_voice, 
    delete_voice, 
    synthesize_speech
)

router = APIRouter()

# 注册各个独立端点
router.include_router(create_voice.router, tags=["voices"])
router.include_router(list_voices.router, tags=["voices"])
router.include_router(get_voice.router, tags=["voices"])
router.include_router(update_voice.router, tags=["voices"])
router.include_router(delete_voice.router, tags=["voices"])
router.include_router(synthesize_speech.router, tags=["voices"]) 