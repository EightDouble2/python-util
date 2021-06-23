# bilibili页面抓取

import requests
import json

base_url = "https://api.bilibili.com/x/space/arc/search"
video_urls = []


def __get_video_urls__(mid):
    ps, count = __get_page_info__(mid)
    for index in range(count // ps + 1):
        __get_video_urls_by_page__(mid, ps, index + 1)
    video_urls.reverse()
    return video_urls


def __get_html_text__(url, params):
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                     'like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'}
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except Exception as e:
            print("{} 获取失败".format(url))


def __get_page_info__(mid):
    params = {'mid': mid, 'order': 'pubdate'}
    page_json = json.loads(__get_html_text__(base_url, params))['data']['page']
    return page_json['ps'], page_json['count']


def __get_video_urls_by_page__(mid, ps, pn):
    params = {'mid': mid, 'ps': ps, 'pn': pn, 'order': 'pubdate'}
    vlist_json = json.loads(__get_html_text__(base_url, params))['data']['list']['vlist']
    for v in vlist_json:
        video_urls.append({'title': v['title'], 'author': v['author'], 'bvid': v['bvid']})
    return video_urls
