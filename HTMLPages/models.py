from core import DATABASE_URL
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine


engine=create_engine(DATABASE_URL,echo=True)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)



Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
