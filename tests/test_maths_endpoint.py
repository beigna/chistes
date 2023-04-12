import pytest

from rest_framework.test import APIClient

BASE_URL = '/api/v1'


@pytest.fixture
def cli():
    return APIClient()


@pytest.mark.parametrize('numbers,result', [
    ([72, 50], 1800),
    ([2, 4, 10], 20),
    ([6, 8], 24)
])
def test_least_common_multiple(cli, mocker, numbers, result):
    res = cli.get(
        f'{BASE_URL}/maths/',
        {
            'numbers': numbers,
        },
        format='json'
    )

    assert res.status_code == 200
    assert res.json() == {'result': result}


@pytest.mark.parametrize('number,result', [(1, 2), (-5, -4), (8, 9)])
def test_number_plus_one(cli, mocker, number, result):
    res = cli.get(
        f'{BASE_URL}/maths/',
        {
            'number': number,
        },
        format='json'
    )

    assert res.status_code == 200
    assert res.json() == {'result': result}


def test_error_two_params(cli, mocker):
    res = cli.get(
        f'{BASE_URL}/maths/',
        {
            'number': 1,
            'numbers': [1, 2, 3],
        },
        format='json'
    )

    assert res.status_code == 500
    assert res.json() == {
        'detail': 'You must send the param number or numbers not both'
    }


def test_error_none_params(cli, mocker):
    res = cli.get(
        f'{BASE_URL}/maths/',
        format='json'
    )

    assert res.status_code == 500
    assert res.json() == {
        'detail': 'You must send the param number or numbers'
    }
