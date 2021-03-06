from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import jieba
import argparse

text_url = 'text/一路向北.txt'  # 文件路径
fonts_path = '‪C:/Windows/Fonts/STKAITI.TTF'  # 字体文件
img_path = 'figure/AE86.png'   # 图片路径

ap = argparse.ArgumentParser()
ap.add_argument('-text', default=text_url, help='text path')
ap.add_argument('-font', default=fonts_path, help='font path')
ap.add_argument('-mask', default=img_path, help='mask figure path')
opt = vars(ap.parse_args())
print(opt)


def get_text():  # 获取文本内容
    content = open(opt['text'], 'r', encoding='utf-8').read()
    # 中文分词
    result = jieba.cut(content)  # 精准模式分词
    text = ' '.join(result)
    return text


def GenerateWordCloud(text):    # 生成词云对象
    mask_figure = np.array(Image.open(opt['mask']))
    wc = WordCloud(font_path= opt['font'],
                   max_words=500,   # 显示最大词数
                   scale=10,   # 比例放大，数值越大词云越清晰
                   background_color='white',
                   #mode = 'RGBA',
                   mask = mask_figure
                   ).generate(text=text)
    print('successful generate the wordcloud...')
    return wc


def draw(wordcloud):    # 画图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def saveFile(wordcloud):    # 保存文件
    print('save the figure...')
    wordcloud.to_file('wordcloud.png')
    print('Done.')


if __name__=='__main__':
    text = get_text()
    wc = GenerateWordCloud(text)
    draw(wc)
    saveFile(wc)