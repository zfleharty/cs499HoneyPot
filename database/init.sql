CREATE TABLE connections (
	  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	  date varchar(20) NOT NULL,
	  protocol varchar(40) NOT NULL,
	  plugin LONGTEXT NOT NULL,
	  remote_host varchar(20) NOT NULL,
	  remote_port varchar(20) NOT NULL,
	  data LONGTEXT,
	  PRIMARY KEY (time));


