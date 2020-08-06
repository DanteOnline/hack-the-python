--
-- ���� ������������ � ������� SQLiteStudio v3.1.1 � �� ��� 26 15:03:59 2018
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: person
DROP TABLE IF EXISTS comments;
CREATE TABLE comments (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, name VARCHAR (32), text VARCHAR (32));
INSERT INTO comments (id, name, text) VALUES (1, 'Admin', 'Good Site');
INSERT INTO comments (id, name, text) VALUES (2, 'User', 'Very Safe');
INSERT INTO comments (id, name, text) VALUES (3, 'Leo', 'I am auth person');


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
