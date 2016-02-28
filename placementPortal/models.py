from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
# from .database import Base
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("sqlite:///placementPortal.db",convert_unicode=True)
Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

class User(Base):
    __tablename__ = 'users'
    usn = Column(String(20), primary_key=True)
    name = Column(String(30))
    username = Column(String(30), unique=True)

    email = Column(String(20))
    password = Column(String(30))
    def __repr__(self):
        return "User "+name

class SuperUser(Base):
    __tablename__ = 'superusers'
    username = Column(String(20), primary_key=True)
    password = Column(String(20))
    email = Column(String(20))



class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    contact_number = Column(String(15), unique=True)
    # categories = relationship('Category', back_populates='department')

    def __repr__(self):
        return "Department: "+self.name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.add_all([
                    SuperUser(username="admin",password="admin",email="admin@kleit.ac.in"),
                    ])

    session.commit()
    session.close()
