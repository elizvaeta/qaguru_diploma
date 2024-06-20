from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Filters:
    specialties: list[str]


@dataclass_json
@dataclass
class PostTagsBody:
    filters: Filters
    limit: int = 100
    category: str = 'it'


body_default = PostTagsBody(
    filters={}
).to_dict()

body_with_specialties = PostTagsBody(
    filters=Filters(
        specialties=['testirovanie']
    )
).to_dict()
