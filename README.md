# testing_workshop
Workshop of code testing

## Table of contents:

- [Requirements](#requirements)
- [Basic concepts](#basic-concepts)
- [Test packages for python](#test-packages-for-python)
  - [unittest](#unittest)
  - [pytest](#pytest)
- [Type of tests](#types-of-tests)
  - [Unit tests](#unit-tests)
  - [Integration tests](#integration-tests)
  - [End-to-end tests](#end-to-end-tests)
- [Mocks](#mocks)
  - [Why using mocks](#why-using-mocks)
  - [How to implement them](#how-to-implement-them)
- [Code coverage](#code-coverage)
- [Profile](#profile)

<a name="requirements"></a>
## Requirements

- unittest (stdlib)
- pytest >= 7.0
- coverage >= 6.0
- pytest-cov >= 3.0

<a name="basic-concepts"></a>
## Basic Concepts

<a name="test-packages-for-python"></a>
## Test packages for python

<a name="unittest"></a>
### unittest

#### It has testcases!!!

<a name="pytest"></a>
### pytest

#### It has fixtures!!!

```python
# Functional test fixtures
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)

# Test classes fixtures, through the use of scope, this can also be made available through whole modules, packages or session
@pytest.fixture(scope='class')
def input(request):
    request.cls.varA = 1
    request.cls.varB = 2
    request.cls.varC = 3
    request.cls.modified_varA = 2

@pytest.mark.usefixtures('input')
class TestClass:
    def test_1(self):
        sum(self.varA, self.varB)

    def test_2(self):
        sum(self.varC, self.modified_varA)
```

#### Fixtures can be parametrized!!!

```python
testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected
```

[More about Fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html), specialy how to do Teardowns and Cleanups.

<a name="paragraph1"></a>
## Type of tests

<a name="paragraph1"></a>
### Unit tests

<a name="paragraph1"></a>
### Integration tests

<a name="paragraph1"></a>
### End-to-end tests

```bash
pytest --cov=myproj tests/
```

<a name="mocks"></a>
## Mocks

  - [Why using mocks](#why-using-mocks)
  - [How to implement them](#how-to-implement-them)
  - [Code coverage](#code-coverage)
  - [Profile](#profile)