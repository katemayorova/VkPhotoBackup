import requests


class VkApi:
    API_VERSION = "5.131"
    URL = 'https://api.vk.com/method/'
    token: str

    def __init__(self, token):
        self.token = token

    def get_photos(self, owner_id: str):
        photos_url = self.URL + 'photos.get'
        photos_params = {
            'count': 1000,
            'extended': 0,
            'access_token': self.token,
            'v': self.API_VERSION,
            'album_id': 'profile'
        }
        response = requests.get(photos_url, params=photos_params)
        return response.json()
