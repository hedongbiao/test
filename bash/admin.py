"""
业务层
"""
from shangxue2.bash.base_api import BaseApi
import xlrd

class Admin(BaseApi):

    # 在这里初始化业务，支持输入指定的参数
    def __init__(self, org_code, username, password):
        self.base_url = ""
        self.org_code = org_code
        self.username = username
        self.password = password

    def get_token(self):
        """
        获取token
        :return:
        """
        url = "/login"
        data = {
            "url": f"{self.base_url}{url}",
            "method": "post",
            "data": {
                "orgCode": self.org_code,
                "username": self.username,  # "admin"
                "password": self.password,  # "CD90EE3A79DF4251"
                "platform":"pc"
            }
        }


        # url_log = global_dict.get_value("url_log")
        # Bearer = global_dict.get_value("Bearer")
        # refresh_token = global_dict.get_value("refresh_token")

        resp = self.do_request(data)
        # print(resp)
        return resp

 