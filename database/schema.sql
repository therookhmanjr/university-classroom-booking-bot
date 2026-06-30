IF DB_ID('UniversityBooking') IS NULL
BEGIN
    CREATE DATABASE UniversityBooking
END
GO

USE UniversityBooking
GO

DROP TABLE IF EXISTS Booking;
DROP TABLE IF EXISTS Schedule;
DROP TABLE IF EXISTS Classrooms;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Buildings;
DROP TABLE IF EXISTS Users;
GO

CREATE TABLE Users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    telegram_id BIGINT NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
        CHECK (role IN ('Admin', 'User'))
);
GO

CREATE TABLE Buildings (
    building_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
GO

CREATE TABLE Classrooms (
    classroom_id INT IDENTITY(1,1) PRIMARY KEY,
    building_id INT NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    FOREIGN KEY (building_id) REFERENCES Buildings(building_id)
);
GO

CREATE TABLE Subjects (
    subject_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);
GO

CREATE TABLE Schedule (
    schedule_id INT IDENTITY(1,1) PRIMARY KEY,

    subject_id INT NOT NULL,
    classroom_id INT NOT NULL,
    teacher_id INT NOT NULL,

    lesson_date DATE NOT NULL,

    start_time TIME NOT NULL,
    end_time TIME NOT NULL,

    group_name VARCHAR(20) NOT NULL,

    CONSTRAINT FK_Schedule_Subjects
        FOREIGN KEY (subject_id)
        REFERENCES Subjects(subject_id),

    CONSTRAINT FK_Schedule_Classrooms
        FOREIGN KEY (classroom_id)
        REFERENCES Classrooms(classroom_id),

    CONSTRAINT FK_Schedule_Users
        FOREIGN KEY (teacher_id)
        REFERENCES Users(user_id),

    CONSTRAINT CHK_Schedule_Time
        CHECK (start_time < end_time)
);
GO

CREATE TABLE Booking (
    booking_id INT IDENTITY(1,1) PRIMARY KEY,

    classroom_id INT NOT NULL,
    user_id INT NOT NULL,

    booking_date DATE NOT NULL,

    start_time TIME NOT NULL,
    end_time TIME NOT NULL,

    purpose VARCHAR(100) NOT NULL,

    status VARCHAR(20) NOT NULL
        CHECK(status IN (
            'Pending',
            'Approved',
            'Rejected',
            'Cancelled'
        )),

    CONSTRAINT FK_Booking_Classrooms
        FOREIGN KEY (classroom_id)
        REFERENCES Classrooms(classroom_id),

    CONSTRAINT FK_Booking_Users
        FOREIGN KEY (user_id)
        REFERENCES Users(user_id),

    CONSTRAINT CHK_Booking_TIME
        CHECK (start_time < end_time)
);
GO









