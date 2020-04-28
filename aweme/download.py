import csv
import os
import uuid

import requests
from tqdm import tqdm
from pyquery import PyQuery as pq

temp_path = 'D:\\PycharmProjects\\TikTok\\aweme\\awemes.csv'


def read_csv():
    with open(temp_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        dict_reader = csv.DictReader(csvfile)
        return [r for r in dict_reader]


def write_csv(rows):
    with open(temp_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=list(rows[0].keys()))
        dict_writer.writeheader()
        dict_writer.writerows(rows)


def downloadd(url, type):
    if len(url) > 0 and 'http' in url:
        path = f'D:/PycharmProjects/TikTok/source/{type}'
        if not os.path.exists(path):
            os.makedirs(path)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        }
        if type == 'music':
            path = f'{path}/{uuid.uuid4().hex}.mp3'
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        if type == 'avatar':
            path = f'{path}/{uuid.uuid4().hex}.png'
            r = requests.get(url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        if type == 'video':
            path = f'{path}/{uuid.uuid4().hex}.mp4'
            r = requests.get(url, headers=headers)
            doc = pq(r.text)
            download_url = doc('video.video-player').attr('src')
            r = requests.get(download_url, headers=headers)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        return path
    else:
        return url


if __name__ == '__main__':
    aweme_list = read_csv()
    if len(aweme_list) > 0:
        for aweme in tqdm(aweme_list):
            # 下载背景音乐
            aweme['MUSIC'] = downloadd(aweme.get('MUSIC'), 'music')
            # 下载作者头像
            aweme['POST_USER_IMAGE'] = downloadd(aweme.get('POST_USER_IMAGE'), 'avatar')
            # 下载短视频
            aweme['AWEME_URL'] = downloadd(aweme.get('AWEME_URL'), 'video')
        write_csv(aweme_list)
