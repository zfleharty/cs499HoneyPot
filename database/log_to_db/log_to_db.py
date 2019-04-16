import mysql.connector
import sys
import configparser
from time import sleep

config_file_path = sys.argv[1]
file_path = sys.argv[2]


###################################################
# date = column 0                #                #
# time = column 1                #                #
# [plugin,connection,ip] = column 2             # #
# session or exception= column 3 #                #
# protocol = column 4            #                #
# connect? = column 5            #                #
# local_ip = column 6                             #
# local_port = column 7                           #
# service = column 8                              #
# remote_ip = column 9                            #
# remot_port = column 10                          #
###################################################
def read_log_sessions(path_to_log_file):
    file = open(path_to_log_file,'r')
    sessions = {}
    for line in file:
        line = line.strip()
        columns = line.split()
        if(len(columns) > 10):
            column = {
                "date":"",
                "time":"",
                "plugin":"",
                "protocol":"",
                "remote_host":"",
                "remote_port":"",
                "data":""
            }
            session_key = str(columns[3])
            if(session_key.lower() != "exception:"):
                if session_key in sessions:
                    column = sessions.get(session_key)
                    if(len(column['data']) <= 3):  
                        column['data'] = (str(columns[11]) if (len(columns) >= 12) else column['data']) 
                else:
                    column['date'] = str(columns[0])
                    column['time'] = str(columns[1])
                    column['protocol'] = str(columns[4])
                    column['plugin'] = str(columns[8])
                    column['remote_host'] = str(columns[9])
                    column['remote_port'] = str(columns[10])
                sessions[session_key] = column
                
                    
    return sessions                                                                                                                                                  
                        
def log(cursor,db,session):
    add_ctx = ("INSERT INTO connections"
               "(date, protocol, plugin, remote_host, remote_port, data)"
               "VALUES (%s, %s, %s, %s, %s, %s)")
    date = session['date']
    protocol = session['protocol'] 
    plugin = session['plugin'] 
    remote_host = session['remote_host'] 
    remote_port = session['remote_port'] 
    data = session['data'] 

    ctx_data = (date, protocol, plugin, remote_host, remote_port, data)
    cursor.execute(add_ctx, ctx_data)
    db.commit()

def connect_to_db(config_file_path):
    configparse = configparser.ConfigParser()
    configparse.read(config_file_path)
    config = configparse['mariadb']

    h = str(config['host'])
    u= str(config['user'])
    p = str(config['password'])
    d = str(config['database'])

    db = mysql.connector.connect(user=u,password=p,host=h,database=d)
    cursor = db.cursor()
    return (cursor,db)
    

sessions = read_log_sessions(file_path)
cursor,db = connect_to_db(config_file_path)
print(len(sessions))
      
for session_key in sessions:
    data = sessions.get(session_key)
    log(cursor,db,data)
    sleep(1.)

cursor.close()
db.close()



    
    





    
    



