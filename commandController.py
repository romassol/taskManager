from api import Api


class CommandController:
    def __init__(self, database):
        self.active_user = None
        self.database = database
        self.commands = {'AUTH': Api.log_in, 'REG': Api.sign_up, 'ADD': Api.add_task, 'LIST': Api.get_tasks,
                         'CSTAT': Api.change_task_status}

    @staticmethod
    def find_arguments_error(arguments, arguments_number, command):
        if len(arguments) != arguments_number:
            raise ValueError('Wrong number of arguments for command - {command}'.format(command=command))

    def read_command(self, input_line):
        command_line = input_line.split(' ', 1)
        if command_line[0] != 'LIST':
            if len(command_line) != 2:
                 return 'Wrong command'
        if command_line[0] == 'AUTH' or command_line[0] == 'REG':
            command, arguments = command_line
            arguments = arguments.split(' ')
            try:
                CommandController.find_arguments_error(arguments, 2, command)
            except Exception as e:
                return e
            try:
                self.active_user = self.commands[command](*arguments, self.database)
                return 'Ok'
            except Exception as e:
                return e

        elif command_line[0] == 'ADD':
            command, arguments = command_line
            try:
                self.commands[command](arguments, self.active_user)
                return 'Ok'
            except Exception as e:
                return e
        elif command_line[0] == 'LIST':
            arguments = None
            if len(command_line) >= 2:
                arguments = command_line[1].split(',')
                arguments = [a.strip() for a in arguments]
            try:
                return self.commands[command_line[0]](self.active_user, arguments)
            except Exception as e:
                return e
        elif command_line[0] == 'CSTAT':
            command, arguments = command_line
            arguments = arguments.split(' ')
            try:
                CommandController.find_arguments_error(arguments, 2, command)
            except Exception as e:
                return e
            try:
                self.commands[command](*arguments, self.active_user)
                return 'Ok'
            except Exception as e:
                return e
        else:
            return 'Wrong command'
