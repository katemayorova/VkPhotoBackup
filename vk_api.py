from datetime import datetime

import requests


class VkApi:
    API_VERSION = "5.131"
    URL = 'https://api.vk.com/method/'
    token: str

    def __init__(self, token):
        self.token = token

    def get_photos(self, vk_screen_name: str, count: int = 1000):
        vk_owner_id = self.__get_user_id(vk_screen_name)
        response_json = self.__get_from_api(vk_owner_id, count)
        parsed_photos = self.__parse_photos(response_json)

        return parsed_photos

    def __get_user_id(self, screen_name):
        utils_url = self.URL + 'utils.resolveScreenName'
        utils_params = {
            'access_token': self.token,
            'v': self.API_VERSION,
            'screen_name': screen_name
        }
        response = requests.get(utils_url, params=utils_params)
        response_json = response.json()
        return response_json['response']['object_id']

    @staticmethod
    def __parse_photos(response_json):
        photos = response_json['response']['items']
        parsed_photo = {}
        for photo in photos:
            name = f'{photo["likes"]["count"]}.jpg'
            if name in parsed_photo:
                date = datetime.utcfromtimestamp(photo['date']).strftime('%Y%m%d')
                name = f'{photo["likes"]["count"]}_{date}.jpg'
            url = max(photo['sizes'], key=lambda key: key['height'])['url']
            parsed_photo[name] = url
        return parsed_photo

    def __get_from_api(self, vk_owner_id: str, count: int):
        photos_url = self.URL + 'photos.get'
        photos_params = {
            'count': count,
            'extended': 1,
            'access_token': self.token,
            'v': self.API_VERSION,
            'album_id': 'profile',
            'owner_id': vk_owner_id,
            'rev': 1
        }
        response = requests.get(photos_url, params=photos_params)
        return response.json()
