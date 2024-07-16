CREATE TABLE "Material" (
	"UID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Cost by unit"	INTEGER NOT NULL,
	"Unit of measurment"	TEXT NOT NULL,
	PRIMARY KEY("UID")
)