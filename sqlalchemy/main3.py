from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

# create the engine and connect to a new SQLite database file
engine = create_engine('sqlite:///sample.db')

# create a session factory for creating sessions with the database
Session = sessionmaker(bind=engine)

# create a base class for declarative ORM
Base = declarative_base()

# define the Foo and Bar classes
class Foo(Base):
    __tablename__ = 'foo'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bar = relationship('Bar', uselist=False, back_populates='foo')

class Bar(Base):
    __tablename__ = 'bar'
    id = Column(Integer, primary_key=True)
    foo_id = Column(Integer, ForeignKey('foo.id'), unique=True)
    info = Column(String)
    foo = relationship('Foo', back_populates='bar')

# create the tables in the database
Base.metadata.create_all(engine)


# create a session
session = Session()

# create a new Foo object
foo = Foo(name='foo1')

# create a new Bar object and associate it with the Foo object
bar = Bar(info='bar1', foo=foo)

# add the Foo and Bar objects to the session
session.add(foo)
session.add(bar)

# commit the session to save the changes to the database
session.commit()

# query the Foo table and print the results
foos = session.query(Foo).all()
for foo in foos:
    print(f'Foo: {foo.name}, Bar: {foo.bar.info}')
