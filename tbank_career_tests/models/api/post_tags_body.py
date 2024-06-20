from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Filters:
    specialties: list[str]
    category: str = 'it'


@dataclass_json
@dataclass
class PostTagsBody:
    filters: Filters
    limit: int | str = 'all'


body_default = PostTagsBody(
    filters=Filters(
        specialties=[]
    )
).to_dict()

body_with_specialties = PostTagsBody(
    filters=Filters(
        specialties=['testirovanie']
    )
).to_dict()
