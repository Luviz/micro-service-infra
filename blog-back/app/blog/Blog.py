from dataclasses import dataclass, asdict
from typing_extensions import Self
import uuid
import json


@dataclass
class Blog():
    id: str
    title: str
    author: str
    published: str

    def __init__(self, title: str, author: str, published: str, id=None):
        self.id = str(uuid.uuid4()) if id is None else id
        self.title = title
        self.author = author
        self.published = published

    def asDict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.asDict(), indent=2)

    @classmethod
    def from_json(cls: type[Self], json_str: str):
        val = json.loads(json_str)
        return Blog(**val)


if __name__ == '__main__':
    print("tests")
    blog1 = Blog("test1", "bardia jedi", "2022-12-02T00:00:00Z")
    print(blog1.to_json())
    blog2 = Blog("test2", "bardia jedi", "2022-12-02T00:00:00Z", id='someId')
    print(blog2.to_json())
    print(blog2.asDict())
    json_data = """
    {
        "id": "3fb1ae17-8e5e-453a-9994-9b5446912679",
        "title": "test",
        "author": "bardia jedi",
        "published": "2022-12-02T00:00:00Z"
    }
    """
    print(Blog.from_json(json_data))
