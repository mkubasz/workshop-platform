from pydantic_settings import BaseSettings, SettingsConfigDict

class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    project_name: str = "workshop-platform"
    version: str = "dev"
    debug: bool = False

    allowed_hosts: tuple[str] = ("*",)

class TestApiConfig(ApiConfig):
    project_name: str = "test-workshop-platform"
    version: str = "test"
    debug: bool = True
