from peewee import Model, CharField, IntegerField, TextField, DateTimeField, FloatField, SqliteDatabase


sqlite_db = SqliteDatabase('database/tg_bot.db', pragmas={'journal_mode': "wal", 'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class History(BaseModel):
    user_id = IntegerField()
    command = CharField()
    city = CharField()
    location_id = IntegerField()
    adults_qty = IntegerField()
    children = IntegerField()
    entry_date = CharField()
    exit_date = CharField()
    hotels_quantity = IntegerField()
    photo_qty = IntegerField(default=0)
    min_price = IntegerField(null=True)
    max_price = IntegerField(null=True)
    distance_from_center = IntegerField(null=True)
    request_date = DateTimeField()


sqlite_db.create_tables([History])


