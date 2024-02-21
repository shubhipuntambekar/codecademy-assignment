from flask import Flask
from flasgger import Swagger

from app.config.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)
swagger = Swagger(app)


@app.route('/health')
def health_check():
    return 'Status: Up!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
