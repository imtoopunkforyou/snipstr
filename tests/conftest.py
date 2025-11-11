import faker
import pytest


@pytest.fixture
def fake():
    return faker.Faker()

@pytest.fixture
def long_text(fake):
    return fake.text(max_nb_chars=1_000)
