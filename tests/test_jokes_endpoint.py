import pytest

from rest_framework.test import APIClient

from jokes.models import Joke


BASE_URL = '/api/v1'


@pytest.fixture
def cli():
    return APIClient()


@pytest.mark.django_db
def test_jokes_create(cli, mocker):
    joke_text = 'había una vez un perro con dos colas'

    res = cli.post(
        f'{BASE_URL}/jokes/',
        {
            'text': joke_text,
        },
        format='json'
    )

    assert res.status_code == 201

    obj = Joke.objects.last()
    assert obj.text == joke_text


@pytest.mark.django_db
def test_jokes_delete(cli, mocker):
    joke_text = 'había una vez un perro con dos colas'
    obj = Joke.objects.create(text=joke_text)

    res = cli.delete(
        f'{BASE_URL}/jokes/{obj.id}/',
        format='json'
    )

    assert res.status_code == 204
    assert Joke.objects.count() == 0
