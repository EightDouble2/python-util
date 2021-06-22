import getHtml
import getVideo
import re
import sys


def __main__(root_url, path, video_root_path):
    video_infos = getHtml.__get_video_infos__(root_url, path)
    getVideo.__get_videos__(video_infos, video_root_path)


if __name__ == "__main__":
    input_url = sys.argv[1]
    input_video_root_path = sys.argv[2]
    input_root_url = re.findall(r"(.*://.*?)/", input_url)[0]
    input_path = input_url.replace(input_root_url, "")
    __main__(input_root_url, input_path, input_video_root_path)
