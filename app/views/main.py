from flask import Blueprint, request, render_template, redirect

from app.container import post_service, comment_service, bookmark_service



main_blueprint = Blueprint("main", __name__, static_folder='static', template_folder='templates')


@main_blueprint.route('/')
def main():
    post_service.add_tag()
    post_service.add_tag_in_post_content()
    posts = post_service.get_all()

    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post(postid):

    post = post_service.get_item(postid)
    comments = comment_service.get_by_pk(postid)
    count_comments = len(comments)

    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@main_blueprint.route('/search/')
def search():

    return render_template('search.html')


@main_blueprint.route('/posts/')
def s_search():

    query = request.args['s']
    posts = post_service.get_posts_by_word(query)
    count_posts = len(posts)
    print(posts)

    return render_template('search.html', query=query, posts=posts, count_posts=count_posts)


@main_blueprint.route('/users/<username>')
def users(username):

    user_posts = post_service.get_post_by_username(username)

    return render_template('user-feed.html', posts=user_posts)


@main_blueprint.route('/bookmarks/')
def bookmarks():

    bookmarks = bookmark_service.get_all()

    return render_template('bookmarks.html', bookmarks=bookmarks)



@main_blueprint.route('/bookmarks/add/<int:postid>')
def add_post(postid):

    bookmark_service.add_bookmark(postid)

    return redirect("/", code=302)


@main_blueprint.route('/bookmarks/remove/<int:postid>')
def remove_post(postid):

    bookmark_service.delete_bookmark(postid)

    return redirect("/", code=302)


@main_blueprint.route('/tag/<name_tag>')
def user_tag(name_tag):

    posts = post_service.get_posts_by_word(name_tag)

    return render_template('tag.html', posts=posts, name_tag=name_tag)








