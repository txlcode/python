import task
from api import app
task.my_job()


if __name__ == '__main__':
    app.run(debug=True)
