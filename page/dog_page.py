import random
import requests

from config import YaToken
from page.yandex_page import YaUploader


class Dogs:
    def __init__(self):
        pass

    """Получение подпород"""

    def get_sub_breeds(self, breed):
        res = requests.get(f'https://dog.ceo/api/breed/{breed}/list')
        return res.json().get('message', [])

    """Получение url случайных фотографий собак"""

    def get_urls_photos(self, breed, sub_breeds):
        url_images = []
        if sub_breeds:
            for sub_breed in sub_breeds:
                res = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
                sub_breed_urls = res.json().get('message')
                url_images.append(sub_breed_urls)
        else:
            url_images.append(requests.get(f"https://dog.ceo/api/breed/{breed}/images/random").json().get('message'))
        return url_images

    """Загрузка фотографий собак на яндекс диск в папку test_folder"""

    def upload_photos_to_yd(self, breed):
        sub_breeds = self.get_sub_breeds(breed)
        urls = self.get_urls_photos(breed, sub_breeds)
        yandex_client = YaUploader()
        for url in urls:
            part_name = url.split('/')
            name = '_'.join([part_name[-2], part_name[-1]])
            yandex_client.upload_file_to_yd(f"{YaToken.token}",
                                            "test_folder",
                                            url, name)

    """Получение рандомной породы собаки"""

    def get_random_breed(self):
        url = "https://dog.ceo/api/breeds/list/all"
        response = requests.get(url)
        data = response.json()
        breeds = list(data['message'].keys())
        return random.choice(breeds)

    """Получение всех пород собак"""

    def get_all_breeds(self):
        url = "https://dog.ceo/api/breeds/list/all"
        response = requests.get(url)
        data = response.json()
        breeds = list(data['message'].keys())
        return breeds
