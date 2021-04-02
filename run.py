from blog import app, db
from blog import routes, models, errors


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': models.User,
        'Post': models.Post
    }


if __name__ == '__main__':
    app.run(debug=True)
