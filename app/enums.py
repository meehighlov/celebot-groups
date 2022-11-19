from enum import Enum


class StaticMessages(str, Enum):
    HELLO_MESSAGE = "Hi, i'm celebot 🤗\nGot access code? Type /code to pass it!"


class CommandCodeStates(str, Enum):
    CHECK = 1


class CommandSetmeStates(str, Enum):
    SET = 1
