from db.postgres_db import db_session
from models.student_models import StudentProfile

def insert_student_profile(profile):
    new_profile = StudentProfile(
        id=int(profile['id']),
        first_name=profile['first_name'],
        last_name=profile['last_name'],
        age=profile['age'],
        address=profile['address'],
    )
    db_session.add(new_profile)
    db_session.commit()

    return new_profile.id