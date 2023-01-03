import re
from app.dao.models.models import Post
from app.dao.post_dao import PostDAO
from app.services.base_service import BaseService
from exceptions import ItemNotFound


class PostService(BaseService[PostDAO]):

    def get_all(self) -> list[Post]:

        return self.dao.get_all()


    def get_item(self, pk: int) -> Post:

        try:
            if post := self.dao.get_by_id(pk):
                return post
        except ItemNotFound(f'Post with pk={pk} not exists.') as e:
            print(f'Post with pk={pk} not exists.', e)


    def get_post_by_username(self, username: str):

        post = self.dao.get_item_by_username(username)

        return post


    def get_posts_by_word(self, word: str):

        list_posts = self.get_all()
        content = [x for x in list_posts if word.lower() in re.split(" |,|-|!|#|по", x.content)]

        return content


    def add_tag_in_post_content(self):

        posts = self.get_all()

        for post in posts:
            post.content_tag = ""
            list_items = re.split(" |,|-|!", post.content)
            for i in range(len(list_items)):
                if "#" in list_items[i]:
                    list_items[i] = f"<a href=\"/tag/{list_items[i][1:]}\">{list_items[i]}</a>"

            post.content_tag = " ".join(list_items)

            self.dao.update(post)


    def add_tag(self):

        posts = self.get_all()

        for post in posts:
            post.text_tag = ""
            for i in re.split(" |,|-|!", post.content):
                if '#' in i:
                    post.text_tag += f"<a href=\"/tag/{i[1:]}\">{i}</a>"

            self.dao.update(post)

