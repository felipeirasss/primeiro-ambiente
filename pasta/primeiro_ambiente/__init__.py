from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'hello world'

app.run()

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app


    