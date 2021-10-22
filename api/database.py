import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# load env vars
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_name = os.environ['DB_NAME']


engine = create_engine(
    f'postgresql+pg8000://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
)
# Test Database Connection:
#conn = engine.connect()
#print('Connection:' + str(conn))
#conn.close()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
