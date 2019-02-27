**TODO**: 

Assume you are already cloned this repository.

In root folder run next commands:
```
vagrant up
vagrant ssh
cd /home/vagrant/pbc/
source bin/activate
# update pip && install depencies
./update-pip.sh
pytest -v tests/
```

Python requirements:

- Python version 2.7, packages:
  * attrs==17.3.0
  * funcsigs==1.0.2
  * pluggy==0.6.0
  * py==1.5.2
  * pytest==3.3.0
  * selenium==3.8.0
  * six==1.11.0
  * paramiko==2.4.0

Application structure:

​	app.py - main program. Accept in arguments which command to execute and and one or several numbers for processing. To see details type python app.py -h

Depending from parameters happens call of imported module and printing its output.

​      some_app folder contain next files:

```some_app/
some_app/
├── __init__.py
├── fibonacci.py
└── numbers_summ.py

```

Inside \__init__.py listed allowed for import functions.

**fibonacci.py** accept as argument number in ```str ``` mode, module also return string with result. Main logic - assign initial values for two variables, initialize empty list, for saving temporary result, then in ```for``` loop appends first value and using feature ```tuple``` data structure,  reassign values for variables.

For example, ```python2 app.py -a fibonacci -n 5``` will print next output:

```````
<type 'str'>
5
0, 1, 1, 2, 3
```````

**numbers_summ.py** accept as argument string with numbers sequence via space 
and return ```list oftuples ``` with number pairs,  which sum equal 10. Inside main function ```num_func``` define two empty lists for results containing, then check type of argument and convert it to the ```list``` type. Inside double ```for``` loop performs adding each element with each other, form position element+1 till last . Combination, which is equal 10 and those combinations are not resent inside list with final data appends into that list.

Both modules uses ```func_info``` decorator, which print info about arguments and its type.

For application provided unit test inside folder tests:

```
tests/
├── conftest.py
├── __init__.py
├── test_fib.py
└── test_numbers.py
```

To run tests, type:

```````
pytest -v tests/
```````

Tests use pytest feature ```@pytest.fixture``` with scope module.

Before each test checks is environment is ready, if not with ```paramiko``` module performs setup selenium-server.
