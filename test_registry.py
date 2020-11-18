import pytest
import requests

@pytest.fixture(scope="module")
def server_url():
    return "http://data.threesixtygiving.org/data.json"


def test_api_root(server_url):
    # Download the root of the API
    r = requests.get(server_url)
    # Try to decode it as JSON
    datasets = r.json()
    # Check that the fields we expect have the types we expect
    assert type(datasets) == list
    for dataset in datasets:
        assert type(dataset) == dict
        assert type(dataset['title']) == str
        assert type(dataset['description']) == str
        assert type(dataset['identifier']) == str
        assert type(dataset['can_have_cats']) == str
        assert type(dataset['license_name']) == str
        assert type(dataset['publisher']) == dict
        for key in ['name','website','logo','prefix']:
            assert type(dataset['publisher'][key]) == str
            
        assert type(dataset['distribution']) == list
        for distribution in dataset['distribution']:
            assert type(distribution['downloadURL']) == str
            assert type(distribution['accessURL']) == str
            assert type(distribution['title']) == str
    # Check that identifiers are unique
    assert len(set(dataset['identifier'] for dataset in datasets)) == len(datasets)
