from app.application import ExampleApi
from config import Configuration

app = None

if __name__ == "__main__":
    cfg = Configuration(debug=True)
    app = ExampleApi(cfg)
    app.run(host=cfg.host,port=cfg.port,debug=cfg.debug)
else:
    cfg = Configuration(debug=False)
    app = ExampleApi(cfg)
