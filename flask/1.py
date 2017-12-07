#!/usr/bin/env python

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        body = """
        remote_ip : {remote_ip}
        <br>
        cookies : {cookies}
        """ .format(
            remote_ip=self.request.remote_ip,
            cookies=self.request.cookies
        )
        self.write(body)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
