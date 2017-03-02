"""
The handlers to dispose of all routers
"""
from tornado.web import RequestHandler
from tornado.log import logging
from bson.json_util import dumps
from dbmanager import DbManager

class MainHandler(RequestHandler):
    # /
    """
    Handler the router
    """
    def get(self):
        self.write("hello, world")


class ApiHandler(RequestHandler):
    # /Api
    """
    Handler the router
    """
    def prepare(self):
        logging.debug("Enter Api router")

    def get(self, *args, **kwargs):
        cursor = DbManager.find({"id": int(args[0])})
        if cursor.count() > 0:
            self.write(dumps(cursor))
        else:
            self.write("Can't find a person which id is %s"%args[0])

    def post(self, *args, **kwargs):
        if DbManager.insert(int(args[0]), args[1], args[2]):
            logging.debug("insert %s %s %s into the database"%(args[0], args[1], args[2]))
            self.write("Insert successed")
        else:
            logging.debug("Can't insert %s into the database"%(args[0]))
            self.write("Insert failure")

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        result = DbManager.delete_one({"id": args[0]})
        if result:
            self.write(dumps(result))
        else:
            self.write("Can't find a person which id is %s"%args[0])
