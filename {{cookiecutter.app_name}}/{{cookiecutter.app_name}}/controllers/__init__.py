from .. import app


from .HelloWorld import HelloWorldController
HelloWorldController.register(app, route_base='/')
