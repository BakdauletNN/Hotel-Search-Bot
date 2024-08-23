from database.models import History


def add(data: dict):
    if data.get("command") in ['low', 'high', 'bestdeal']:
        History.create(
            user_id=data.get('user_id_telegram'),
            command=data.get('command'),
            city=data.get('city'),
            location_id=data.get('id_location'),
            adults_qty=data.get('adults'),
            children=data.get('child_amount', 0),
            entry_date=data.get('entry'),
            exit_date=data.get('exit'),
            hotels_quantity=data.get('hotels_qty', 0),
            photo_qty=data.get('photos', 0),
            min_price=data.get('price_min_bestdeal', 0),
            max_price=data.get('price_max_bestdeal', 0),
            distance_from_center=data.get('center_distance', 0),
            request_date=data.get('request_date')
        )
