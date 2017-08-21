import sys
sys.path.insert(0,"/var/www/")

from app.application import ExampleApi

from config import Configuration

cfg = Configuration(debug=True)
ExampleApi(cfg).run(host=cfg.host,port=cfg.port,debug=cfg.debug)
