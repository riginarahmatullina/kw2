from app import app
api_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']


def test_posts():
    """Проверка всех постов"""
    api_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    api_posts = response.json
    for api_post in api_posts:
        for api_post_key in api_post.keys():
            print(api_post_key in api_keys)
            assert api_post_key in api_keys


def test_post_by_user():
    """Проверка одного поста"""
    api_keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk', 'comments']
    response = app.test_client().get('/api/posts/1/')
    assert response.status_code == 200
    api_posts = response.json
    for api_post in api_posts:
        for api_post_key in api_post.keys():
            print(api_post_key)
            assert api_post_key in api_keys
