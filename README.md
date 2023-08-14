# coinex_python_client
coinex.com API wrapper client

## Why?
Coinex.com lacks an official API client SDK, so it took me some time to create an API wrapper. I have shared the code with you, so you don't have to read their documentation to set up a basic API client in Python. If you actively use it, let me know your requirements by creating issues, and I would update the repository.

## Final words
In conclusion, I recommend using CCXT, but there are cases where it is more convenient to directly use the broker's API.

# Example Usage
```python
import time

c = CoinexClient('access_id', 'secret_key')

r = c.request(
    auth=True, # set this to false for public APIs
    endpoint="/order/finished",
    params={
        'start_time': 0,
        'end_time': int(time.time()),
        'page': 1,
        'limit': 100,
    }
)

print(r)
```

