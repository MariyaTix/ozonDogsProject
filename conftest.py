import pytest

from page.yandex_page import YaUploader

yandex_client = YaUploader()


@pytest.fixture()
def ya_folder():
    yandex_client.create_folder('test_folder', "y0_AgAAAAAQqhlWAADLWwAAAAEWKNU5AAAFC__2N51K1KdG0ijaVqp2Lh6Mkg")
    yield
    yandex_client.delete_folder('test_folder', "y0_AgAAAAAQqhlWAADLWwAAAAEWKNU5AAAFC__2N51K1KdG0ijaVqp2Lh6Mkg")
