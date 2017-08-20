# Lambda test skeleton

This project provides a project structure that supports local lambda function testing including lambda
profiling/ billing estimations. Python packages such as [Emulambda](https://github.com/fugue/emulambda/) and
[python-lambda-local](https://pypi.python.org/pypi/python-lambda-local). Emulambda is not in the python package index
so it should be installed on macOS with:

## Emulambda

Emulambda provides profiling information (clock time and memory usage estimation):

```
git clone https://github.com/fugue/emulambda/
pip3 install -e emulambda --user
cd <path>/lambda-test-skeleton/noddy_lambda
emulambda noddy_lambda.lambda_handler - -v < event.json
```

## python-lambda-local

The `python-lambda-local` package must be run inside of a virtualenv. The env can live alongside the project as
long as it is git ignored:

```
pip3 install virtualenv --user
sudo -H virtualenv <path>/azcard-env
```

To select a brew installed python3 as the interpretor for the env and install the package :

```
source <path>/azcard-env/bin/activate
virtualenv -p /usr/local/bin/python3.6 my_project
(azcard-env) sudo -H pip3 install python-lambda-local
```

Run the lambda function:

```
cd <path>/lambda-test-skeleton/noddy_lambda
python-lambda-local -f lambda_handler noddy_lambda.py event.json
```

An amazon engineer has written an [unofficial blog](https://medium.com/@bezdelev/how-to-test-a-python-aws-lambda-function-locally-with-pycharm-run-configurations-6de8efc4b206)
on configuring a test script to use `python-lambda-local`.