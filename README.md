# testing_workshop
Workshop of code testing

## Table of contents:

- [Requirements](#requirements)
- [Test packages for python](#test-packages-for-python)
  - [unittest](#unittest)
  - [pytest](#pytest)
- [Basic concepts](#basic-concepts)
  - [Setup](#setup)
  - [Teardown](#teardown)
  - [Parametrization](#parametrization)
  - [Temporary Files and Directories](#temp)
  - [Asserting Errors](#asserting-errors)
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
- tempfile (stdlib)

- pytest >= 7.0
- pytest-cov >= 3.0
- pytest-mock >= 3.7

<a name="test-packages-for-python"></a>
## Test packages for python

<a name="unittest"></a>
### unittest

It is a standard library for python, and its version will depend on your python instalation.

- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Asserts](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)

#### It has testcases!!!

```python
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
```

<a name="pytest"></a>
### pytest

Its is an alternative library, backwards compatible with unittest as well as adding a new design philosophy to tests.

- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Good Practices](https://docs.pytest.org/en/6.2.x/goodpractices.html)

```python
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

[More about Fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html), specialy how to do Teardowns and Cleanups.

<a name="basic-concepts"></a>
## Basic Concepts

<a name="setup"></a>
### Setup

#### Unittest

```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')
```

#### Pytest and its fixtures

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

<a name="teardown"></a>
### Teardown

#### Unittest

```python
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        
    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

```

#### Pytest

[Pytest Teardown](https://docs.pytest.org/en/latest/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization)

```python
import pytest

@pytest.fixture()
def resource():
    print("setup")
    yield "resource"
    print("teardown")

class TestResource:
    def test_that_depends_on_resource(self, resource):
        print("testing {}".format(resource))
```

[Stackoverflow Example](https://stackoverflow.com/a/39401087)

<a name="parametrization"></a>
### Parametrization

#### Pytest

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

<a name="temp"></a>
### Temporary Files and Directories

[tempfile](https://docs.python.org/3/library/tempfile.html)

```python
import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()
# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()
# file is now closed and removed

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
  print('created temporary directory', tmpdirname)
# directory and contents have been removed
```

```python
import unittest
from pathlib import Path
import tempfile

class TestCase(unittest.TestCase):
    def setUp(self):
        self.temp_folder = tempfile.TemporaryDirectory()
        self.working_dir = Path(self.temp_dir.name)


    def tearDown(self):
        self.temp_folder.cleanup()
```

```python
# content of test_tmpdir.py
def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
    assert 0
```

[tmpdir pytest fixtures](https://docs.pytest.org/en/6.2.x/tmpdir.html#the-tmpdir-fixture)

<a name="asserting-errors"></a>
### Asserting Errors

#### Unittest

```python
import unittest


def whatever(i):
    return i/0


class TestWhatEver(unittest.TestCase):
  
    def test_whatever(self):
        with self.assertRaises(ZeroDivisionError):
            whatever(3)

    def test_whatever(self):
        self.assertRaises(ZeroDivisionError, div, 3,0)
```

#### Pytest

```python
def test_raises():
    with pytest.raises(Exception) as exc_info:   
        raise Exception('some info')
    # these asserts are identical; you can use either one   
    assert exc_info.value.args[0] == 'some info'
    assert str(exc_info.value) == 'some info'

def test_another_raises():
  with pytest.raises(ValueError, match='must be 0 or None'):
      raise ValueError('value must be 0 or None')

def test_the_second_another_raises():
  with pytest.raises(ValueError, match=r'must be \d+$'):
      raise ValueError('value must be 42')
```

[Stackoverflow Discussion](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)

<a name="types-of-tests"></a>
## Type of tests

Tests can be caracterized by their scope. They can test individual functions and methods and other structures, 
can test the interaction of many, or enven full use case scenarios.

The appropriate coverage of the test with different kinds of tests, guarantes that from its small building blocks, to 
larger interoperable blocks and usecases, the expectations regarding inputs and outputs are validated.

<a name="unit-tests"></a>
### Unit tests

- [Example - Testing IO functions](https://github.com/nebi-um/testing_workshop/blob/main/tests/unit_tests/test_io.py)
- [Example - Testing Data Structures](https://github.com/nebi-um/testing_workshop/blob/main/tests/unit_tests/test_data_structures.py)
- [Example - Testing Mocked SeqIO BLAST](https://github.com/nebi-um/testing_workshop/blob/main/tests/unit_tests/test_blast.py)
- [Example - Testing Uniprot API call](https://github.com/nebi-um/testing_workshop/blob/main/tests/unit_tests/test_api.py)

<a name="integration-tests"></a>
### Integration tests

- [Example - Testing a Data Structure Interaction](https://github.com/nebi-um/testing_workshop/blob/main/tests/integration_tests/test_data_structures_blast.py)
- [Example - Testing a IO to Data Structure loading](https://github.com/nebi-um/testing_workshop/blob/main/tests/integration_tests/test_io_data_structures.py)

<a name="end-to-end-tests"></a>
### End-to-end tests

- [Example - Testing a Blast Pipeline](https://github.com/nebi-um/testing_workshop/blob/main/tests/end_to_end_tests/test_blast_pipeline.py)

<a name="mocks"></a>
## Mocks

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [pytest-mock](https://pypi.org/project/pytest-mock/)

<a name="why-using-mocks"></a>
### Why using mocks

<a name="how-to-implement-them"></a>
### How to implement them

[MagicMock vs Mock](https://stackoverflow.com/questions/17181687/mock-vs-magicmock)

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