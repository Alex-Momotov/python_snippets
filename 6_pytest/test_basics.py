# ----------------------------------------------------------------------------------------------------------------------
#   Pytest Naming
# Test file     Must begin with 'test_'
# Test method   Must begin with 'test'
# Test class    Must begin with 'Test'

#   Pytest In Pycharm
# 1. Preferences -> Python Integrated Tools -> Default test runner -> pytest. This will enable green arrows next to test functions.
# 2. Pycharm automatically adds project root dir to PYTHONPATH. Run configuration ... -> "Add ... to PYTHONPATH" (both boxes).

# 	Pytest from terminal
# 1. Add project dir to PYTHONPATH env var. E.g. PYTHONPATH=$PYTHONPATH:foo/bar in ~/.bashrc.
# 2. 'pipenv shell' To activate project environment. The environment must have pytest installed.

#   Commands
# pytest                Pytest in all files in current dir and subdirs.
# pytest <dir>          Pytest in dir and its subdirs.
# pytest <file>    		Pytest in the file.
# -m <mark>      		Only tests with given mark.
# -k <substring> 		Only tests with given substring in test/class name.

# ----------------------------------------------------------------------------------------------------------------------
#   Sample Tests
import pytest

# Test class must start with 'Test'
class TestCat:
    def test_somethign(self):
        print('test_somethign')
        assert False

# Test methods must start with 'test'
def test_one():
    print('test_one')
    x = 1
    y = 2
    assert x==y, str(x) + ' is not equal to ' + str(y)

def test_two(testdir):
    print('test_two')
    assert True

# ----------------------------------------------------------------------------------------------------------------------
#   Parametrised
@pytest.mark.parametrize('datapoint', [1, 2, 3, 4])
def test_three(datapoint):
    print(datapoint)
    assert True

@pytest.mark.parametrize("colour", ('red', 'blue', 'green'))
@pytest.mark.parametrize("number", (1, 2, 3))
def test_another(colour, number):
    print(colour, number)

@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
def test_add(input1, input2, output):
    assert input1+input2 == output,"failed"

@pytest.mark.parametrize("number", (1, 2, 3))
@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
def test_add_2(input1, input2, output, number):
    print()


# ----------------------------------------------------------------------------------------------------------------------
#   Marks
# 'pytest -m <mark>' runs tests only with specific mark.

@pytest.mark.set1
def test_four():
    print('test_four')
    assert False

@pytest.mark.untrusted
def test_six():
    print('test_four')
    assert False
# ----------------------------------------------------------------------------------------------------------------------
#   Skipping tests

@pytest.mark.skip
def test_to_skip():
    print("I've been skipped")

# ----------------------------------------------------------------------------------------------------------------------
#   Fixture - Basics
# Test method takes fixture name as parameter, then can use fixture name in it's body to retrieve fixture results

@pytest.fixture
def supply_A_B_C():
    a = 'a'
    b = 'b'
    c = 'c'
    return [a, b, c]

def test_seven(supply_A_B_C):
    for x in supply_A_B_C: print(x)

# ----------------------------------------------------------------------------------------------------------------------
#   Fixture - Scope
# function	  Run once per test
# class	      Run once per class of tests
# module	  Run once per module
# session	  Run once per session
# The default scope is function

@pytest.fixture(scope='class')
def sample_fixture():
    print('sample_fixture')

class TestOwl:
    # Even though we use fixture in each class test, it only runs once because scope is class
    def test_one(self, sample_fixture):
        print('test_one')

    def test_two(self, sample_fixture):
        print('test_two')



# ----------------------------------------------------------------------------------------------------------------------
#   Fixture - Tear Down
# Fixture function must accept parameter 'request' then declare some enclosed fin() method and call 'request.addfinalizer(fin)'
# Just as fixture itself, enclosed tear down function will run according to the current fixture scope

@pytest.fixture
def db_connection(request):
    print('opening db connection')
    def fin():
        print('closing db connection')
    request.addfinalizer(fin)
    return 'db client'

def test_bb(db_connection):
    print('test_b is using', db_connection)

def test_bbb(db_connection):
    print('test_bb is using', db_connection)

# ----------------------------------------------------------------------------------------------------------------------
#   Fixtue - Autouse
# When 'autouse=True' the fixture will run automatically for each test in the session, without tests taking fixture name as parameter

# This will run before each test in the session
@pytest.fixture(autouse=True)
def autouse_exampl_function():
    print('autouse_exampl_function')

# This will run before each test in the session for tests outside classes, and only once per class for tests inside a classes
@pytest.fixture(scope='class', autouse=True)
def autouse_example_class():
    print('autouse_example_class')

# ----------------------------------------------------------------------------------------------------------------------
#   Fixture - Autouse within a class
# If fixture with 'autouse=True' is within a class, it will only apply to tests in that class and not tests outside it.
class TestOne:

    @pytest.fixture(scope='class', autouse=True)
    def fixtureOne(self):
        print('fixtureOne')

    @pytest.fixture(scope='function', autouse=True)
    def fixtureTwo(self):
        print('fixtureTwo')

    def test_one(self):
        print('test_one')

    def test_two(self):
        print('test_two')

def test_outside():
    print('test_outside')

# ----------------------------------------------------------------------------------------------------------------------
#   Fixture - Usefixtures
# Allows to use fixtures on all methods withing a class

@pytest.fixture
def example():
    print('example fixture')

@pytest.fixture
def example_two():
    print('example two fixture')

@pytest.mark.usefixtures("example", "example_two")
class TestFox:
    def test_one(self):
        print('test_one')

    def test_two(self):
        print('test_two')

# ----------------------------------------------------------------------------------------------------------------------































































