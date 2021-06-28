import generateImagePath
import generateTagsAndCategories
import sys


def main():
    generateImagePath.main(rootpath)
    generateTagsAndCategories.main(rootpath)


if __name__ == "__main__":
    rootpath = sys.argv[1]
    main()
