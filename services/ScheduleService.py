class ScheduleService:

    def get_schedule_today(self) -> list:
        return [
            {"name": "Ин-яз", "room": "423"},
            {"name": "Ин-яз", "room": "423"},
            {"name": "Ин-яз", "room": "423"},
            {"name": "Ин-яз", "room": "423"}
        ]
    

    def get_schedule_tomorrow(self) -> list:
        return [
            {"name": "Математика", "room": "423"},
            {"name": "Математика", "room": "423"},
            {"name": "Математика", "room": "423"},
            {"name": "Математика", "room": "423"}
        ]