from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create an engine to connect to a SQLite database
engine = create_engine('sqlite:///example.db', echo=True)

# create a declarative base object
Base = declarative_base()

# create a model class that uses the declarative base
class Foo(Base):
    __tablename__ = 'foo'

    id = Column(Integer, primary_key=True)
    data = Column(String)

# create the table in the database
Base.metadata.create_all(engine)

# create a session factory to interact with the database
Session = sessionmaker(bind=engine)

# create a session
session = Session()

# create a new instance of the Foo class and add it to the session
foo = Foo(data="hello world")
session.add(foo)

# commit the changes to the database
session.commit()

# query the database for the instance we just inserted
foo = session.query(Foo).filter_by(id=1).first()

# update the row with new string data
foo.data = "hello foobar"

# commit the changes to the database
session.commit()
