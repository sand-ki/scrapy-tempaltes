from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Float
from scrapy_templates.config import database_path


Base = declarative_base()


def db_connect(db_name: str, db_path: str = database_path):
    engine_url: str = f"sqlite:///{db_path}/{db_name}"
    return create_engine(engine_url)


def create_table(engine):
    Base.metadata.create_all(engine)


class Product(Base):
    __tablename__ = "products"

    extraction_date = Column(DateTime, primary_key=True)
    shop_name = Column(String)
    id = Column(String, primary_key=True)
    product_name = Column(String)
    price = Column(Float)
    unit = Column(String)
    image_urls = Column(String)
    url = Column(String)
