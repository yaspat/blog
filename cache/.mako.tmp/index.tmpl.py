# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440064324.590216
_enable_loop = True
_template_filename = u'/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer(u'\n<div class="postindex">\n')
        for post in posts:
            __M_writer(u'    <article class="h-entry post-')
            __M_writer(unicode(post.meta('type')))
            __M_writer(u'">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">')
            __M_writer(unicode(post.author()))
            __M_writer(u'</span></p>\n            <p class="dateline"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.formatted_date('webiso')))
            __M_writer(u'" title="')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer(u'                <p class="commentline">')
                __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer(u'\n')
            __M_writer(u'        </div>\n    </header>\n')
            if index_teasers:
                __M_writer(u'    <div class="p-summary entry-summary">\n    ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'    <div class="e-content entry-content">\n    ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'    </div>\n    </article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer(u'        <link rel="prefetch" href="')
            __M_writer(unicode(posts[0].permalink()))
            __M_writer(u'" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"133": 6, "143": 6, "144": 7, "145": 7, "146": 8, "147": 9, "148": 9, "149": 9, "22": 3, "25": 2, "155": 14, "31": 0, "166": 155, "51": 2, "52": 3, "53": 4, "58": 11, "63": 42, "69": 13, "83": 13, "88": 14, "89": 16, "90": 17, "91": 17, "92": 17, "93": 19, "94": 19, "95": 19, "96": 19, "97": 21, "98": 21, "99": 22, "100": 22, "101": 22, "102": 22, "103": 22, "104": 22, "105": 22, "106": 22, "107": 23, "108": 24, "109": 24, "110": 24, "111": 26, "112": 28, "113": 29, "114": 30, "115": 30, "116": 31, "117": 32, "118": 33, "119": 33, "120": 35, "121": 38, "122": 39, "123": 39, "124": 40, "125": 40, "126": 41, "127": 41}, "uri": "index.tmpl", "filename": "/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
