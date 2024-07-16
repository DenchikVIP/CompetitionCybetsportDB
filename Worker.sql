CREATE TABLE "Worker" (
	"UID"	INTEGER NOT NULL UNIQUE,
	"FIO"	TEXT NOT NULL,
	"Phone number"	TEXT NOT NULL,
	"Assignment 1"	TEXT NOT NULL,
	"Assignment 2"	TEXT,
	"Assignment 3"	TEXT,
	PRIMARY KEY("UID")
)