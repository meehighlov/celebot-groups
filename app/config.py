import dotenv

from pydantic import BaseSettings, Field


dotenv.load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = Field('celebotgroups', const=True)
    BOTTOKEN_CELEBOT: str  # noqa
    ADMINCODE: str
    CLUBCODE: str
    CONVERSATION_TIMEOUT: float = 60.0


config = Config()
