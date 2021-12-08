import os

from vk_api import VkApi
from ya_api import YaApi

if __name__ == '__main__':
    vk_owner_id = "begemot_korovin"
    vk_token = os.getenv("VK_TOKEN")
    vk_api = VkApi(vk_token)
    photo_count = 5
    parsed_photos = vk_api.get_photos(vk_owner_id, photo_count)

    ya_token = os.getenv("YA_TOKEN")
    ya_api = YaApi(ya_token)
    ya_api.get_and_upload("photos", parsed_photos)
