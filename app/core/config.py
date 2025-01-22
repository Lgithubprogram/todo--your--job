from pydantic_settings import BaseSettings
from typing import List, Dict
from dotenv import load_dotenv
load_dotenv()  # 这会确保从 .env 文件加载环境变量


class Settings(BaseSettings):
    API_VERSION: str = "1.0.0"
    CONTACT: Dict[str, str] = {
        "name": "TODOJOB FastAPI Demo",
        "url": "https://github.com/Lgithubprogram?tab=repositories",
        "email": "2080994407@qq.com",
    }
    ENV: str = "dev"
    RELOAD: bool = True if ENV == "dev" else False
    LOG_LEVEL: str = "debug" if ENV == "dev" else "info"
    ALLOWED_HOSTS: List[str] = ["*"]

    # Database settings
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"  # Make sure this points to your .env file
        extra = "ignore"


settings = Settings()
