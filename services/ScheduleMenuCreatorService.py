from vkwave.bots import Keyboard, ButtonColor
from enums.MenuEnum import MenuEnum


class ScheduleMenuCreatorService:

    def get_menu(self) -> Keyboard:
        menu_kayboard = Keyboard()
        menu_schedule_today = MenuEnum.SCHEDULE_TODAY.value
        menu_schedule_tomorrow = MenuEnum.SCHEDULE_TOMORROW.value
        
        menu_kayboard.add_text_button(text=menu_schedule_today.get('name'), payload=menu_schedule_today.get('command'), color=ButtonColor.POSITIVE)
        menu_kayboard.add_row()
        menu_kayboard.add_text_button(text=menu_schedule_tomorrow.get('name'), payload=menu_schedule_tomorrow.get('command'), color=ButtonColor.NEGATIVE)

        return menu_kayboard.get_keyboard()