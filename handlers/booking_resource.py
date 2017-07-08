from tornado import web


class BookingCreateResource(web.RequestHandler):

    def post(self, room_number):
        print self.get_body_arguments('guest_name')
        self.write('Book room.')


class BookingUpdateResource(web.RequestHandler):

    def put(self, room_number, booking_id):
        self.write('Update booking')

    def delete(self, room_number, booking_id):
        self.write('Cancel booking')
