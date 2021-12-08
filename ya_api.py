import requests
from progress.bar import Bar


class YaApi:
    def __init__(self, token: str):
        self.token = token

    def get_and_upload(self, dir_name, parsed_files):
        self.__create_directory_if_not_exist(dir_name)
        bar = Bar('Processing', check_tty=False, max=len(parsed_files))
        for file_name in parsed_files:
            url = parsed_files[file_name]
            file_bytes = self.__download(url)
            self.__upload(dir_name, file_name, file_bytes)
            bar.next()
        bar.finish()

    @staticmethod
    def __download(url):
        response = requests.get(url)
        return response.content

    def __get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def __get_upload_url(self, dir_name, file_path: str):
        file_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.__get_headers()
        params = {"path": dir_name + "/" + file_path, "overwrite": "true"}
        response = requests.get(url=file_url, params=params, headers=headers)
        return response.json()['href']

    def __upload(self, dir_name, file_name, file_bytes):
        url = self.__get_upload_url(dir_name, file_name)
        response = requests.put(url=url, data=file_bytes)
        return response

    def __create_directory_if_not_exist(self, dir_name: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.__get_headers()
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.get(url=url, params=params, headers=headers)
        response_json = response.json()
        if response.status_code == 404:
            response = requests.put(url=url, params=params, headers=headers)
