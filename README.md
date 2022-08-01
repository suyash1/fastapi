## Sample [FastAPI](https://fastapi.tiangolo.com/) Application to demonstrate Cycle analysis in a list and Async architecture with [Celery](https://docs.celeryproject.org/), [RabbitMQ](https://www.rabbitmq.com/)


### Setting up the VirtualEnv and install dependencies

Go inside the project folder and execute the below commands. We will use [venv](https://docs.python.org/3/library/venv.html) to setup the VirtualEnv.

```
pipenv shell --python 3.9.2
pipenv install -r requirements.txt

```

All the dependencies are in requirements.txt. Python version I used is 3.8.9 is used for this project.

### Prerequisite
1. Python 3.7+
3. RabbitMQ instance

### Run the Application
Start the virtual env and then
```
pip install -r requirements.txt
```
This will start the application on port 8000

You can start the application by running the following
```
uvicorn main:app --reload
```

To start the Celery process, navigate to the project directory in a new terminal, activate the virtual environment, and then run:
```
celery -A main.celery worker --loglevel=info -Q tasks (in a new tab)
```
Please make sure rabbitmq is running at this point.

### Test the application
You can visit http://127.0.0.1:8000/docs in our browser to see the interactive API documentation provided by [Swagger UI](https://github.com/swagger-api/swagger-ui). You can try the APIs in the swagger. I have added `input.json` file for testing the cycle in lists. You can modify the file and add more cases to it. Alternatively, you can upload another test file, which will appear in the application root folder later.
