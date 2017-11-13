USE COP4720;

GO

CREATE SCHEMA FCL2;

GO

CREATE TABLE FCL2.RATE
(
	RT_CODE VARCHAR(20) PRIMARY KEY,
	RT_NAME VARCHAR(20),
	RT_AMT DECIMAL(19,4)
);

CREATE TABLE FCL2.MECHANIC
(
	MECH_ID INT IDENTITY(1,1) PRIMARY KEY,
	MECH_FNAME VARCHAR(20),
	MECH_LNAME VARCHAR(30)
);