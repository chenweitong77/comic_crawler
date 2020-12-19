# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-11-22

import re
import requests
import time

import config
from util import PrintLog, HeadersBuilder


class Crawler(object):
    def __init__(self, timeout):
        self.timeout = timeout
        self.headers_builder = HeadersBuilder()

    def download(self, comic_id, output_dir):
        list_page_url = "%s/%s" % (config.base_url, comic_id)
        list_page = self.__html(list_page_url)
        

    def __html(self, url):
        headers = self.headers_builder.build()
        try:
            r = requests.get(url, headers=headers, timeout=self.timeout)
            PrintLog("访问成功：%s" % url)
            if r.status_code == 200:
                return r.text
        except Exception:
            PrintLog("无法访问：%s，请确保网络畅通后重试！" % url)
            return False


if __name__ == '__main__':
    c = Crawler(config.timeout)
    c.download(config.comic_id_dict['火影忍者'], "./")
