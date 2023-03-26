import os
import sys
import urllib.request
import re
from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor, ProxyHandler
from urllib.parse import urljoin

class thief:
    _url = ""
    _root = ""
    _siteurl = ""

    def __init__(self, u, r, user_agent=None):
        self._op = urllib.request.build_opener()
        if user_agent:
            self._op.addheaders = [('User-agent', user_agent)]
        self._url = u
        url_list = u.split('/')
        self._siteurl = url_list[0] + '//' + url_list[2]
        print(self._url)
        if r == None:
            self._root = sys.path[0] + os.path.sep + url_list[2] + os.path.sep
        else:
            self._root = r + os.path.sep
        self.create_dir(self._root, True)

    # 爬取文件 & 建立目录
    def get(self, something):
        something = something.replace(self._siteurl, '')
        if re.search(r"^((https://|http://|//)+)[^\s]+", something) != None:
            return something
        d = self.create_dir(something, False)
        if d[1] != '' and d[1] != None:
            data = self.read(something)
            self.save(data, d[0] + d[1])

            # 判断是否是CSS
            if d[1].split('.').pop() == 'css':
                self.parse_css(something, data)

        return something.replace(self._siteurl, '').strip('/')

    # [返回本地文件夹路径,文件名]
    def create_dir(self, d, is_root):
        if is_root:
            t = d
            f = None
        else:
            t = d.strip('/').split('/')
            f = t.pop()
            f_list = re.findall(r"^(.*?)[\?|\#].*", f)
            if f_list != [] : f = f_list[0]
            t = "/".join(t)
            t = self._root + t.replace('/', os.path.sep)
        if os.path.exists(t) == False:
            os.makedirs(t)
        return [t + os.path.sep, f]

            # 判断是否是CSS
        if d[1].split('.').pop() == 'css':
            self.parse_css(something, data)

        return something.replace(self._siteurl, '').strip('/')

    def read(self, url):
        if url.find(self._siteurl) == -1:
            # 根目录拼接
            if url.find('/') == 0:
                url = self._siteurl + '/' + url
            # 相对路径拼接
            else:
                url = os.path.dirname(self._url) + '/' + url

    def save(self, data, filename):
        if data is not None:
            with open(filename, 'wb') as fp:
                fp.write(data)


    def getroot(self):
        return self._root

    def parse_css(self, url, data):
        #url = urljoin(self._url, url)
        #with self._op.open(url) as f:
        #    data = f.read()

        if data is None:
            data = b''

        t = url.split('/')
        t.pop()
        #url = "/".join(t) + '/'
        #data_str = data.decode('utf-8')
        img = re.findall(r"url\((.*?)\)", '')
        for v in img:
            if v.find('data:') == -1 : self.get(url + v.strip('\''))
