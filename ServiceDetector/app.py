from connexion.resolver import RestyResolver
import connexion
from services.provider import ItemsProvider
from injector import Binder
from flask_injector import FlaskInjector
from services.cleartext import ClearText
from services.models import Models


def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}, {"Name": "test2"}])
    )
    print('config!!!')
    binder.bind(
        ClearText, 
        ClearText()
    )
    binder.bind(
        Models,
        Models()
    )
    return binder


if __name__ == '__main__':
    # from flup.server.fcgi import WSGIServer
    # print('cu=cu')
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('my_supper_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=9090, host='127.0.0.1', server='tornado')
    # bindAddress = ('127.0.0.1', int('9090'))
    # WSGIServer(app, bindAddress=bindAddress).run()
