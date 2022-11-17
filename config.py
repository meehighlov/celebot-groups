import dotenv

from pydantic import BaseSettings


dotenv.load_dotenv()


class Config(BaseSettings):
    BOTTOKEN_CELEBOT: str  # noqa
    ADMINCODE: str
    CLUBCODE: str


config = Config()
