import faker
import pytest


@pytest.fixture
def fake():
    return faker.Faker()
