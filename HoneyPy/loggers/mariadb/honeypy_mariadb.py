import mysql.connector


# TABLES = {}
# TABLES['connections'] = (
#     "CREATE TABLE `connections` ("
#     "  `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
#     "  `date` varchar(20) NOT NULL,"
#     "  `protocol` varchar(40) NOT NULL,"
#     "  `plugin` varchar(20) NOT NULL,"
#     "  `remote_host` varchar(20) NOT NULL,"
#     "  `remote_port` varchar(20) NOT NULL,"
#     "  `data` LONGTEXT,"
#     "  PRIMARY KEY (`time`)"
#     ") ENGINE=InnoDB")
#

# db = mysql.connector.connect(**config)
# cursor = db.cursor()
#
# for table_name in TABLES:
#         table_description = TABLES[table_name]
#         try:
#                 cursor.execute(table_description)
#         except mysql.connector.Error as err:
#                 if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                         print("already exists.")
#                 else:
#                         print(err.msg)
#         else:
#                 print("OK")


# TCP
#       parts[0]: date
#       parts[1]: time_parts
#       parts[2]: plugin
#       parts[3]: session
#       parts[4]: protocol
#       parts[5]: event
#       parts[6]: local_host
#       parts[7]: local_port
#       parts[8]: service
#       parts[9]: remote_host
#       parts[10]: remote_port
#       parts[11]: data
# UDP
#       parts[0]: date
#       parts[1]: time_parts
#       parts[2]: plugin string part
#       parts[3]: plugin string part
#       parts[4]: session
#       parts[5]: protocol
#       parts[6]: event
#       parts[7]: local_host
#       parts[8]: local_port
#       parts[9]: service
#       parts[10]: remote_host
#       parts[11]: remote_port
#       parts[12]: data
def process(config, section, parts, time_parts):
    db = mysql.connector.connect(user=config.get(section, 'user'), password=config.get(section, 'password'),
                                 host=config.get(section, 'host'), database=config.get(section, 'database'))
    cursor = db.cursor()

    if parts[4] == 'TCP':
        if len(parts) == 11:
            parts.append('EMPTYDATA')  # No data recieved
        log(db, cursor, parts[0], parts[4], parts[2], parts[9], parts[10], parts[11])
    else:
        # UDP splits differently (see comment section above)
        if len(parts) == 12:
            parts.append('EMPTYDATA')  # no data sent
        log(db, cursor, parts[0], parts[5], parts[2], parts[10], parts[11], parts[12])
    cursor.close()
    db.close()


def log(db, cursor, date, protocol, plugin, remote_host, remote_port, data):
    add_ctx = ("INSERT INTO connections"
               "(date, protocol, plugin, remote_host, remote_port, data)"
               "VALUES (%s, %s, %s, %s, %s, %s)")
    ctx_data = (date, protocol, plugin, remote_host, remote_port, data)
    cursor.execute(add_ctx, ctx_data)
    db.commit()
