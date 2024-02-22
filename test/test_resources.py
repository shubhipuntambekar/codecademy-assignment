import requests


class TestCat:
    def test_post_cat(self):
        data = {'file': ('test_cat.jpg', open('test_cat.jpg', 'rb'))}
        response = requests.post('http://127.0.0.1:5000/cat', files=data)
        assert response.status_code == 201
        assert 'data' in response.json()
        assert 'message' in response.json()
        assert response.json().get('message') == 'File saved successfully.'

    def test_put_cat(self):
        data = {'file': ('test_cat.jpg', open('test_cat.jpg', 'rb'))}
        response = requests.put('http://127.0.0.1:5000/cat/1', files=data)
        print(response)
        assert response.status_code == 200
        assert 'data' in response.json()
        assert 'message' in response.json()
        assert response.json().get('message') == 'File updated successfully.'

    def test_get_cat(self):
        response = requests.get('http://127.0.0.1:5000/cat/1')
        assert response.status_code == 200

    def test_get_cat_list(self):
        response = requests.get('http://127.0.0.1:5000/cat_list')
        assert 'data' in response.json()
        assert 'message' in response.json()
        assert response.json().get('message') == 'success'

    def test_delete_cat(self):
        response = requests.delete('http://127.0.0.1:5000/cat/1')
        assert response.status_code == 200
        assert 'message' in response.json()
        assert response.json().get('message') == 'Cat image deleted successfully!'


