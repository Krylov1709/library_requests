from urllib import response
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': os.path.join(file_path), 'overwrite': 'true'}
        resp = requests.get(url, headers = headers, params = params).json()
        href = resp['href']
        response = requests.put(href, open(os.path.join(file_path), 'rb'))
        
if __name__ == '__main__':
    path_to_file = "save.txt"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

