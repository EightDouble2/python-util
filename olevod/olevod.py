import getHtml
import getVideo
import re


def __main__(root_url, path, video_root_path):
    video_infos = getHtml.__get_video_infos__(root_url, path)
    getVideo.__get_videos__(video_infos, video_root_path)


if __name__ == "__main__":
    input_url = input("请输入视频地址: ")
    input_root_url = re.findall(r"(.*://.*?)/", input_url)[0]
    input_path = input_url.replace(input_root_url, "")
    default_root_path = "/Users/wuhao02/Downloads"
    input_video_root_path = input("请输入保存地址(默认:{}): ".format(default_root_path))
    if len(input_video_root_path) == 0:
        input_video_root_path = default_root_path
    __main__(input_root_url, input_path, input_video_root_path)
