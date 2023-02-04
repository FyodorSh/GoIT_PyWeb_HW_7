import configparser
import pathlib

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
host = config.get('DB', 'host')
port = config.get('DB', 'port')

url_to_db = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

print(url_to_db)

engine = create_engine(url_to_db, echo=True, pool_size=5)
# if not database_exists(engine.url):
#     create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()
