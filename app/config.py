import dotenv

from pydantic import BaseSettings, Field


dotenv.load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = Field('celebotgroups', const=True)
    CONVERSATION_TIMEOUT: float = Field(60.0, const=True)

    BOTTOKEN_CELEBOT: str  # noqa
    ADMINCODE: str
    CLUBCODE: str
    LOG_FILE: str
    MY_CHAT_ID: int


config = Config()
