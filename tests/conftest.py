import faker
import pytest


@pytest.fixture
def fake():
    return faker.Faker()


@pytest.fixture
def long_text(fake):
    return fake.text(max_nb_chars=1_000)


@pytest.fixture
def not_int(fake):
    return fake.word()


@pytest.fixture
def negative_int(fake):
    return 0 - fake.pyint()


@pytest.fixture
def not_side(fake):
    return fake.word()


@pytest.fixture
def source(fake):
    return fake.pyobject()


@pytest.fixture
def very_long_text(fake):
    return fake.text(max_nb_chars=1_000) + fake.text(max_nb_chars=1_000)


@pytest.fixture
def length():
    return 10
