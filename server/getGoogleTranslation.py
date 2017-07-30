import sys
import re
import urllib2
import urllib
import HTMLParser

agent = {'User-Agent':
"Mozilla/4.0 (\
compatible;\
MSIE 6.0;\
Windows NT 5.1;\
SV1;\
.NET CLR 1.1.4322;\
.NET CLR 2.0.50727;\
.NET CLR 3.0.04506.30\
)"}

def unescape(text):
    parser = HTMLParser.HTMLParser()
    return (parser.unescape(text))

def translate(to_translate, to_language="auto", from_language="auto"):
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"

    to_translate = urllib.quote_plus(to_translate)
    link = base_link % (to_language, from_language, to_translate)
    request = urllib2.Request(link, headers=agent)
    raw_data = urllib2.urlopen(request).read()

    data = raw_data.decode("utf-8")
    expr = r'class="t0">(.*?)<'
    re_result = re.findall(expr, data)
    if (len(re_result) == 0):
        result = ""
    else:
        result = unescape(re_result[0])
    return str(result)