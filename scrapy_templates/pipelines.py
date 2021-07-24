# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from sqlalchemy.orm import sessionmaker
from scrapy_templates.model import db_connect, create_table, Product
from scrapy_templates.config import database_path, product_db_name


class CustomImageNamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name': item["product_name"]})
                for x in [item.get('image_urls')]]

    def file_path(self, request, response=None, info=None, **kwargs):
        return '%s.jpg' % request.meta['image_name']


class CleaningPipeline(object):
    def __init__(self):
        raise NotImplemented

    @staticmethod
    def clean_string(value):
        """Cleaning string fields from unnecessary characters.

        Cleaning double back slashes, new lines, squared brackets, commas.

        Args:
            value: scrapy item
        Returns:
            cleaned: cleaned string value
        """
        cleaned = [line.strip('\n') for line in value]
        cleaned = [line.strip('\\') for line in cleaned]
        cleaned = [line.strip("['") for line in cleaned]
        cleaned = [line.strip("']") for line in cleaned]
        cleaned = [line.strip('","') for line in cleaned]

        return cleaned


class SaveProductPipeline(object):
    def __init__(self):
        engine = db_connect(db_path=database_path, db_name=product_db_name)
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        product = Product()

        product.extraction_date = item['extraction_date']
        product.shop_name = item['shop_name']
        product.id = item['id']
        product.sku = item['sku']
        product.product_name = item['product_name']
        product.price = item['price']
        product.unit = item['unit']
        product.url = item['url']

        try:
            session.add(product)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
