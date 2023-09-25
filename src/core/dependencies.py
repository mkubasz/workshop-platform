from functools import cache
from src.core.config import ApiConfig


@cache
def get_api_config() -> ApiConfig:
    return ApiConfig()
