from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from base.base import Base


class StudentProfile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    address = Column(String)

    # Updated relationships
    performance = relationship('StudentPerformance', back_populates='student_obj')
    lifestyle = relationship('Student_Lifestyle', back_populates='student_obj')
    # review = relationship('Review', back_populates='student_obj')
    # academy = relationship('Academy', back_populates='student_obj')

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "address": self.address,
        }


class Student_Lifestyle(Base):
    __tablename__ = 'lifestyle'
    id = Column(Integer, primary_key=True)
    study_hours_per_day = Column(Float)
    extracurricular_hours_per_day = Column(Float)
    sleep_hours_per_day = Column(Float)
    social_hours_per_day = Column(Float)
    physical_activity_hours_per_day = Column(Float)
    gpa = Column(Float)
    stress_level = Column(Float)

    student_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    student_obj = relationship('StudentProfile', back_populates='lifestyle')

    def to_dict(self):
        return {
            "study_hours_per_day": self.study_hours_per_day,
            "extracurricular_hours_per_day": self.extracurricular_hours_per_day,
            "sleep_hours_per_day": self.sleep_hours_per_day,
            "social_hours_per_day": self.social_hours_per_day,
            "physical_activity_hours_per_day": self.physical_activity_hours_per_day,
            "gpa": self.gpa,
            "stress_level": self.stress_level,
            "student_id": self.student_id,
        }


class StudentPerformance(Base):
    __tablename__ = 'performance'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    current_grade = Column(Float)
    attendance_rate = Column(Float)
    assignment_completed = Column(Integer)
    missed_deadlines = Column(Integer)
    participation_score = Column(Float)
    midterm_grade = Column(Float)
    study_group_attendance = Column(Integer)
    office_hours_visits = Column(Integer)
    extra_credit_completed = Column(Integer)

    student_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    student_obj = relationship('StudentProfile', back_populates='performance')

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "current_grade": self.current_grade,
            "attendance_rate": self.attendance_rate,
            "assignment_completed": self.assignment_completed,
            "missed_deadlines": self.missed_deadlines,
            "participation_score": self.participation_score,
            "midterm_grade": self.midterm_grade,
            "study_group_attendance": self.study_group_attendance,
            "office_hours_visits": self.office_hours_visits,
            "extra_credit_completed": self.extra_credit_completed,
            "student_id": self.student_id,
        }
