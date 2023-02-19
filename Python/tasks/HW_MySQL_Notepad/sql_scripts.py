DB_HOST = "localhost"
DB_USER = 'root'
DB_PASSWORD = '!Wot199123'
DB_NAME = 'HW_NOTEPAD'

CREATE_DB = "CREATE DATABASE IF NOT EXISTS `HW_NOTEPAD`"
CREATE_TABLE_USER = "CREATE TABLE IF NOT EXISTS `user` (id INT AUTO_INCREMENT KEY, name VARCHAR(255), surname VARCHAR(255), login VARCHAR(100), password VARCHAR(100));"
CREATE_TABLE_NOTE = "CREATE TABLE IF NOT EXISTS `note` (id INT AUTO_INCREMENT KEY, user_id INT, note VARCHAR(255), date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES user(id));"
INSERT_INTO_USER = "INSERT INTO `user`(`name`,`surname`, `login`, `password`) VALUES ('{}','{}','{}','{}')"
INSERT_INTO_NOTE = "INSERT INTO `note`(`user_id`,`note`) VALUES ('{}','{}')"
DELETE_NOTE = "DELETE FROM `note` WHERE id = '{}' and user_id = '{}';"
IS_NOTE_EXISTS = "SELECT EXISTS(SELECT id FROM note WHERE id = '{}' AND user_id = '{}')"
UPDATE_NOTE = "UPDATE note SET `note` = '{}' WHERE id = '{}' AND user_id = '{}';"
SELECT_NOTE_BY_ID = "SELECT * FROM note WHERE id = '{}' and user_id = '{}';"
SELECT_ALL_NOTES = "SELECT * FROM note WHERE user_id = '{}';"
SELECT_ALL_NOTES_BY_DATE = "SELECT * FROM note WHERE date BETWEEN '{} 00:00:01' AND '{} 23:59:59' AND user_id = '{}';"
SELECT_ALL_BY_INCLUDE_WORD = "SELECT * FROM note WHERE `note` LIKE '%{}%' AND user_id = '{}';"
