from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .models import User

engine = create_engine('sqlite:///placementPortal.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)

def create_user(usn, name, username, email, password):
    try:
        db_session.add(User(usn, name, username, email,password))
        return "{} Created Successfully"+format(name)
    except Exception as e:
        return "Unable to create user, probably user exists"


def create_ward(ward_no, ward_name):
    db_session.add(Ward(number=eval(ward_no),name=ward_name))
    db_session.commit()

def create_department(id,name,contact):
    db_session.add(Department(id=eval(id),name=name, contact_number=contact))
    db_session.commit()


def get_wards():
    return db_session.query(Ward).all()

def get_departments():
    return db_session.query(Department).all()


