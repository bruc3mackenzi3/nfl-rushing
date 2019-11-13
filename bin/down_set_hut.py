#!/usr/bin/env python

import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web

# Add lib folder to path so Python can find these modules
sys.path.append('lib/')
import main_handler
import rushing_data


# workaround for Windows
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

port = 8888

def build_web_app():
    # Load rushing.json
    rush_data = rushing_data.RushingData()

    return tornado.web.Application(
        [(r'/rushing', main_handler.MainHandler, dict(rushing_data=rush_data))],
        static_path='static/')


def main():    
    app = build_web_app()

    # Start web server
    print('Starting up web server!')
    server = tornado.httpserver.HTTPServer(app)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
