import pytest
import requests

from page.yandex_page import YaUploader
from page.dog_page import Dogs
from conftest import ya_folder
from config import YaToken

yandex_client = YaUploader()
dogs = Dogs()

"""ТЕСТ
На вход подаются всё породы собак из API Dogs. 
Функция находит одну случайную картинку этой собаки и загружает её на Я.Диск.
Если у породы есть подпороды, то для каждой подпороды загружается по одной картинки.
Например, для doberman будет одна картинка, а для spaniel 7 картинок по одной на каждую подпороду."""


@pytest.mark.regress
@pytest.mark.usefixtures("ya_folder")
@pytest.mark.parametrize('breed', dogs.get_all_breeds())
def test_upload_dog(breed):
    dogs.upload_photos_to_yd(breed)
    url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': f'OAuth {YaToken.token}'}
    response = requests.get(f'{url_create}?path=/test_folder', headers=headers)
    assert response.json()['type'] == "dir"
    assert response.json()['name'] == "test_folder"
    assert True
    if dogs.get_sub_breeds(breed) == []:
        assert len(response.json()['_embedded']['items']) == 1
        for item in response.json()['_embedded']['items']:
            assert item['type'] == 'file'
            assert item['name'].startswith(breed)

    else:
        assert len(response.json()['_embedded']['items']) == len(dogs.get_sub_breeds(breed))
        for item in response.json()['_embedded']['items']:
            assert item['type'] == 'file'
            assert item['name'].startswith(breed)


"""Смоук тест - для одной рандомной породы"""


@pytest.mark.smoke
@pytest.mark.usefixtures("ya_folder")
@pytest.mark.parametrize('breed', [dogs.get_random_breed()])
def test_upload_dog_smoke(breed):
    test_upload_dog(breed)
