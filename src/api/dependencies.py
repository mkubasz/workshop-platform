from functools import cache
from config import ApiConfig

@cache
def get_api_config() -> ApiConfig:
    return ApiConfig()
