import sys
sys.path.insert(0,"/var/www/")

from app.application import ExampleApi

from config import Configuration

cfg = Configuration(debug=False)
app = ExampleApi(cfg)
if __name__ == "__main__":
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)
