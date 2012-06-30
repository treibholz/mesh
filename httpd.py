#!/usr/bin/python
# -*- coding: utf-8 -*-
#
__revision__ = "0"
#
# simple httpd to run and develop CGIs

import CGIHTTPServer
import BaseHTTPServer
import sys

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]

if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8000

IP="127.0.0.1"

httpd = BaseHTTPServer.HTTPServer((IP, PORT), Handler)
print "Server at: http://%s:%s/cgi/mesh.py" % ( IP, PORT, )

httpd.serve_forever()

# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
