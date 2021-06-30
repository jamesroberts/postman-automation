import json
import uuid
import configparser

from os import path
from dataclasses import dataclass


@dataclass
class Credentials:
    access_key: str
    secret_key: str
    token: str = None


def get_aws_credentials(profile, filepath):
    filename = path.expanduser(filepath)
    if path.isfile(filename):
        config = configparser.RawConfigParser()
        config.read(filename)
        return Credentials(*config[profile].values())
    else:
        raise FileNotFoundError(f"{filepath} could not be found.")


def create_test_environment():
    content = {
        'id': str(uuid.uuid4()),
        'name': "Whatever Env",
        'values': [
            {
                "key": "size",
                "value": "5",
                "enabled": True
            },
        ],
        "_postman_variable_scope": "environment",
        "_postman_exported_at": "2021-06-30T14:05:25.551Z",
        "_postman_exported_using": "Postman/8.6.2"

    }
    with open("./Test-env.postman_environment.json", "w") as env:
        env.write(json.dumps(content))


print("Creating...")
create_test_environment()
print("Done")
