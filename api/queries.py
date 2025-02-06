from typing import List
import strawberry
from api.types import Post as GQLPost  # GraphQL type
from models import Session, Post as SQLPost  # SQLAlchemy model

@strawberry.type
class Query:
   @strawberry.field
   def get_posts(self) -> List[GQLPost]:
       with Session() as session:
           posts = session.query(SQLPost).all()
           return [GQLPost(id=post.id, title=post.title, content=post.content)
                  for post in posts]

   @strawberry.field
   def get_post_by_id(self, id: strawberry.ID) -> GQLPost:
       with Session() as session:
           post = session.get(SQLPost, id=id)
           return GQLPost(id=post.id, title=post.title, content=post.content)