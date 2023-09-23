from database import database


async def launcher_database():
    await database.db_start()
