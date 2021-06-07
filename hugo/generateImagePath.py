# 生成hugo图片路径

import os
import re


def main(rootpath):
    find_files(rootpath)


def find_files(rootpath):
    for root, dirs, files in os.walk(rootpath):
        for file in files:
            if os.path.splitext(file)[-1] == ".md":
                generate_image_path(os.path.join(root, file))


def generate_image_path(filename):
    print(filename)
    file = open(filename, mode='r', encoding='utf-8')
    line = []
    for txt in file:
        if re.match("!\[]\(/image/.*?\.png\)", txt):
            line = line[0: -1]
        else:
            if re.match("!\[]\((\.\./)*static/image/.*?\.png\)", txt):
                line.extend([re.sub("(\.\./)*static/image/", "/image/", txt), '\n'])
            line.append(txt)

    file = open(filename, mode='w', encoding='utf-8')
    for txt in line:
        file.write(txt)


if __name__ == "__main__":
    main("/Users/wuhao02/Nutstore Files/文档/JBlog/content/posts/")
