#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import markdown
import model

urls = (
    '/',                    'Index',
    '/new',                 'New',
    '/reply/(.+)',          'Reply',
    '/node/(.+)',           'Node',
    '/appreciate/(.+)',     'Appreciate',
)

t_globals = {
    'datestr': web.datestr,
    'markdown': markdown.markdown,
}
render = web.template.render('templates', base='base', globals=t_globals)


class Index: # {{{

    form = web.form.Form(
        web.form.Button('Reply'),
        web.form.Button('Appreciate'),
    )


    def GET(self):
        """ Show page """
        form  = self.form()
        nodes = model.get_nodes()
        return render.index(nodes, form)

# }}}

class New: # {{{

    form = web.form.Form(
        web.form.Textarea('content', web.form.notnull,
            rows=5, cols=80,
            description="Node content:", post="markdown"),
        web.form.Button('Create Node'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.new(form)

        ID=model.new_node(form.d.content)

        raise web.seeother('/node/' + ID)

# }}}

class Node: # {{{

    form = web.form.Form(
        web.form.Button('Reply'),
        web.form.Button('Appreciate'),
    )

    def GET(self, ID):
        form = self.form()
        node = model.get_node_by_id(ID)
        if not node:
            raise web.seeother('/404')
        return render.view(node, form)



# }}}

class Reply: # {{{

    form = web.form.Form(
        web.form.Textarea('content', web.form.notnull,
            rows=5, cols=80,
            description="Node content:", post="markdown"),
        web.form.Button('Create Node'),
    )

    def GET(self, Reference):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()

        if not form.validates():
            return render.new(form)

        ID=model.new_node(form.d.content)

        raise web.seeother('/node/' + ID)

# }}}

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()



# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
