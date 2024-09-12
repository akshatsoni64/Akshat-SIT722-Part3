from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://admin:RigJDPQFJ6bxMrChWSgiyLuD33G6MowL@dpg-crha09l6l47c73c4sjdg-a.singapore-postgres.render.com/task72p_59hk" # os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
