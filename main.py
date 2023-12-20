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


    class Fields(SubClass, base):
        __tablename__ = 'fields'
        name = Column('name', String(100))
        student = relationship('Students', backref='field')
        classes1 = relationship('Classes', backref='field2')

    class Teachers(SubClass, base):
        __tablename__ = 'teachers'
        first_name = Column('first_name', String(50))
        last_name = Column('last_name', String(50))
        classes2 = relationship('Classes', backref='field3')


    class Students(SubClass, base):
        __tablename__ = 'students'
        first_name = Column('first_name', String(50))
        last_name = Column('last_name', String(50))
        field_id = Column('field_id', Integer, ForeignKey('fields.id'))
        classes = relationship('Classes', secondary='student_class', back_populates='students')

    class Classes(SubClass, base):
        __tablename__ = 'classes'
        name = Column('name', String(50))
        teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id'))
        field_id = Column('field_id', Integer, ForeignKey('fields.id'))
        students = relationship('Students', secondary='student_class', back_populates='classes')



    class StudentClass(SubClass, base):
        __tablename__ = 'student_class'
        student_id = Column('student_id', Integer, ForeignKey('students.id'))
        class_id = Column('class_id', Integer, ForeignKey('classes.id'))


if __name__ == '__main__':
    db = DB()
    db.create_session()
    db.create_all_tables()
    # field = db.Fields(name='Math')
    # db.session.add(field)
    # db.session.commit()
    # student = db.Students(first_name='Ali', last_name='Alizadeh')
    # db.session.add(student)
    # db.session.commit()
    # teacher = db.Teachers(first_name='Ali', last_name= 'Alizadeh')
    # db.session.add(teacher)
    # db.session.commit()
    # db.session.query(DB.Fields).filter(DB.Fields.id == 1).delete()
    # db.session.commit()
    #
    # print(student.field_id)

    # classroom = db.Classes(name='A', field_id= 2, teacher_id=teacher.id)
    # db.session.add(classroom)
    # db.session.commit()

    # student = db.session.query(db.Students).one()
    # classs = db.session.query(db.Classes).one()
    #
    # classs.students = [student]
    # db.session.commit()

    # print(classs.students)

