from enum import Enum
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime
from typing import Annotated
import pytz

timezone = pytz.timezone('Europe/Belgrade')
intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now(timezone), nullable=False)]
update_at = Annotated[datetime, mapped_column(
    server_default=func.now(timezone),
    nullable=False,
    onupdate=func.now(timezone),
)]

str_256 = Annotated[str, '256']


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
    }


class Role(Enum):
    ROLE_USER = 'ROLE_USER'
    ROLE_ADMIN = 'ROLE_ADMIN'


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    telegram_id: Mapped[int]
    chat_id: Mapped[int]
    role: Mapped[Role] = mapped_column(default=Role.ROLE_USER)
    is_blocked: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]

    @property
    def is_admin(self) -> bool:
        return Role.ROLE_ADMIN in self.role


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[intpk]
    title: Mapped[str_256]
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]


class Product(Base):
    __tablename__ = "products"
    id: Mapped[intpk]
    title: Mapped[str_256]
    description: Mapped[str_256]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]
