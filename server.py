"""
a server that using restful API to collect information of transform
those data are stored in the mongodb
"""
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.log import logging
import handler


def make_app():
    """
    the main api server
    """
    return Application([
        (r"/", handler.MainHandler),
        (r"/api", handler.ApiHandler),
        (r"/api/id/(\d+)", handler.ApiHandler),
        (r"/api/id/(\d+)/name/(\w+)/phone/(\w+)", handler.ApiHandler),
    ])


if __name__ == "__main__":
    APP = make_app()
    if APP.listen(8888):
        logging.info("listening on 8888...")
    IOLoop.instance().start()
