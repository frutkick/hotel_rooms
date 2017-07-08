from entities_managers.base_manager import BaseManager


class RoomManager(BaseManager):
    
    queries_map = {
        'get_all': """SELECT * FROM rooms WHERE hotel_id=%s;""",
        'create': """INSERT INTO rooms (hotel_id, room_number, floor_number) VALUES (%s, %s, %s) RETURNING *;""",
        'get_one': """SELECT * FROM rooms WHERE id=%s;""",
        'update': """UPDATE rooms SET room_number=%s, floor_number=%s WHERE id=%s RETURNING *;""",
        'delete': """DELETE FROM rooms WHERE id=%s RETURNING *;"""
    }
