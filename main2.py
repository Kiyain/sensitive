from scrapy import cmdline
import uuid
id = str(uuid.uuid4()).replace('-', '')
cmdline.execute("scrapy crawl epoch".format(id).split())
