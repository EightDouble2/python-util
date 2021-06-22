import generateImagePath
import generateTagsAndCategories


def main(rootpath):
    generateImagePath.main(rootpath)
    generateTagsAndCategories.main(rootpath)


if __name__ == "__main__":
    main("/Users/wuhao02/Nutstore Files/文档/JBlog/content/posts/")
