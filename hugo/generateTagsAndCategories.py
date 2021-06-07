# 生成hugo标签及分类

import os
import re


def main(rootpath):
    find_files(rootpath)


def find_files(rootpath):
    for root, dirs, files in os.walk(rootpath):
        for file in files:
            if os.path.splitext(file)[-1] == ".md":
                filename = os.path.join(root, file)
                tags = [tag.split(".")[-1] for tag in re.sub(rootpath, "", root).split("/")]
                categories = '_'.join(tags)
                generate_tags_and_categories(filename, str(tags), str([categories]))


def generate_tags_and_categories(filename, tags, categories):
    print(filename, tags, categories)
    file = open(filename, mode='r', encoding='utf-8')
    line = []
    for txt in file:
        if re.match("tags: \[.*?]", txt):
            line.extend(["tags: ", tags, '\n'])
        elif re.match("categories: \[.*?]", txt):
            line.extend(["categories: ", categories, '\n'])
        else:
            line.append(txt)

    file = open(filename, mode='w', encoding='utf-8')
    for txt in line:
        file.write(txt)


if __name__ == "__main__":
    main("/Users/wuhao02/Nutstore Files/文档/JBlog/content/posts/")
