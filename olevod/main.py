import getHtml
import getVideo
import re


def __main__(root_url, path, video_root_path):
    video_infos = []
    html = getHtml.__get_html_text__(root_url + path)
    getHtml.__fill_video_infos__(video_infos, root_url, html)
    getHtml.__get_m3u8_url__(video_infos)
    getHtml.__get_video_url__(video_infos)
    getVideo.__get_video__(video_infos, video_root_path)


if __name__ == "__main__":
    input_url = input("请输入视频地址: ")
    input_root_url = re.findall(r"(.*://.*?)/", input_url)[0]
    input_path = input_url.replace(input_root_url, "")
    default_root_path = "/Users/wuhao02/Downloads"
    input_video_root_path = input("请输入保存地址(默认:{}): ".format(default_root_path))
    if len(input_video_root_path) == 0:
        input_video_root_path = default_root_path
    __main__(input_root_url, input_path, input_video_root_path)
