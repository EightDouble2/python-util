import getVideoUrl
import getVideo
import sys


def __main__():
    video_infos = getVideoUrl.__get_video_urls__(mid)
    getVideo.__get_videos__(video_infos, root_path)


if __name__ == "__main__":
    mid = sys.argv[1]
    root_path = sys.argv[2]
    __main__()
