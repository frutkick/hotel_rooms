from tornado import gen


class HotelManager(object):
    
    def __init__(self, db_client):
        self.db_client = db_client
    
    @gen.coroutine
    def create_hotel(self, hotel_name):
        query = """
            INSERT INTO hotels (name) VALUES (%s) RETURNING id, name;
        """
        conn = self.db_client.execute(query, (hotel_name,))
        yield conn
        cursor = conn.result()
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def get_all_hotels(self):
        query = """
            SELECT * FROM hotels;
        """
        conn = self.db_client.execute(query)
        yield conn
        cursor = conn.result()
        raise gen.Return(cursor.fetchall())

    @gen.coroutine
    def get_hotel(self, hotel_id):
        query = """
            SELECT * FROM hotels where id=%s;
        """
        conn = self.db_client.execute(query, (hotel_id,))
        yield conn
        cursor = conn.result()
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def update_hotel(self, hotel_id, new_name):
        query = """
            UPDATE hotels SET name=%s WHERE id=%s RETURNING id, name;
        """
        conn = self.db_client.execute(query, (new_name, hotel_id))
        yield conn
        cursor = conn.result()
        raise gen.Return(cursor.fetchone())

    @gen.coroutine
    def delete_hotel(self, hotel_id):
        query = """
            DELETE FROM hotels WHERE id=%s RETURNING id, name;
        """
        conn = self.db_client.execute(query, (hotel_id,))
        yield conn
        cursor = conn.result()
        raise gen.Return(cursor.fetchone())
