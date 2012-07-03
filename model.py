# -*- coding: utf-8 -*-

import web
import hashlib
import time

db = web.database(dbn='sqlite', db='mesh.db')

def gen_ID(content):
    """docstring for gen_ID"""
    return hashlib.sha1(content).hexdigest()

def get_nodes():
    return db.select('nodes', order='unixtime DESC')

def new_node(content):
    ID          = gen_ID(content)
    unixtime    = int(time.time())

    db.insert('nodes', ID=ID, content=content, unixtime=unixtime)
    return ID

def get_node_by_id(ID):
    try:
        return db.select('nodes', where='ID=$ID', vars=locals())[0]
    except IndexError:
        return None



# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
