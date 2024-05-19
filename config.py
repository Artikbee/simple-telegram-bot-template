from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    TOKEN: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            TOKEN=env('BOT_TOKEN'),
        ),
    )
