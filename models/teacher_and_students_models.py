from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from base.base import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    title = Column(String)
    office = Column(String)
    email = Column(String)

class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    section = Column(String)
    department = Column(String)
    semester = Column(String)
    room = Column(String)
    schedule = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

class Relationship(Base):
    __tablename__ = 'relationships'

    student_id = Column(Integer, ForeignKey('students.id'))
    class_id = Column(Integer, ForeignKey('classes.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    enrollment_date = Column(DateTime)
    relationship_type = Column(String)