from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.database.models.models import Base

engine = create_async_engine(
    url="sqlite+aiosqlite:///example.db",
    echo=True,
    future=True
)

async_session_local = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


def get_session() -> async_sessionmaker:
    return async_session_local()


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
