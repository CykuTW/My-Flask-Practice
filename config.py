DEBUG = True
SECRET_KEY = '<I_AM_SECRET>'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/test-db?charset=utf8mb4"
# <ENGINE>://<USER>:<PASSWORD>@<HOST>/<DB>?charset=<CHARACTER_SET>
SQLALCHEMY_TRACK_MODIFICATIONS = True