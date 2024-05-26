from typing import Sequence

from sqlalchemy import select, update
from database.models.models import User, Role
from sqlalchemy.ext.asyncio import AsyncSession


class UserDAL:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, telegram_id: int, chat_id: int) -> None:
        new_user = User(telegram_id=telegram_id, chat_id=chat_id)
        self.session.add(new_user)
        await self.session.commit()

    async def update_user(self, chat_id: int, **kwargs) -> None:
        query = (
            update(User).
            where(User.chat_id == chat_id).
            values(kwargs)
        )
        await self.session.execute(query)
        await self.session.commit()

    async def get_user_by_chat_id(self, chat_id: int) -> User | None:
        query = select(User).where(User.chat_id == chat_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_users_not_recorded(self) -> Sequence[User]:
        query = (select(User).
                 where(User.is_recorded == 0, User.role == Role.ROLE_USER, User.is_blocked == 0))
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_user_admin(self) -> User | None:
        query = select(User).where(User.role == Role.ROLE_ADMIN)
        result = await self.session.execute(query)
        return result.scalars().first()
