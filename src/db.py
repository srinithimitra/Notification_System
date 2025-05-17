from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
import sqlalchemy
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./notification.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

# Database model
class Notifications(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True, nullable=False)
    message = Column(String, nullable=False)
    delivered = Column(Boolean, default=False)
    delivered_at = Column(DateTime, nullable=True, index=True)
    created_at = Column(DateTime, nullable=False, index=True)
    
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()