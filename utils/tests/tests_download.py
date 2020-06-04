import pytest
import requests
from ..download import DownloadData


@pytest.fixture(autouse=True)
def initialize_download_data_class():
    utils = DownloadData("Pizza")
    return utils


class MockRequestsGet:
    def __init__(self, url=None, params=None, result=None, st_code=200):
        self.result = result
        self.st_code = st_code

    def json(self):
        if self.st_code != 200:
            raise requests.exceptions.HTTPError
        return self.result


results_download = {
    "RESULTS_OK": {
        "page_size": 250,
        "page": 1,
        "count": 276,
        "products": [{"product_name": "product_1"}, {"product_name": "product_2"}]},
    "RESULTS_KEYERROR": {
        "page_size": 250,
        "page": 1,
        "count": 276}
}


def test_download_status_is_ok(monkeypatch, initialize_download_data_class):
    correct_result = [{"product_name": "product_1"}, {"product_name": "product_2"}]

    def mock_response_ok(*args, **kwargs):
        return MockRequestsGet(result=results_download["RESULTS_OK"])

    monkeypatch.setattr('requests.get', mock_response_ok)

    assert initialize_download_data_class.download() == correct_result


def test_download_return_status_not_ok(monkeypatch, initialize_download_data_class, capsys):
    exception_request_stdout = "There is a problem with the OFF servor or your connection"

    def mock_response_not_ok(*args, **kwargs):
        return MockRequestsGet(st_code=400)

    monkeypatch.setattr('requests.get', mock_response_not_ok)

    initialize_download_data_class.download()
    captured = capsys.readouterr()
    assert captured.out == exception_request_stdout


def test_download_with_keyerror_in_result(monkeypatch, initialize_download_data_class, capsys):
    exception_stdout = "There is a problem with the OFF data return"

    def mock_response_keyerror(*args, **kwargs):
        return MockRequestsGet(result=results_download["RESULTS_KEYERROR"])

    monkeypatch.setattr('requests.get', mock_response_keyerror)

    initialize_download_data_class.download()
    captured = capsys.readouterr()
    assert captured.out == exception_stdout
