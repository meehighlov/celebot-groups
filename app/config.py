import dotenv
import os.path

from pydantic import BaseSettings, Field, validator


dotenv.load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = Field('celebotgroups', const=True)
    CONVERSATION_TIMEOUT: float = Field(60.0, const=True)

    BOTTOKEN_CELEBOT: str  # noqa
    ADMINCODE: str
    CLUBCODE: str
    LOG_FILE: str
    MY_CHAT_ID: int

    @validator('LOG_FILE')
    def check_logfile_if_exists(cls, value):
        if not os.path.isfile(value):
            raise ValueError(f'Logfile {value!r} does not exists')
        return value

config = Config()
