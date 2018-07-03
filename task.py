from enum import Enum
from datetime import datetime


class Status(Enum):
    active = 1
    completed = 2

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value


class Task:
    def __init__(self, task_text, id, creation_time=None, status=None, end_time=None, execution_time_in_seconds=None):
        self.id = id
        self.text = task_text
        self.creation_time = datetime.now() if creation_time is None else creation_time
        self.status = Status.active if status is None else status
        self.end_time = None if end_time is None else end_time
        self.execution_time_in_seconds = None if execution_time_in_seconds is None else execution_time_in_seconds
        self._functions_from_status = {Status.active: self.active, Status.completed: self.complete}

    def to_dict(self):
        return {'text': self.text, 'id': self.id, 'creation_time': self.creation_time.strftime("%Y-%m-%d-%H-%M-%S"),
                'status': str(self.status),
                'end_time': self.end_time.strftime("%Y-%m-%d-%H-%M-%S") if self.end_time is not None else None,
                'execution_time_in_seconds': self.execution_time_in_seconds}

    def __repr__(self):
        return 'Task: {0}\n' \
               'id: {5}' \
               'creation time: {1}\n' \
               'status: {2}\n' \
               'end time: {3}\n' \
               'execution time in seconds: {4}'.format(self.text, self.creation_time, self.status,
                                                       self.end_time, self.execution_time_in_seconds, self.id)

    def __str__(self):
        return 'Task: {0}\n' \
               'id: {5}' \
               'creation time: {1}\n' \
               'status: {2}\n' \
               'end time: {3}\n' \
               'execution time in seconds: {4}'.format(self.text, self.creation_time, self.status,
                                                       self.end_time, self.execution_time_in_seconds, self.id)

    def change_status(self, new_status):
        if new_status in self._functions_from_status:
            self._functions_from_status[new_status]()
        else:
            raise ValueError('There is no function for this status - {status}'.format(status=status))

    def active(self):
        self.status = Status.active
        self.end_time = None

    def complete(self):
        self.status = Status.completed
        self.end_time = datetime.now()
        self.execution_time_in_seconds = (self.end_time - self.creation_time).total_seconds()
