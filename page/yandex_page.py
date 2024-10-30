import time
import requests


class YaUploader:
    def __init__(self):
        pass

    """Создание папки на яндекс диске"""

    def create_folder(self, path, token):
        url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        try:
            response = requests.put(f'{url_create}?path={path}', headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при создании папки: {e}")

    """Удаление папки из яндекс диска"""

    def delete_folder(self, path, token):
        url_create = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        try:
            response = requests.delete(f'{url_create}?path={path}', headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при удалении папки: {e}")

    """Загрузка файлов(фотографий) в папку яндекс диска"""

    def upload_file_to_yd(self, token, path, url_file, name):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {"path": f'/{path}/{name}', 'url': url_file, "overwrite": "true"}
        try:
            response = requests.post(url, headers=headers, params=params, timeout=3)
            response.raise_for_status()
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при загрузке файла в папку: {e}")
