import os
from pathlib import Path

import tbank_career_tests


def root_dir():
    return (
        Path(tbank_career_tests.__file__)
        .parent
        .parent
        .absolute()
        .__str__()
    )


ROOT_DIR = root_dir()
JSON_SCHEMAS_DIR = os.path.join(ROOT_DIR, 'json_schemas')
