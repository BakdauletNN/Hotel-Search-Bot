from peewee import Model, CharField, IntegerField, TextField, DateField, FloatField, SqliteDatabase


sqlite_db = SqliteDatabase('tg_bot.db', pragmas={'journal_mode': "wal", 'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class History(BaseModel):
    user_id = IntegerField()
    command = CharField()
    city = CharField()
    location_id = CharField()
    adults_qty = IntegerField()
    children = TextField()
    entry_date = DateField()
    exit_date = DateField()
    hotels_quantity = IntegerField()
    photo_qty = IntegerField()
    min_price = FloatField(null=True)
    max_price = FloatField(null=True)
    distance_from_center = FloatField(null=True)
    request_date = DateField(null=True)


sqlite_db.create_tables([History])
