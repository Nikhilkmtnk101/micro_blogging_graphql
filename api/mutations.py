import strawberry

from api.types import Post
from models import  Session
from models import Post as SQLPost  # Rename to avoid conflict



@strawberry.type
class Mutation:
    @strawberry.field
    def create_post(self, title: str, content: str) -> Post:
        with Session() as  session:
            db_post = SQLPost(title=title, content=content)
            session.add(db_post)
            session.commit()
            session.refresh(db_post)
            return Post(id=db_post.id, title=db_post.title, content=db_post.content)