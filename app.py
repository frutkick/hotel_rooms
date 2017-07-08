import argparse

from handlers.hotel_rooms_resource import (
    HotelRoomHandler,
    HotelRoomsHandler
)

from handlers.booking_resource import (
    BookingCreateResource,
    BookingUpdateResource
)
from tornado import (
    ioloop,
    web
)


def get_handlers():
    handlers = [
        (r'/rooms', HotelRoomsHandler),
        (r'/rooms/([0-9]+)', HotelRoomHandler),
        (r'/rooms/([0-9]+)/book', BookingCreateResource),
        (r'/rooms/([0-9]+)/book/([0-9]+)', BookingUpdateResource)
    ]
    return handlers


def make_app():
    handlers = get_handlers()
    app = web.Application(handlers)
    return app


def run(host, port):
    app = make_app()
    app.listen(port, host)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('-H', '--host', default='localhost', required=False, help='Host to run app on.')
    args_parser.add_argument('-P', '--port', default=8080, required=False, help='Port to run app on.')
    args = args_parser.parse_args()
    run(args.host, args.port)
