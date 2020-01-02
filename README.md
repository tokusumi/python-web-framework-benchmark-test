# performance check of Python web frameworks

# Basic Usage
1. run web server
2. use wrk2
## run web server
see /*/README.md
this repo includes the follows,

- Django 2.X
- Flask
- japronto
- responder
- FastAPI
## use wrk2
### install wrk2
see,
- https://github.com/giltene/wrk2/wiki
### use wrk2
ex) measure responder server
```
$ cd wrk2
$ zsh ./responder.sh
```
if you measure others, call followings,
- Django 2.X: django.sh
- Flask: flask.sh
- japronto: japronto.sh
- responder: responder.sh
- FastAPI: fastapi.sh

# Customize Options
Default options is defined in ```/wrk2/attack.sh```.
They are simple lines of command line for wrk2.
You can change each lines you want, referring to [command line options](https://github.com/wg/wrk#command-line-options)