from models.db_models import Base
from db import engine

def init_pg_db():
    Base.metadata.create_all(bind=engine)
init_pg_db() 