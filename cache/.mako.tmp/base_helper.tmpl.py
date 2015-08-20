# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1440064324.276736
_enable_loop = True
_template_filename = u'/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>\n            <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        striphtml = _import_ns.get('striphtml', context.get('striphtml', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer(u"prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer(u'og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer(u'article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            __M_writer(u"'")
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n    <base href="')
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <title>')
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n    <link rel="canonical" href="')
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(unicode(text))
                __M_writer(u' <b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u' <span class="sr-only">')
                        __M_writer(unicode(messages("(active)", lang)))
                        __M_writer(u'</span></a>\n')
                    else:
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                __M_writer(u'            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u' <span class="sr-only">')
                    __M_writer(unicode(messages("(active)", lang)))
                    __M_writer(u'</span></a>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        notes = _mako_get_namespace(context, 'notes')
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer(u'            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">\n')
            else:
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 3, "25": 0, "32": 2, "33": 3, "34": 65, "35": 92, "36": 126, "37": 149, "38": 172, "39": 180, "45": 67, "56": 67, "57": 68, "58": 69, "59": 70, "60": 73, "61": 74, "62": 76, "63": 77, "64": 78, "65": 80, "66": 81, "67": 86, "68": 88, "69": 89, "70": 89, "71": 89, "72": 91, "73": 91, "74": 91, "80": 4, "109": 4, "110": 8, "111": 9, "112": 10, "113": 11, "114": 13, "115": 14, "116": 16, "117": 17, "118": 19, "119": 22, "120": 23, "121": 26, "122": 26, "123": 26, "124": 29, "125": 29, "126": 30, "127": 31, "128": 31, "129": 31, "130": 33, "131": 34, "132": 34, "133": 34, "134": 34, "135": 36, "136": 36, "137": 37, "138": 37, "139": 38, "140": 38, "141": 40, "142": 41, "143": 42, "144": 42, "145": 42, "146": 42, "147": 42, "148": 42, "149": 42, "150": 45, "151": 46, "152": 47, "153": 47, "154": 47, "155": 49, "156": 50, "157": 51, "158": 51, "159": 51, "160": 53, "161": 54, "162": 54, "163": 54, "164": 56, "165": 57, "166": 57, "167": 58, "168": 59, "169": 60, "170": 61, "171": 61, "172": 61, "173": 63, "174": 64, "175": 64, "181": 128, "194": 128, "195": 129, "196": 130, "197": 131, "198": 131, "199": 131, "200": 133, "201": 134, "202": 135, "203": 135, "204": 135, "205": 135, "206": 135, "207": 135, "208": 135, "209": 136, "210": 137, "211": 137, "212": 137, "213": 137, "214": 137, "215": 140, "216": 141, "217": 142, "218": 143, "219": 143, "220": 143, "221": 143, "222": 143, "223": 143, "224": 143, "225": 144, "226": 145, "227": 145, "228": 145, "229": 145, "230": 145, "236": 95, "249": 95, "250": 96, "251": 97, "252": 98, "253": 100, "254": 101, "255": 103, "256": 104, "257": 105, "258": 106, "259": 107, "260": 109, "261": 113, "262": 114, "263": 117, "264": 118, "265": 121, "266": 122, "267": 122, "268": 122, "269": 123, "270": 124, "271": 124, "272": 124, "278": 174, "290": 174, "291": 175, "292": 176, "293": 177, "294": 177, "295": 177, "296": 177, "297": 177, "298": 177, "299": 177, "305": 151, "318": 151, "319": 152, "320": 153, "321": 153, "322": 153, "323": 154, "324": 155, "325": 156, "326": 157, "327": 157, "328": 157, "329": 157, "330": 157, "331": 159, "332": 160, "333": 160, "334": 160, "335": 163, "336": 164, "337": 165, "338": 166, "339": 166, "340": 166, "341": 166, "342": 166, "343": 168, "344": 169, "345": 169, "346": 169, "352": 346}, "uri": "base_helper.tmpl", "filename": "/Volumes/CLE-ROUGE/nikola/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl"}
__M_END_METADATA
"""
