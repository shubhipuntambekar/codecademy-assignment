import os

from flask import request, send_file
from flasgger.utils import swag_from

from app.model.cat import Cat, cat_files
from app.resources.base import BaseResource, validate_files


class CatResource(BaseResource):

    @swag_from('api_docs/cat/cat_post.yml')
    @validate_files
    def post(self):
        uploaded_file = request.files.get('file')
        cat = Cat()
        cat_files[cat.id] = cat
        os.makedirs(os.path.dirname(cat.path), exist_ok=True)
        uploaded_file.save(cat.path)
        return self.handle_success(201, cat.id, 'File saved successfully.')

    @swag_from('api_docs/cat/cat_put.yml')
    @validate_files
    def put(self, cat_id):
        cat = cat_files.get(cat_id)
        if not cat:
            return self.handle_error(400, 'Cat image not found!')
        updated_file = request.files.get('file')
        updated_file.save(cat.path)
        return self.handle_success(200, cat.id, 'File updated successfully.')

    @swag_from('api_docs/cat/cat_get.yml')
    def get(self, cat_id):
        cat = cat_files.get(cat_id)
        if not cat:
            return self.handle_error(400, 'Cat image not found!')
        print(cat.path)
        return send_file(cat.path, as_attachment=True)

    @swag_from('api_docs/cat/cat_delete.yml')
    def delete(self, cat_id):
        cat = cat_files.get(cat_id)
        if not cat:
            return self.handle_error(400, 'Cat image not found!')
        os.remove(cat.path)
        del cat_files[cat_id]
        return self.handle_success(200, cat_id, 'Cat image deleted successfully!')


class CatListResource(BaseResource):
    @swag_from('api_docs/cat/cat_list_get.yml')
    def get(self):
        response = {}
        for _id, cat in cat_files.items():
            response[_id] = cat.path
        return self.handle_success(200, response, 'success')
