import json

POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"
def get_posts_all():
    try:
        with open(POST_PATH, "r", encoding='utf-8')as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден")

def get_posts_by_user(post_id):
    posts = get_posts_all()
    posts_list = []
    comment_list = get_comments_by_post_id(post_id)
    for post in posts:
        if post["pk"] == post_id:
            post['comments'] = comment_list
            posts_list.append(post)
            count = len(posts_list)
    return posts_list

def get_comments_by_post_id(post_id):
    with open(COMMENTS_PATH, "r", encoding='utf-8') as file:
        comments = json.load(file)
    comments_list = []
    for comment in comments:
        if comment["post_id"] == post_id:
            comments_list.append(comment)
    return comments_list

def search_for_posts(query):
    posts = get_posts_all()
    search_list = []
    query_lower = query.lower()
    for post in posts:
        search_word = post["content"].lower()
        if query_lower in search_word:
            search_list.append(post)
    return search_list