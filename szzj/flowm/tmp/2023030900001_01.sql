CREATE TABLE ITOM."ldk_test" (
	NOTICE_ID VARCHAR(32) NOT NULL,
	TITLE VARCHAR(200) DEFAULT NULL,
	IMPORTANT INT DEFAULT 0,
	TOPPED INT DEFAULT 0,
	STATUS INT DEFAULT 0,
	PUBLISH_TIME DATETIME DEFAULT NULL,
	CONTENT TEXT,
	READ_NUM INT DEFAULT 0 NOT NULL,
	AID VARCHAR(32) DEFAULT NULL,
	CREATOR VARCHAR(32) DEFAULT NULL,
	CDATE DATETIME DEFAULT NULL,
	UPDATOR VARCHAR(32) DEFAULT NULL,
	UDATE DATETIME DEFAULT NULL,
	MARK INT DEFAULT 1 NOT NULL,
	PRIMARY KEY (NOTICE_ID)
);

CREATE TABLE ITOM."ldk_test2" (
	ID VARCHAR2(32),
	INSPECTION_TABLE_NAME VARCHAR2(200),
	INSPECTION_PLACE VARCHAR2(20),
	GENERAL_ITEMS VARCHAR2(4000),
	IMPORTANT_ITEMS VARCHAR2(4000),
	OTHER_ITEMS VARCHAR2(2),
	SIGNATURE_SETTING VARCHAR2(50),
	CREATE_TIME TIMESTAMP,
	UPDATE_TIME TIMESTAMP,
	DEL_FLAG NUMBER
);