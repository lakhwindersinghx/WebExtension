from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.db_models import Base  # Ensure this imports your SQLAlchemy models

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:1721261212Ff!@localhost:5432/webactivity"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Automatically create tables
Base.metadata.create_all(bind=engine)
