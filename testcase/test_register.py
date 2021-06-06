import pytest
from api.register import register
def test_register(base_url):
    print(base_url)
    r = register(base_url,"layzhang19911008")
    print(base_url)
    print(r.url)