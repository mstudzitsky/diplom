#!bin/python


import app


if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    bindAddress = ('127.0.0.1', int('9090'))
    WSGIServer(app.myapp, bindAddress= bindAddress).run()
