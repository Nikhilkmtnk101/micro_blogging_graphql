import strawberry


@strawberry.type
class User:
    id: strawberry.ID
    name: str

@strawberry.type
class Post:
    id: strawberry.ID
    title: str
    content: str

    @strawberry.field
    def summary(self)-> str:
        return f'{self.content[:10]}' if len(self.content) > 10 else self.content

    @strawberry.field
    def user(self) -> User:
        return User(id=1, name="Nikhil")