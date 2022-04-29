from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create database session
Session = sessionmaker()
Session.configure(bind=engine, autoflush=True, expire_on_commit=False)
session = Session()
session.commit()


