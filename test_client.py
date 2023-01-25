import pytest
from client import ClientWrapper

class TestAPI:
  @pytest.mark.vcr
  def test_request(self):
    response  = ClientWrapper().do_request()
    assert response.status_code == 200
