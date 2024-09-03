from database.models import History
import logging


def add(data: dict):
    # Добавляем логирование для отслеживания работы функции
    logging.info(f"Attempting to add data to History: {data}")

    # Проверяем, что команда присутствует и она одна из разрешенных
    command = data.get("command")
    if command not in ["low", "high", "bestdeal"]:
        logging.warning(f"Command '{command}' is not valid for adding to History.")
        return

    try:
        # Создаем запись в базе данных
        new_record = History.create(
            user_id=data.get('user_id_telegram'),
            command=command,
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
        logging.info(f"Record added to History successfully: {new_record}")
        return new_record
    except Exception as e:
        # Логируем ошибку, если не удалось создать запись
        logging.error(f"Error adding data to History: {e}")
        raise 'Не удалось подключиться к БД'

