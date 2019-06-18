#!bin/python

def myapp(environ, start_response):
    print('ddfdfdfd')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!\n']

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    bindAddress = ('127.0.0.1', int('9090'))
    WSGIServer(myapp, bindAddress=bindAddress).run()
