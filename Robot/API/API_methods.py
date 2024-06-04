import requests
from requests.auth import HTTPBasicAuth
import json
import jsonpath


class api_method():

    def api_get_method(self, req_url, headers):
        response = requests.get(req_url)
        if response.status_code == 200:
            res = json.loads(response.text)
            data_res = jsonpath.jsonpath(res, 'data')
            return data_res

    def api_post_method(self, req_url, payload_file):
        f = open(payload_file, 'r')
        payload = f.read()
        json_payload = json.dumps(payload)
        response = requests.post(url=req_url, json=json_payload)
        if response.status_code==201:
            json_response = json.loads(response.text)
            return json_response

    def api_delete_method(self, req_url):
        response = requests.delete(req_url)
        if response.status_code ==204:
            return True
        else:
            return False

    def api_patch_method(self, req_url, payload_file):
        f = open(payload_file, 'r')
        payload = f.read()
        json_payload = json.loads(payload)
        response = requests.patch(req_url, json=json_payload)
        if response.status_code == 200:
            json_response = json.loads(response.text)
            return json_response
