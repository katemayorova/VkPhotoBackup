from vk_api import VkApi
import os

if __name__ == '__main__':
    vk_owner_id = "begemot_korovin"
    vk_token = os.getenv("VK_TOKEN")
    vk_api = VkApi(vk_token)
    photo_response = vk_api.get_photos(vk_owner_id)
    print(photo_response)
