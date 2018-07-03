import hashlib
from task import Task


class User:
    def __init__(self, login, password, tasks=None):
        self.login = login
        self.password = password #hashlib.sha1(password).hexdigest()
        self.tasks = tasks if tasks else []
        # self.trash = []
        self.sorted_keys = {'creation time': lambda task: task.creation_time, 'status': lambda task: task.status,
                            'end time': lambda task: task.end_time, 'text length': lambda task: len(task.text),
                            'execution time': lambda task: task.execution_time_in_seconds}

    def __hash__(self):
        return self.login

    def added_task(self, task):
        self.tasks.append(task)

    def add_task(self, task_text, id):
        self.tasks.append(Task(task_text, id))

    def delete_task(self, task_number):
        self.tasks.pop(int(task_number) - 1)

    def change_task_status(self, task_number, new_status):
        self.tasks[int(task_number) - 1].change_status(new_status)

    # def add_task_from_trash(self, task_number):
    #     self.tasks.append(self.trash.pop(task_number - 1))

    # def empty_trash(self):
    #     self.trash = []

    # def delete_task_from_trash(self, task_number):
    #     self.trash.pop(task_number - 1)

    def get_tasks(self, sorted_keys=None):
        if sorted_keys is None:
            return self.tasks
        keys = []
        for key in sorted_keys:
            if key not in self.sorted_keys:
                raise ValueError('Cannot be sorted by key - {key}'.format(key=key))
            keys.append(self.sorted_keys[key])
        sorted_fields = []
        is_none = False
        for f in keys:
            is_none = False
            for t in self.tasks:
                if f(t) is None:
                    is_none = True
                    break
            if not is_none:
                sorted_fields.append(f)
        if len(sorted_fields) == 0:
            return self.tasks
        return sorted(self.tasks, key=lambda task: [f(task) for f in sorted_fields])
