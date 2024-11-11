from aiogram.filters import Filter
from aiogram.types import Message
from configs import BotSettings

class AdminFilter(Filter):
    async def __call__(
        self,
        message: Message,
    ) -> bool:
        return message.from_user.id == BotSettings.ADMIN_ID
