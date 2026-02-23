create database if not exists portafolio;
default character set utf8mb4;
default collage utf8mb4:general_ci;
use portafolio;

create user if not exists 'Juan_MG'@'Localhost' identified by 'p3rs0n4_LpR*y3(T';
grant all privileges on portafolio. * to 'Juan_MG'@'Localhost';

create table if not exists users (
    id_user int primary key not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    email varchar(100) not null unique,
    password_hash varchar(255) not null,
    birthdate date not null
)

create table if not exists contactame (
    id_contact intr primary key not null auto_increment,
    nombre varchar(255) not null,
    email varchar(255) not null,
    mensaje text not null,
    fecha_envio datetime not null default current_timestamp
)