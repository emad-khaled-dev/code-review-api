from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Code Review Assistant API"
    version: str = "1.0.0"
    groq_api_key: str = ""
    max_code_length: int = 5000
    
    class Config:
        env_file = ".env"

settings = Settings()