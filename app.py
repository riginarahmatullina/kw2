from flask import Flask, render_template, request, redirect, jsonify
from utils import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/posts/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/api/posts/')
def index_api():
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/posts/<int:post_id>/', methods=['GET'])
def post_page(post_id):
    if post_id:
        posts = get_posts_by_user(post_id)
        if posts:
            return render_template('post.html', posts=posts)
        else:
            return render_template('errors_for_id.html')


@app.route('/api/posts/<int:post_id>/')
def index_api_by_user(post_id):
    posts = get_posts_by_user(post_id)
    return jsonify(posts)


@app.route('/search/')
def search_page():
    search_by = request.args['s']
    posts = search_for_posts(search_by)
    return render_template("search.html", posts=posts)



@app.route('/users/<user_name>')
def user_name_page(user_name):
    posts = get_posts_all()
    posts_list = []
    for post in posts:
        if post['poster_name'] == user_name:
            posts_list.append(post)
    if posts_list:
        return render_template('user-feed.html', posts=posts_list)
    else:
        return render_template('errors_for_user.html')


if __name__ == '__main__':
    app.run(debug=True)