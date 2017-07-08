CREATE TABLE rooms (
    id serial PRIMARY KEY NOT NULL,
    room_number smallint NOT NULL,
    hotel_id integer NOT NULL,
    floor_number smallint NOT NULL,
    UNIQUE (hotel_id, room_number),
    FOREIGN KEY (hotel_id) REFERENCES hotels (id) ON DELETE CASCADE
);
