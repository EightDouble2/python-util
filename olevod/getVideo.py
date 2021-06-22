# olevod视频下载

import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def __get_videos__(video_infos, video_root_path):
    for index, video_info in enumerate(video_infos):
        video_title = video_info[0]
        video_name = "{:0>3}.{}.mp4".format(index + 1, video_info[1])
        video_path = "{}/{}".format(video_root_path, video_info[0])
        m4s_root_url = video_info[4]
        m4s_urls = video_info[5]
        m4s_total = len(m4s_urls)

        if not os.path.exists(video_path):
            os.makedirs(video_path)

        video_path_name = "{}/{}".format(video_path, video_name)
        if not os.path.exists(video_path_name):
            __get_m4ss__(video_title, video_name, m4s_urls, m4s_total, video_path_name)
            __get_m4s_root__(video_title, video_name, m4s_root_url, video_path_name)
            __merge_video__(video_title, video_name, m4s_total, video_path_name)
            __clear_m4s__(video_title, video_name, m4s_total, video_path_name)

        print("已完成: {} {}".format(video_title, video_name))


def __get_m4ss__(video_title, video_name, m4s_urls, m4s_total, video_path_name):
    schedule = ["□"] * m4s_total
    print("正在下载: {} {} {} {} / {}".format(video_title, video_name, "".join(schedule), 0, m4s_total), end="")
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = []
        for m4s_index, m4s_url in enumerate(m4s_urls):
            m4s_path_name = "{}-{}".format(video_path_name, m4s_index + 1)
            if not os.path.exists(m4s_path_name):
                thread = pool.submit(__get_m4s__, video_title, video_name, m4s_index, m4s_url, m4s_total, m4s_path_name)
                futures.append(thread)

        for future in as_completed(futures):
            schedule[future.result()] = "■"
            print("\r正在下载: {} {} {} {} / {}".format(
                video_title, video_name, "".join(schedule), schedule.count("■"), m4s_total), end="")
    print("\r下载完成: {} {}".format(video_title, video_name))


def __get_m4s__(video_title, video_name, m4s_index, m4s_url, m4s_total, m4s_path_name):
    finish = False
    retry_times = 0
    while not finish:
        try:
            with open(m4s_path_name, "wb+") as file:
                response = requests.get(m4s_url)
                response.raise_for_status()
                file.write(response.content)
            finish = True
        except Exception as e:
            retry_times = retry_times + 1
            print("\r下载失败: {} {} {} / {} 重试第{}次".format(video_title, video_name, m4s_index + 1, m4s_total, retry_times))
    return m4s_index


def __get_m4s_root__(video_title, video_name, m4s_root_url, video_path_name):
    print("正在下载根文件: {} {}".format(video_title, video_name), end="")
    finish = False
    retry_times = 0
    while not finish:
        try:
            with open(video_path_name, "wb+") as file:
                response = requests.get(m4s_root_url)
                response.raise_for_status()
                file.write(response.content)
            finish = True
        except Exception as e:
            retry_times = retry_times + 1
            print("\r根文件下载失败: {} {} 重试第{}次".format(video_title, video_name, retry_times))
    print("\r根文件下载完成: {} {}".format(video_title, video_name))


def __merge_video__(video_title, video_name, m4s_total, video_path_name):
    print("正在合并: {} {}".format(video_title, video_name), end="")
    with open(video_path_name, "ab+") as file:
        for m4s_index in range(m4s_total):
            with open("{}-{}".format(video_path_name, m4s_index + 1), "rb") as m4s_file:
                file.write(m4s_file.read())
    print("\r合并完成: {} {}".format(video_title, video_name))


def __clear_m4s__(video_title, video_name, m4s_total, video_path_name):
    print("正在清理缓存: {} {}".format(video_title, video_name), end="")
    for m4s_index in range(m4s_total):
        os.remove("{}-{}".format(video_path_name, m4s_index + 1))
    print("\r缓存清理完成: {} {}".format(video_title, video_name))
