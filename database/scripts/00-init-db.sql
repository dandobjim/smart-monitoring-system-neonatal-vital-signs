create table vital_signs
(
    sensor_id   varchar not null,
    heart_rate  integer,
    id          integer generated always as identity
        constraint id_pk
            primary key,
    timestamp   varchar,
    temperature double precision
);

