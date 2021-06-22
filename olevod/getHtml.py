# olevod页面抓取

import requests
from bs4 import BeautifulSoup
import bs4
import json
import re


def __get_video_infos__(root_url, path):
    video_infos = []
    html = __get_html_text__(root_url + path)
    __fill_video_infos__(video_infos, root_url, html)
    __get_m3u8_url__(video_infos)
    __get_video_url__(video_infos)
    return video_infos


def __get_html_text__(url):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except Exception as e:
            print("{} 获取失败".format(url))


def __fill_video_infos__(video_infos, root_url, html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('h2', attrs={'class': 'title scookie'}).text

    for tag in soup.find('ul', attrs={'class': 'content_playlist list_scroll clearfix'}).children:
        if isinstance(tag, bs4.element.Tag) and tag.name == 'li':
            tag_a = tag('a')[0]
            video_infos.append([title, tag_a.text, root_url + tag_a.attrs['href']])


def __get_m3u8_url__(video_infos):
    for video_info in video_infos:
        video_title = video_info[0]
        video_name = video_info[1]
        html = __get_html_text__(video_info[2])
        soup = BeautifulSoup(html, "html.parser")
        video_url_json = json.loads(re.findall(r".*?({.*?})",
                                               soup.find('div', attrs={'class': 'player_video embed-responsive '
                                                                                'embed-responsive-16by9 '
                                                                                'author-qq362695000 '
                                                                                'clearfix'}).script.string)[0])
        video_info.append(video_url_json['url'])
        print("已找到: {} {}".format(video_title, video_name))


def __get_video_url__(video_infos):
    for video_info in video_infos:
        video_title = video_info[0]
        video_name = video_info[1]
        root_url = video_info[3].replace(video_info[3].split("/")[-1], "")
        html = __get_html_text__(video_info[3])
        html = __get_html_text__(root_url + html.split("\n")[2])

        m4s_ext_x_maps = re.findall(r'#EXT-X-MAP:URI="(.*)"', html)
        video_info.append(root_url + m4s_ext_x_maps[0])

        m4s_extinfs = re.findall(r"#EXTINF:(.*),\n(.*)\n", html)
        m4s_urls = []
        for m4s_extinf in m4s_extinfs:
            m4s_urls.append(root_url + m4s_extinf[1])
        video_info.append(m4s_urls)
        print("正在解析: {} {}".format(video_title, video_name))
