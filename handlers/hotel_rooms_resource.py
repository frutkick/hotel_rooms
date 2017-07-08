from tornado import web


class HotelRoomsHandler(web.RequestHandler):

    def get(self):
        self.write('Get all rooms.')


class HotelRoomHandler(web.RequestHandler):

    def get(self, room_number):
        self.write('Get room by number.')
