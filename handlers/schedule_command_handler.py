from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler
from vkwave.bots.core.dispatching import filters

from enums.MenuEnum import MenuEnum
from services.ScheduleMenuCreatorService import ScheduleMenuCreatorService
from services.ScheduleService import ScheduleService

router = DefaultRouter()
schedule_menu_creator = ScheduleMenuCreatorService()
schedule = ScheduleService()

menu_schedule_today = MenuEnum.SCHEDULE_TODAY.value
menu_schedule_tomorrow = MenuEnum.SCHEDULE_TOMORROW.value


@simple_bot_message_handler(
    router,
    filters.CommandsFilter(menu_schedule_today.get('payload')) |
    filters.PayloadFilter(menu_schedule_today.get('command'))
)
async def menu(event: SimpleBotEvent):
    return await event.answer(
        message="\n".join([f"{subject.get('name')}: {subject.get('room')}" for subject in schedule.get_schedule_today()]),
        keyboard=schedule_menu_creator.get_menu()
    )


@simple_bot_message_handler(
    router,
    filters.CommandsFilter(menu_schedule_tomorrow.get('payload')) |
    filters.PayloadFilter(menu_schedule_tomorrow.get('command'))
)
async def menu(event: SimpleBotEvent):
    return await event.answer(
        message="\n".join([f"{subject.get('name')}: {subject.get('room')}" for subject in schedule.get_schedule_tomorrow()]),
        keyboard=schedule_menu_creator.get_menu()
    )