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
- coverage >= 6.0
- cProfile (stdlib)
- timeit (stdlib)

- pytest >= 7.0
- pytest-cov >= 3.0
- pytest-mock >= 3.7

<a name="basic-concepts"></a>
## Basic Concepts

<a name="test-packages-for-python"></a>
## Test packages for python

<a name="unittest"></a>
### unittest

#### It has testcases!!!

<a name="pytest"></a>
### pytest

Its is an alternative library, backwards compatible with unittest as well as adding a new design philosophy to tests.

```python

```

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


<a name="mocks"></a>
## Mocks

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [pytest-mock](https://pypi.org/project/pytest-mock/)

<a name="why-using-mocks"></a>
### Why using mocks

<a name="how-to-implement-them"></a>
### How to implement them

#### unittest

```python
import unittest
from unittest.mock import patch, Mock, MagicMock

from tmp import my_module


class MyClassTestCase(unittest.TestCase):

    def test_create_class_call_method(self):
        # Create a mock to return for MyClass.
        m = MagicMock()
        # Patch my_method's return value.
        m.my_method = Mock(return_value=2)

        # Patch MyClass. Here, we could use autospec=True for more
        # complex classes.
        with patch('tmp.my_module.MyClass', return_value=m) as p:
            value = my_module.create_class_call_method()

        # Method should be called once.
        p.assert_called_once()
        # In the original my_method, we would get a return value of 1.
        # However, if we successfully patched it, we'll get a return
        # value of 2.
        self.assertEqual(value, 2)


if __name__ == '__main__':
    unittest.main()
```

from [stackoverflow](https://stackoverflow.com/questions/57044593/python-unittest-mock-class-and-class-method)

#### pytest

```python
import os

class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
```

<a name="code-coverage"></a>
### Code coverage

**Coverage**
https://coverage.readthedocs.io/en/6.4/

```bash
coverage run -m unittest test_arg1.py test_arg2.py test_arg3.py

coverage run -m pytest test_arg1.py test_arg2.py test_arg3.py
pytest --cov=src/package tests/
```

```bash
-------------------- coverage: ... ---------------------
Name                 Stmts   Miss  Cover
----------------------------------------
myproj/__init__          2      0   100%
myproj/myproj          257     13    94%
myproj/feature4286      94      7    92%
----------------------------------------
TOTAL                  353     20    94%
```

<a name="profile"></a>
### Profile

#### cProfile

```python
import cProfile
import re
cProfile.run('re.compile("foo|bar")')
```

```bash
      197 function calls (192 primitive calls) in 0.002 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
     1    0.000    0.000    0.001    0.001 re.py:212(compile)
     1    0.000    0.000    0.001    0.001 re.py:268(_compile)
     1    0.000    0.000    0.000    0.000 sre_compile.py:172(_compile_charset)
     1    0.000    0.000    0.000    0.000 sre_compile.py:201(_optimize_charset)
     4    0.000    0.000    0.000    0.000 sre_compile.py:25(_identityfunction)
   3/1    0.000    0.000    0.000    0.000 sre_compile.py:33(_compile)
```

```bash
python -m cProfile [-o output_file] [-s sort_order] (-m module | myscript.py)
```

#### timeit

```bash
python -m timeit [-n N] [-r N] [-u U] [-s S] [-h] [statement ...]
```