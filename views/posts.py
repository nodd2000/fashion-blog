"""Blueprint с /posts/"""

from flask import Blueprint, render_template
from models.post import Post

post_app = Blueprint("post_app", __name__)


@post_app.route("/", endpoint="posts_list")
def post_list():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("posts/post_list.html", posts=posts, theme_en='all')


@post_app.route("/<string:theme_en>/", endpoint="posts_theme")
def post_theme(theme_en):
    posts = Post.query.filter(Post.theme.has(theme_en=theme_en)).order_by(Post.id.desc()).all()
    return render_template("posts/post_list.html", posts=posts, theme_en=theme_en)


@post_app.route("/<int:post_id>/", endpoint="post_detail")
def post_detail(post_id):
    post = Post.get_post_by_id(post_id)
    return render_template(post.html, post=post)
