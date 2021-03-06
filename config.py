"""
    use file *.config to configure the project
"""
from tornado.options import define, options

define("mongodb_host", default="mongodb://localhost:27017")
define("database_name", default="data")
define("collection_name", default="col")
define("listen_port", default=8888)

options.parse_config_file(r"server.config")
