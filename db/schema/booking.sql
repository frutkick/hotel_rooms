CREATE TABLE booking (
    id serial PRIMARY KEY NOT NULL,
    room_id integer NOT NULL,
    guest_name varchar NOT NULL,
    UNIQUE (room_id),
    FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE RESTRICT
);
