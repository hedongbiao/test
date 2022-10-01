"""
这里作为基类，第一层
"""
import requests
import json

class BaseApi:

    def do_request(self, data:dict):

        # print(json.dumps(data, ensure_ascii=False))


        if "url" in data:
            return self._http_request(data)

    def _http_request(self, data):
        return requests.request(**data)



