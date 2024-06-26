import json

from jsonschema.validators import validate
from requests import Response
from tbank_career_tests.helpers.paths import JSON_SCHEMAS_DIR


def assert_json_schema(response: Response, schema_name: str) -> None:
    full_path = JSON_SCHEMAS_DIR + '/' + schema_name

    with open(full_path) as f:
        schema = json.load(f)

    validate(response.json(), schema)
