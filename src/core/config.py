from pydantic_settings import BaseSettings, SettingsConfigDict

class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    project_name: str = "workshop-platform"
    version: str = "dev"
    debug: bool = False
    DATABASE_HOST: str = ""
    DATABASE_NAME: str = ""
    DATABASE_USERNAME: str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_PORT: int = 5432

    allowed_hosts: tuple[str] = ("*",)

class TestApiConfig(ApiConfig):
    project_name: str = "test-workshop-platform"
    version: str = "test"
    debug: bool = True
