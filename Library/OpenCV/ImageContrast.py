import cv2
import time
import numpy as np


# 均值哈希算法
def aHash(img):
    img = cv2.resize(img, (1920, 1080))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    np_mean = np.mean(gray)  # 求numpy.ndarray平均值
    ahash_01 = (gray > np_mean) + 0  # 大于平均值=1，否则=0
    ahash_list = ahash_01.reshape(1, -1)[0].tolist()  # 展平->转成列表
    ahash_str = ''.join([str(x) for x in ahash_list])
    return ahash_str


def pHash(img):
    img = cv2.resize(img, (1920, 1080))  # 默认interpolation=cv2.INTER_CUBIC
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dct = cv2.dct(np.float32(gray))
    dct_roi = dct[0:8, 0:8]  # opencv实现的掩码操作

    avreage = np.mean(dct_roi)
    phash_01 = (dct_roi > avreage) + 0
    phash_list = phash_01.reshape(1, -1)[0].tolist()
    phash_str = ''.join([str(x) for x in phash_list])
    return phash_str


def dHash(img):
    img = cv2.resize(img, (1920, 1080))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    hash_str0 = []
    for i in range(8):
        hash_str0.append(gray[:, i] > gray[:, i + 1])
    hash_str1 = np.array(hash_str0) + 0
    hash_str2 = hash_str1.T
    hash_str3 = hash_str2.reshape(1, -1)[0].tolist()
    dhash_str = ''.join([str(x) for x in hash_str3])
    return dhash_str


def hammingDist(s1, s2):
    assert len(s1) == len(s2)
    return sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])


# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(1920, 1080)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [8192], [0.0, 8192.0])
    hist2 = cv2.calcHist([image2], [0], None, [8192], [0.0, 8192.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def Contrast(image1, image2):
    # 加载图片1
    img1 = cv2.imread(image1)
    # 加载图片2
    img2 = cv2.imread(image2)

    start = time.time()
    ahash_str1 = aHash(img1)
    ahash_str2 = aHash(img2)

    phash_str1 = pHash(img1)
    phash_str2 = pHash(img2)

    dhash_str1 = dHash(img1)
    dhash_str2 = dHash(img2)
    a_score = 1 - hammingDist(ahash_str1, ahash_str2) * 1. / (1920 * 1080 / 4)
    p_score = 1 - hammingDist(phash_str1, phash_str2) * 1. / (1920 * 1080 / 4)
    d_score = 1 - hammingDist(dhash_str1, dhash_str2) * 1. / (1920 * 1080 / 4)

    n = classify_hist_with_split(img1, img2)

    return (a_score + p_score + d_score + n)/4
    # print('三直方图算法相似度：', n)
    # end = time.time()
    # print('a_score:{},p_score:{},d_score{}'.format(a_score, p_score, d_score))
    # print("Total Spend time：", str((end - start) / 60)[0:6] + "分钟")

