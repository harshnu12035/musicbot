async def get_loop(self, chat_id: int) -> int:
    return self.loop.get(chat_id, 0)

async def set_loop(self, chat_id: int, count: int) -> None:
    self.loop[chat_id] = count


async def get_autoplay(self, chat_id: int) -> bool:
    return self.autoplay.get(chat_id, False)

async def set_autoplay(self, chat_id: int, mode: bool) -> None:
    self.autoplay[chat_id] = mode


# AUTH METHODS
async def _get_auth(self, chat_id: int) -> set[int]:
