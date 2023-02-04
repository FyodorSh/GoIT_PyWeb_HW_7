from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # students = relationship("Student")
    # students = relationship("Student", back_populates="groups")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'), nullable=False)

    # group = relationship("Group")
    # grade = relationship("Grade")
   # group = relationship("Group", back_populates="students")
   #  grade = relationship("Grade", back_populates="students")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)

    # subjects = relationship("Subject")
    # subjects = relationship("Subject", back_populates="teachers")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False)

    # teacher = relationship("Teacher")
    # grade = relationship("Grade")

    # teacher = relationship("Teacher", back_populates="subjects")
    # grade = relationship("Grade", back_populates="subjects")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    subject_id = Column(ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, default=func.now())

    # student = relationship("Student", back_populates="grades")
    # subject = relationship("Subject", back_populates="grades")
