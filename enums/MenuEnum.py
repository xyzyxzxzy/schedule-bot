from enum import Enum


class MenuEnum(Enum):

    SCHEDULE_TODAY = {'name': 'Расписание на сегодня', 'command': {"command": "!с"}, 'payload': 'с'}
    SCHEDULE_TOMORROW = {'name': 'Расписание на завтра', 'command': {"command": "!з"}, 'payload': 'з'}