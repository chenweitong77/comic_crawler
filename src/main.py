# -*- coding:utf-8 -*-
#
# Author: Muyang Chen
# Date: 2020-11-22

import os

import config
from crawler import Crawler

if __name__ == '__main__':
    base_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir))
    data_dir = os.path.join(base_path, 'data')
    output_dir = os.path.join(data_dir, 'comic')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    crawler = Crawler(config.timeout)
    crawler.download(config.comic_id_dict['火影忍者'], output_dir)
