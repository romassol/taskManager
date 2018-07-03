from socket import *
import json
import hashlib
from database import Database
from task import Status


class Api:
    # def __init__(self, database):
    #     self.active_user = None
    #     self.database = database

    @staticmethod
    def sign_up(login, password, database):
        if database.is_user_in_database(login):
            raise ValueError('Such login is already registered, use another one')
        database.add_new_user(login, password)

    @staticmethod
    def log_in(login, password, database):
        if not database.is_login_and_password_correct(login, password):
            raise ValueError('Wrong login or password')
        return database.get_user(login)

    @staticmethod
    def add_task(task_text, active_user):
        if active_user is None:
            raise ValueError('You are not authorized')
        active_user.add_task(task_text, len(active_user.tasks) + 1)

    @staticmethod
    def change_task_status(task_number, status_code, active_user):
        if active_user is None:
            raise ValueError('You are not authorized')
        status_codes = {'a': Status.active, 'c': Status.completed}
        if status_code in status_codes:
            active_user.change_task_status(task_number, status_codes[status_code])
        else:
            raise ValueError('There is no this status code - {code}'.format(code=status_code))

    @staticmethod
    def delete_task(task_number, active_user):
        if active_user is None:
            raise ValueError('You are not authorized')
        active_user.delete_task(task_number)

    @staticmethod
    def get_tasks(active_user, sorted_keys=None):
        if active_user is None:
            raise ValueError('You are not authorized')
        return active_user.get_tasks(sorted_keys)


# def get_command_and_arguments(line):
#     return line.split(' ', 2)

# if __name__ == '__main__':
#     database = Database()
#     api = Api(database)
#     commands = {'AUTH': api.log_in, 'REG': api.sign_up, 'ADD': api.add_task, 'LIST': api.get_tasks,
#                 'CSTAT': api.change_task_status}
#
#
#     sock = socket()
#     sock.bind(('', 9090))
#     sock.listen(1)
#     while True:
#         conn, addr = sock.accept()
#         print('connected:', addr)
#
#         while True:
#             data = conn.recv(1024)
#             command, arguments = data.split(' ', 2)
#             print(data.decode())
#             if not data:
#                 break
#             conn.send(data.upper())
#
#     # conn.close()
