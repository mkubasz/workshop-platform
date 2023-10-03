from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.core.dependencies import get_api_config

config = get_api_config()
url_postgresql = URL.create(
    drivername="postgresql",
    username=config.DATABASE_USERNAME,
    password=config.DATABASE_PASSWORD,
    host=config.DATABASE_HOST,
    port=5432,
    database=config.DATABASE_NAME
)
engine = create_engine(
     url_postgresql
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_db():
    Base.metadata.create_all(bind=engine)


async def connection():
    async with Session() as session:
        yield session
