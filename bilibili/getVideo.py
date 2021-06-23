# bilibili视频下载

import os

base_url = "https://www.bilibili.com/video"


def __get_videos__(video_infos, root_path):
    for index, video_info in enumerate(video_infos):
        output_dir = "{}/{}/{:0>3}.{}".format(root_path, video_info['author'], index + 1, video_info['title'])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        os.system("you-get "
                  "--output-dir {} "
                  "--playlist {}/{} "
                  "--no-proxy "
                  .format(output_dir, base_url, video_info['bvid']))
