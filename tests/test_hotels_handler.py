from tornado.testing import (
    AsyncHTTPTestCase,
    gen_test
)
from tornado.escape import (
    json_decode,
    json_encode
)
from tornado import gen
from tornado.httpclient import HTTPRequest
from mock import Mock, patch

from app import make_app, run


def mock_return_value(return_value):
    @gen.coroutine
    def inner(*args, **kwargs):
        yield
        raise gen.Return(return_value)
    return inner


class MyTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()
    
    @patch('entities_managers.base_manager.BaseManager.get_all', mock_return_value([]))
    @gen_test
    def test_hotels_1(self):
        self._app.db = Mock()
        response = yield self.http_client.fetch(self.get_url('/hotels'))
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), [])

    @patch('entities_managers.base_manager.BaseManager.get_all', mock_return_value([(1, 'santa')]))
    @gen_test
    def test_hotels_2(self):
        self._app.db = Mock()
        response = yield self.http_client.fetch(self.get_url('/hotels'))
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), [{'id': 1, 'name': 'santa'}])

    @patch('entities_managers.base_manager.BaseManager.get_one', mock_return_value(None))
    @gen_test
    def test_hotels_3(self):
        self._app.db = Mock()
        try:
            response = yield self.http_client.fetch(self.get_url('/hotels/1'))
        except Exception as e:
            response = e
        self.assertEqual(response.code, 404)

    @patch('entities_managers.base_manager.BaseManager.get_one', mock_return_value((1, 'maria')))
    @gen_test
    def test_hotels_4(self):
        self._app.db = Mock()
        try:
            response = yield self.http_client.fetch(self.get_url('/hotels/1'))
        except Exception as e:
            response = e
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), {'id': 1, 'name': 'maria'})

    @patch('entities_managers.base_manager.BaseManager.update', mock_return_value((1, 'new maria')))
    @gen_test
    def test_hotels_5(self):
        self._app.db = Mock()
        url = self.get_url('/hotels/1')
        request = HTTPRequest(url=url, method='PUT', body=json_encode({'name': 'new maria'}))
        response = yield self.http_client.fetch(request)
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), {'id': 1, 'name': 'new maria'})

    @patch('entities_managers.base_manager.BaseManager.create', mock_return_value((1, 'maria')))
    @gen_test
    def test_hotels_6(self):
        self._app.db = Mock()
        url = self.get_url('/hotels')
        request = HTTPRequest(url=url, method='POST', body=json_encode({'name': 'maria'}))
        response = yield self.http_client.fetch(request)
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), {'id': 1, 'name': 'maria'})

    @gen_test
    def test_hotels_7(self):
        self._app.db = Mock()
        url = self.get_url('/hotels')
        request = HTTPRequest(url=url, method='POST', body=json_encode({'bad_key_name': 'maria'}))
        try:
            response = yield self.http_client.fetch(request)
        except Exception as e:
            response = e
        self.assertEqual(response.code, 400)

    @gen_test
    def test_hotels_8(self):
        self._app.db = Mock()
        url = self.get_url('/hotels/1')
        request = HTTPRequest(url=url, method='PUT', body=json_encode({'bad_key_name': 'maria'}))
        try:
            response = yield self.http_client.fetch(request)
        except Exception as e:
            response = e
        self.assertEqual(response.code, 400)

    @patch('entities_managers.base_manager.BaseManager.delete', mock_return_value((1, 'maria')))
    @gen_test
    def test_hotels_9(self):
        self._app.db = Mock()
        url = self.get_url('/hotels/1')
        request = HTTPRequest(url=url, method='DELETE')
        response = yield self.http_client.fetch(request)
        self.assertEqual(response.code, 200)
        self.assertEqual(json_decode(response.body), {'id': 1, 'name': 'maria'})

