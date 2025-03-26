from typing import Any, Dict, Optional

def success_response(data: Any = None, message: str = "操作成功") -> Dict[str, Any]:
    """标准化成功响应格式"""
    response = {
        "success": True,
        "message": message
    }
    
    if data is not None:
        response["data"] = data
        
    return response

def error_response(message: str, error_code: Optional[str] = None) -> Dict[str, Any]:
    """标准化错误响应格式"""
    response = {
        "success": False,
        "message": message
    }
    
    if error_code:
        response["error_code"] = error_code
        
    return response 