import mysql.connector

class DevelopmentConfig():
    DEBUG = True
    
    #MYSQL_HOST = 'localhost'
    #MYSQL_USER = 'root'
    #MYSQL_PASSWORD = 'password'
    #MYSLQ_DB = 'asignaturasdb'
    
config = {
    'development': DevelopmentConfig
}