--
-- ���� ������������ � ������� SQLiteStudio v3.1.1 � �� ��� 26 15:03:59 2018
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: person
DROP TABLE IF EXISTS buy;
CREATE TABLE buy (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name VARCHAR (32), username VARCHAR (32));
INSERT INTO buy (id, name, username) VALUES (1, 'Phone', 'Kate');
INSERT INTO buy (id, name, username) VALUES (2, 'Bread', 'Kate');
INSERT INTO buy (id, name, username) VALUES (3, 'Bitcoin', 'John');
INSERT INTO buy (id, name, username) VALUES (4, 'One night in paris', 'Admin');
INSERT INTO buy (id, name, username) VALUES (5, 'Debby Does Dallas', 'Admin');
INSERT INTO buy (id, name, username) VALUES (6, 'Otus course', 'Leo');
INSERT INTO buy (id, name, username) VALUES (7, 'Apple', 'Leo');


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
