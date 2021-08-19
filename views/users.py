"""Blueprint с /users/"""

from flask import Blueprint, render_template
from models.user import User
from models.post import Post


user_app = Blueprint("user_app", __name__)


@user_app.route("/", endpoint="users_list")
def user_list():
    users = User.query.order_by(User.id.desc()).all()
    return render_template("users/user_list.html", users=users)


@user_app.route("/<int:user_id>/", endpoint="user_detail")
def user_detail(user_id):
    user = User.get_user_by_id(user_id)
    posts = Post.query.filter(Post.user.has(id=user_id)).order_by(Post.id.desc()).all()

    return render_template('users/user_detail.html', user=user, posts=posts)
