import json
import hashlib
import datetime
from user import User
from task import Task
from task import Status


class Database:
    def __init__(self, data=None):
        self.data = {}
        if data:
            json_date = json.loads(data)
            for login, password in json_date['Users'].items():
                self.data[login] = User(login, password)
            status = {'Status.active': Status.active, 'Status.completed': Status.completed}
            for login, tasks in json_date['Tasks'].items():
                for task in tasks:
                    self.data[login].added_task(Task(task['text'], int(task['id']),
                                                     Database.get_time(task['creation_time']),
                                                     status[task['status']],
                                                     Database.get_time(task['end_time']),
                                                     int(task['execution_time_in_seconds'])
                                                     if task['execution_time_in_seconds'] is not None else None))

    @staticmethod
    def get_time(line):
        if line is None:
            return None
        arguments = line.split('-')
        arguments = [int(a) for a in arguments]
        return datetime.datetime(*arguments)

    def add_new_user(self, login, password):
        self.data[login] = User(login, hashlib.sha1(password.encode()).hexdigest())

    def is_user_in_database(self, login):
        return login in self.data

    def is_login_and_password_correct(self, login, password):
        return self.is_user_in_database(login) and self.data[login].password == hashlib.sha1(password.encode()).hexdigest()

    def get_user(self, login):
        return self.data[login]