"""
a server that using restful API to collect information of transform
those data are stored in the mongodb
"""
from tornado.ioloop import IOLoop
from tornado.log import logging
import pymongo
import tornado.web
import handler
import config


class Application(tornado.web.Application):
    """
    the main api server
    """
    def __init__(self):
        handlers = [
            (r"/", handler.MainHandler),
            (r"/api", handler.ApiHandler),
            (r"/api/id/(\d+)", handler.ApiHandler),
            (r"/api/id/(\d+)/name/(\w+)/phone/(\w+)", handler.ApiHandler),
        ]
        client = pymongo.MongoClient(config.options.mongodb_host)
        database = client.get_database(config.options.database_name)
        self.col = database.get_collection(config.options.collection_name)
        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":
    APP = Application()
    if APP.listen(config.options.listen_port):
        logging.info("listening on %s..." % config.options.listen_port)
    IOLoop.instance().start()
