from tornado import web
from tornado import gen
from tornado.escape import (
    json_decode,
    json_encode
)

from entities import HotelManager


class HotelsHandler(web.RequestHandler):
    
    keys = ['id', 'name']

    @gen.coroutine
    def get(self):
        all_hotels = yield HotelManager(self.application.db).get_all_hotels()
        result = [dict(zip(self.keys, hotel)) for hotel in all_hotels]
        self.write(json_encode(result))

    @gen.coroutine
    def post(self):
        args = json_decode(self.request.body)
        try:
            hotel_name = args['hotel_name']
        except KeyError:
            raise web.HTTPError(400)
        new_hotel = yield HotelManager(self.application.db).create_hotel(hotel_name)
        self.write(json_encode(dict(zip(self.keys, new_hotel))))


class HotelHandler(web.RequestHandler):
    
    keys = ['id', 'name']
    
    @gen.coroutine
    def get(self, hotel_id):
        hotel = yield HotelManager(self.application.db).get_hotel(hotel_id)
        try:
            result = json_encode(dict(zip(self.keys, hotel)))
            self.write(result)
        except TypeError:
            raise web.HTTPError(404)

    @gen.coroutine
    def put(self, hotel_id):
        args = json_decode(self.request.body)
        new_name = args['hotel_name']
        hotel = yield HotelManager(self.application.db).update_hotel(hotel_id, new_name)
        try:
            result = json_encode(dict(zip(self.keys, hotel)))
            self.write(result)
        except TypeError:
            raise web.HTTPError(404)

    @gen.coroutine
    def delete(self, hotel_id):
        hotel = yield HotelManager(self.application.db).delete_hotel(hotel_id)
        try:
            result = json_encode(dict(zip(self.keys, hotel)))
            self.write(result)
        except TypeError:
            raise web.HTTPError(404)