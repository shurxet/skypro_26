import pytest
import wsgi


@pytest.fixture()
def test_client():
    app = wsgi.app
    return app.test_client()


keys_should_be = {"id", "poster_name", "poster_avatar", "pic", "content",
                  "views_count", "likes_count", "text_tag", "content_tag"}

class Test:
    def test_api_list(self, test_client):

        response = test_client.get('/api/posts/')
        assert type(response.json) == list, "не список"
        assert set(response.json[0].keys()) == keys_should_be, "не верный ключ"


    def test_api_dict(self, test_client):

        response = test_client.get('/api/posts/1')
        assert type(response.json) == dict, "не словарь"
        assert set(response.json.keys()) == keys_should_be, "не верный ключ"


