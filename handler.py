"""
The handlers to dispose of all routers
"""
import tornado.web
from tornado.log import logging
from bson.json_util import dumps

class MainHandler(tornado.web.RequestHandler):
    # /
    """
    Handler the router
    """
    def __init__(self, application, request, **kwargs):
        super(MainHandler, self).__init__(application, request)
        self.col = self.application.col

    def get(self):
        self.write("hello, world")


class ApiHandler(tornado.web.RequestHandler):
    # /Api
    """
    Handler the router
    """
    def __init__(self, application, request, **kwargs):
        super(ApiHandler, self).__init__(application, request)
        self.col = self.application.col

    def prepare(self):
        logging.debug("Enter Api router")

    def post(self, *args, **kwargs):
        if self.col.insert_one({'id': args[0], "name":  args[1], "phone":  args[2]}):
            logging.debug("Insert %s %s %s into the database"%(args[0], args[1], args[2]))
            self.write("Insert successed")
        else:
            logging.debug("Can't insert %s into the database"%(args[0]))
            self.write("Insert failure")

    def get(self, *args, **kwargs):
        cursor = self.col.find({"id": int(args[0])})
        if cursor.count() > 0:
            self.write(dumps(cursor))
        else:
            self.write("Can't find a person which id is %s"%args[0])

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        result = self.col.find_one_and_delete(args[0])
        if result:
            self.write(dumps(result))
        else:
            self.write("Can't find a person which id is %s"%args[0])
