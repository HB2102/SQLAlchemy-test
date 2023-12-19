from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import and_, or_


engine = create_engine('sqlite:///database.db')
Base = declarative_base()
session = sessionmaker(bind=engine)()


class Student(Base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    clssroom_id = Column('classroom_id', Integer, ForeignKey("classroom.id"))


class ClassRoom(Base):
    __tablename__ = 'classroom'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    students = relationship('Student', backref='classroom', uselist=False)



Base.metadata.create_all(engine)


# READING DATA =========================================================
# students1 = session.query(Student).all()
#
# for student in students1:
#     print(student._id, student.name)



# students2 = session.query(Student).filter(Student.name=="Ali").all()
# for student in students2:
#      print(student._id, student.name)



# INSERTING DATA ======================================================

# student = Student(name="Mohammadreza")
# student2 = Student(name="Mohammadali")
# session.add_all([student, student2])



# DELETING DATA ===========================================================

# student = session.query(Student).filter(Student.name=="Mohammadali").delete()
# # session.delete(student)
# session.commit()


# UPATING DATA ====================================================================

# session.query(Student).filter(Student._id == 3).update({'name':'Hossein'})
# session.commit()







session.commit()