from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'mytable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


# Create the database engine and session
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

new_id = None

with Session.begin() as session:
    # Create a new row and add it to the session
    new_row = MyTable(name='John Doe', age=30, email='john@example.com')
    session.add(new_row)

    # Commit the changes to the database
    session.flush()

    new_id = new_row.id

# Access the ID of the newly generated row
print("NEW ID: ", new_id)
