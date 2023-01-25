import requests
class ClientWrapper:
  def __init__(self) -> None:
    self._client = APIClient()

  def do_request(self):
    return self._client.request()

class APIClient:
  def request(self):
    return requests.get("http://keithwebber.com/")
