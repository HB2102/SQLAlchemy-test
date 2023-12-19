from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import and_, or_


class DB:

    engine = create_engine("sqlite:///test_database.db")
    base = declarative_base()

    def __init__(self):
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()


    def create_session(self):
        self.session = self.session_maker()


    def create_all_tables(self):
        self.base.metadata.create_all(self.engine)




    class SubClass:
        id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)


    class People(SubClass, base):
        __tablename__ = 'people'
        first_name = Column('first_name', String(50))
        last_name = Column('last_name', String(50))
        position_id = Column('position_id', Integer, ForeignKey('position.id'))


    class Position(SubClass, base):
        __tablename__ = 'position'
        name = Column('name', String(50))
        people = relationship('People', backref='position', back_populates='')


