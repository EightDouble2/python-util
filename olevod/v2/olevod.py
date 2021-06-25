import getHtml
import re
import sys


def __main__():
    video_infos = getHtml.__get_video_infos__(root_url, path)
    print(video_infos[0][0])
    for video_info in video_infos:
        print(video_info[3])
    for index, video_info in enumerate(video_infos):
        print('mv {:0>3}* "{:0>3}.{}.mp4"'.format(index + 1, index + 1, video_info[1]))


if __name__ == "__main__":
    input_url = sys.argv[1]
    root_url = re.findall(r"(.*://.*?)/", input_url)[0]
    path = input_url.replace(root_url, "")
    __main__()
