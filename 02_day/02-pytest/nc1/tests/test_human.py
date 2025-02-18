import pytest
from nc1.human import Human

@pytest.fixture
def sample_human():
    return Human("John Doe", 25, 1.75, 70.0)

def test_human_initialization():
    human = Human("Alice", 30, 1.65, 55.0)
    assert human.name == "Alice"
    assert human.age == 30
    assert human.height == 1.65
    assert human.weight == 55.0

def test_get_bmi(sample_human):
    # BMI = 70 / (1.75 ** 2) ≈ 22.86
    assert round(sample_human.get_bmi(), 2) == 22.86

def test_is_adult():
    adult = Human("Bob", 20, 1.80, 75.0)
    minor = Human("Charlie", 15, 1.70, 60.0)
    assert adult.is_adult() is True
    assert minor.is_adult() is False

def test_introduce(sample_human):
    expected = "Hi, I'm John Doe and I'm 25 years old."
    assert sample_human.introduce() == expected

def test_celebrate_birthday(sample_human):
    initial_age = sample_human.age
    sample_human.celebrate_birthday()
    assert sample_human.age == initial_age + 1

def test_invalid_height():
    with pytest.raises(ValueError):
        Human("Invalid", 25, 0, 70.0)  # Height cannot be zero

def test_invalid_weight():
    with pytest.raises(ValueError):
        Human("Invalid", 25, 1.75, -1)  # Weight cannot be negative 