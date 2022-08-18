import sqlite3

con = sqlite3.connect("ladies.db")
cur = con.cursor()

query = """
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS `cats`;
DROP TABLE IF EXISTS `oldladies`;

CREATE TABLE `oldladies` (
  `pk` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` VARCHAR(30)
);


CREATE TABLE `cats` (
  `pk` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `name` VARCHAR(30),
  `owner_pk` INTEGER,  

   FOREIGN KEY (owner_pk) 
   REFERENCES oldladies(pk)
   ON DELETE RESTRICT  -- !Обратите внимание сюда!
);

INSERT INTO `oldladies` VALUES (1, "Dorothy");
INSERT INTO `oldladies` VALUES (2, "Margareth");

INSERT INTO `cats` VALUES (1, "Luna", 1);
INSERT INTO `cats` VALUES (2, "Daisy", 1);
INSERT INTO `cats` VALUES (3, "Bell", 1);

"""

cur.executescript(query)


