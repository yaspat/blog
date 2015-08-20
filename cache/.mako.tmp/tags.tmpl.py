# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440064325.32056
_enable_loop = True
_template_filename = u'/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/tags.tmpl'
_template_uri = u'tags.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_items = context.get('cat_items', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_items = context.get('cat_items', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        if cat_items:
            if items:
                __M_writer(u'        <h2>')
                __M_writer(unicode(messages("Categories")))
                __M_writer(u'</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer(u'            <ul class="unstyled">\n')
                __M_writer(u'        <li><a class="reference badge" href="')
                __M_writer(unicode(link))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
                if indent_change_after <= 0:
                    __M_writer(u'            </li>\n')
                for i in range(-indent_change_after):
                    __M_writer(u'            </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer(u'                </li>\n')
            if items:
                __M_writer(u'        <h2>')
                __M_writer(unicode(messages("Tags")))
                __M_writer(u'</h2>\n')
        if items:
            __M_writer(u'    <ul class="list-inline">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer(u'            <li><a class="reference badge" href="')
                    __M_writer(unicode(link))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a></li>\n')
            __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"26": 0, "41": 2, "46": 38, "52": 4, "66": 4, "67": 5, "68": 5, "69": 6, "70": 7, "71": 8, "72": 8, "73": 8, "74": 10, "75": 11, "76": 12, "77": 14, "78": 14, "79": 14, "80": 14, "81": 14, "82": 15, "83": 16, "84": 18, "85": 19, "86": 20, "87": 21, "88": 25, "89": 26, "90": 26, "91": 26, "92": 29, "93": 30, "94": 31, "95": 32, "96": 33, "97": 33, "98": 33, "99": 33, "100": 33, "101": 36, "107": 101}, "uri": "tags.tmpl", "filename": "/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/tags.tmpl"}
__M_END_METADATA
"""
