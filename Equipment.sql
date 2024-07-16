CREATE TABLE "Equipment" (
	"UID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Stationary"	INTEGER NOT NULL,
	PRIMARY KEY("UID")
	CHECK("Stationary" >= 0 & "Stationary" <= 1) 
)