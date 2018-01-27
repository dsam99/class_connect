drop table if exists students;
create table students (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists courses;
create table courses (
  id integer primary key autoincrement,
  title text not null,
  student text not null
);