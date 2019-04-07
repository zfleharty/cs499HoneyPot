CREATE TABLE connections (
	  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	  date LONGTEXT NOT NULL,
	  protocol LONGTEXT,
	  plugin LONGTEXT,
	  remote_host varchar(20) NOT NULL,
	  remote_port varchar(20) NOT NULL,
	  data LONGTEXT,
	  PRIMARY KEY (time));


