from enum import Enum
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime
from typing import Optional
import pytz

timezone = pytz.timezone('Europe/Belgrade')


class Base(DeclarativeBase):
    pass


class Role(str, Enum):
    ROLE_USER = 'ROLE_USER'
    ROLE_ADMIN = 'ROLE_ADMIN'


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column()
    chat_id: Mapped[int] = mapped_column()
    role: Mapped[Role] = mapped_column(default=Role.ROLE_USER)
    is_blocked: Mapped[Boolean] = mapped_column(Boolean, default=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.now(tz=timezone))
    modified_at: Mapped[Optional[datetime]] = mapped_column()

    @property
    def is_admin(self) -> bool:
        return Role.ROLE_ADMIN in self.role
