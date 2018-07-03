import json
from database import Database
from commandController import CommandController


if __name__ == '__main__':
    data = None
    try:
        file = open('data.txt')
    except IOError as e:
        print('Database not detected')
    else:
        with file:
            data = file.readlines()
            data = data[0]
    database = Database(data)
    cc = CommandController(database)
    input_line = input()
    while input_line != 'EXIT':
        print(cc.read_command(input_line))
        input_line = input()
    json_data = {"Users": {}, "Tasks": {}}
    for login, user in database.data.items():
        json_data['Users'][login] = user.password
        json_data['Tasks'][login] = [task.to_dict() for task in user.tasks]
    with open('data.txt', 'w', encoding='utf8') as outfile:
        json.dump(json_data, outfile)
