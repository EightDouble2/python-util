import requests
import os


def __get_video__(video_infos, video_root_path):
    for index, video_info in enumerate(video_infos):
        video_title = video_info[0]
        video_name = "{:0>3}.{}.mp4".format(index + 1, video_info[1])
        video_path = "{}/{}".format(video_root_path, video_info[0])

        if not os.path.exists(video_path):
            os.makedirs(video_path)

        video_path_name = "{}/{}".format(video_path, video_name)
        if not os.path.exists(video_path_name):
            with open(video_path_name, "wb+") as file:
                file.write(requests.get(video_info[4]).content)

            m4s_urls = video_info[5]
            print("正在下载: {} {} {} / {}".format(video_title, video_name, 0, len(m4s_urls)), end="")
            for m4s_index, m4s_url in enumerate(m4s_urls):
                with open(video_path_name, "ab+") as file:
                    file.write(requests.get(m4s_url).content)
                print("\r正在下载: {} {} {} / {}".format(video_title, video_name, m4s_index + 1, len(m4s_urls)), end="")
            print("\r{} {} 下载完成".format(video_title, video_name))
        else:
            print("{} {} 已存在".format(video_title, video_name))
