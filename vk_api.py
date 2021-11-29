from datetime import datetime

import requests


class VkApi:
    API_VERSION = "5.131"
    URL = 'https://api.vk.com/method/'
    token: str

    def __init__(self, token):
        self.token = token

    def get_photos(self, owner_id: str):
        response_json = self.__get_from_api()
        parsed_photo = self.__parse_photos(response_json)

        return parsed_photo

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

    def __get_from_api(self):
        photos_url = self.URL + 'photos.get'
        photos_params = {
            'count': 1000,
            'extended': 1,
            'access_token': self.token,
            'v': self.API_VERSION,
            'album_id': 'profile'
        }
        response = requests.get(photos_url, params=photos_params)
        return response.json()
