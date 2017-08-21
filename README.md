# flask-example-app
Flask REST API example app

## Dividing app into modules
[Flask Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)

## Requests
[Requests variables](http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules)

## Responses
[Custom response class](https://blog.miguelgrinberg.com/post/customizing-the-flask-response-class)

## App
### Simple controller
Example of a [simple controller](./app/script_magic)

### Controllers as a class
Controller as a [class](./app/class_module), it simplifies IoC.

### Custom errors
Example declaring [custom errors](./app/errors), declaring exception classes

### Custom responses
Example [custom response](./app/responses)


# Docker
## Why a docker

## Building container
$ docker build -t flask-example-app .

## Runing container
$ docker run -it flask-example-app
# debug

# Apache
## Configuration
[Full tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
