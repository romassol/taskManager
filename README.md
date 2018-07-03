### Как пользоваться

#### Команды

AUTH login password - авторизация
REG login password - регистрация
ADD task_text - создание новой задачи                                                              |
LIST (filter - необязательно) - список всех тасков с фильтрацией                |только для авторизованных
CSTAT task_number a/c - изменение состояния задачи active/completed  |

EXIT - выход из приложения

#### Виды фильтров

creation time - по времени создания
status - по статусу
end time - по времени завершения
text length - по длине сообщения
execution time - по времени выполнения

#### Пример сессии

```
REG olya 1234
Ok
AUTH olya 1234
Ok
ADD купить хлеб
Ok
ADD спать
Ok
ADD есть
Ok
CSTAT 2 c
Ok
LIST
[Task: купить хлеб
id: 1
creation time: 2018-07-03 23:50:46.476624
status: Status.active
end time: None
execution time in seconds: None, Task: спать
id: 2
creation time: 2018-07-03 23:51:01.739780
status: Status.completed
end time: 2018-07-03 23:51:42.201050
execution time in seconds: 40.46127, Task: есть
id: 3
creation time: 2018-07-03 23:51:15.744741
status: Status.active
end time: None
execution time in seconds: None]
LIST status
[Task: купить хлеб
id: 1
creation time: 2018-07-03 23:50:46.476624
status: Status.active
end time: None
execution time in seconds: None, Task: есть
id: 3
creation time: 2018-07-03 23:51:15.744741
status: Status.active
end time: None
execution time in seconds: None, Task: спать
id: 2
creation time: 2018-07-03 23:51:01.739780
status: Status.completed
end time: 2018-07-03 23:51:42.201050
execution time in seconds: 40.46127]
LIST status, creation time
[Task: купить хлеб
id: 1
creation time: 2018-07-03 23:50:46.476624
status: Status.active
end time: None
execution time in seconds: None, Task: есть
id: 3
creation time: 2018-07-03 23:51:15.744741
status: Status.active
end time: None
execution time in seconds: None, Task: спать
id: 2
creation time: 2018-07-03 23:51:01.739780
status: Status.completed
end time: 2018-07-03 23:51:42.201050
execution time in seconds: 40.46127]
EXIT
```

### Инфраструктура

`user.py` - класс пользователя + методы, связанные с изменением списка задач данного пользователя

`task.py` - класс клиента + метод изменения состояния задачи и enum статуса

`database.py` - класс базы данных + методы, связанные с пользователями, хранящимися в этой базе данных

`api.py` - класс Api, который содержит методы по сути самого task manager, например регистрация, аутентификация и т.п. 

`commandController.py` - взаимодействие между методами из Api и командами, воторые будет вводить пользователь из консоли

`main.py`- создание базы данных, запуск приложения, обработка команд

`data.txt` - текстовый файл, в котором хранится база данных в формате json

Если файл `data.txt` присутствует призапуске приложения, то данные берутся от туда, иначе создается новая пустая база данных

