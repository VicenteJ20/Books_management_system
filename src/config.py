class Config:
    SECRET_KEY = 'Vicente#inacap*2021'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'loan_books_management'

class ReturnConfigDB(Config):
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'loan_books_management'

config = {
    'development': DevelopmentConfig
}