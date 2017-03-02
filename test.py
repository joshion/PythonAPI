from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Condition

condition = Condition()

@gen.coroutine
def waiter():
    print("I'll wait right here")
    yield condition.wait()
    print("I'm done waiting")

@gen.coroutine
def notifier():
    print("About to notify")
    condition.notify()
    print("Done notifying")

@gen.coroutine
def runner():
    yield[waiter(), notifier()]

IOLoop.current().run_sync(runner)