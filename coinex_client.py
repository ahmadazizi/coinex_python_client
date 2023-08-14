import time
import hashlib
import requests

class CoinexClient():
    """coinex.com api client
    repo: https://github.com/ahmadazizi/coinex_python_client
    v: 1.0
    """
    _headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }

    def __init__(self, access_id, secret_key, headers={}):
        self.access_id = access_id
        self.secret_key = secret_key
        self.api_address = 'https://api.coinex.com/v1'
        self._headers.update(headers)
    
    def _get_sign(self, params={}):
        sign_str = '&'.join([key + '=' + str(params[key]) for key in sorted(params)]) + f"&secret_key={self.secret_key}"
        md5 = hashlib.md5(sign_str.encode())
        return md5.hexdigest().upper()
    
    def request(self, endpoint, params={}, data='', auth=True, method="get"):
        url = self.api_address + endpoint
        method = method.upper()
        _headers = {**self._headers}
        if auth:
            params['access_id'] = self.access_id
            params['tonce'] = int(time.time()*1000)
            _headers['Authorization'] = self._get_sign(params)
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=_headers,
                params=params,
                data=data,
            )
            response.raise_for_status()
            response = response.json()
            if response['code'] != 0:
                raise Exception(f"Code: {response['code']}, Message: {response['message']}")
        except requests.exceptions.RequestException as e:
            return False, f"Exception in {method} {endpoint} -> {e}"
        return True, response['data']
