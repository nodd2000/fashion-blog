from flask import Flask, render_template
import config
from models.base import db
from models.post import Post
from views.posts import post_app
from views.users import user_app

app = Flask(__name__)
app.register_blueprint(post_app, url_prefix="/posts")
app.register_blueprint(user_app, url_prefix="/users")

app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)


@app.route("/", methods=["GET", "POST"], endpoint="index")
def index():
    posts = Post.query.order_by(Post.id.desc()).limit(3).all()
    return render_template("index.html", posts=posts)


@app.cli.command('init-db', with_appcontext=True)
def initialize_db():
    """
    Create initial sqlite db
    """
    print("Do init db")
    db.create_all()
    print("Init db done")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )