CREATE TABLE booking (
    room_id integer PRIMARY KEY NOT NULL,
    guest_name varchar NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE RESTRICT
);
