from bottle import Bottle, run, debug
from apps import settings

debug(settings.DEBUG)

run(settings.APP, host=settings.HOST, port=settings.PORT)