from faker import Faker

from database.db import session
from database.models import Group

fake = Faker('uk_UA')


def create_groups():
    for _ in range(1, 5):
        group = Group(
            name=fake.bothify(text='Group ?#'),
        )
        session.add(group)
    session.commit()


if __name__ == "__main__":
    create_groups()
