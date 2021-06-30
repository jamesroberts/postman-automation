import json
import configparser

from os import path
from typing import List
from dataclasses import dataclass, asdict


@dataclass
class Credentials:
    access_key: str
    secret_key: str
    token: str = None


@dataclass
class PostmanVariable:
    key: str
    value: str


@dataclass
class PostmanEnvironment:
    values: List[PostmanVariable]

    def as_file(self):
        return json.dumps(asdict(self))


def get_aws_credentials(profile, filepath):
    filename = path.expanduser(filepath)
    if path.isfile(filename):
        config = configparser.RawConfigParser()
        config.read(filename)
        return Credentials(*config[profile].values())
    else:
        raise FileNotFoundError(f"{filepath} could not be found.")


def create_test_environment():
    with open("./Test-env.postman_environment.json", "w") as env:
        variables = [PostmanVariable("size", "5")]
        content = PostmanEnvironment(variables)
        env.write(content.as_file())


print("Creating...")
create_test_environment()
print("Done")
