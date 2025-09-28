CREATE TABLE Result_file (
    Ano int,
    Rno int,
    name varchar(20),
    sub1 int,
    grade1 varchar(2),
    sub2 int,
    grade2 varchar(2),
    sub3 int,
    grade3 varchar(2),
    sub4 int,
    grade4 varchar(2),
    sub5 int,
    grade5 varchar(2),
    total int,
    avg int,
    division varchar(5)
);

CREATE TABLE Student_file (
    Ano int,
    Rno int,
    class int,
    Section char(1),
    name varchar(20),
    Dob date,
    Mname varchar(20),
    Fname varchar(20),
    phone int,
    Gender char(1),
    StreamCode char(2)
);
