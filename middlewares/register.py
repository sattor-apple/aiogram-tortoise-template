from aiogram import BaseMiddleware
from aiogram.types import Update
from database.models import User
from typing import Callable, Awaitable, Dict, Any


class Register(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        if event.message:
            user_id = event.message.from_user.id
            chat_type = event.message.chat.type
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
            chat_type = event.callback_query.message.chat.type
        else:
            return await handler(event, data)

        await User.get_or_create(
            user_id=user_id,
            defaults=dict(
                chat_type=chat_type,
            )
        )

        return await handler(event, data)
