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

    def write_to_file(self, filepath):
        with open(filepath, "w") as file:
            file.write(json.dumps(asdict(self)))


def get_aws_credentials(profile, filepath):
    filename = path.expanduser(filepath)
    if path.isfile(filename):
        config = configparser.RawConfigParser()
        config.read(filename)
        return Credentials(*config[profile].values())
    else:
        raise FileNotFoundError(f"{filepath} could not be found.")


def create_test_environment():
    variables = [PostmanVariable("size", "5")]
    content = PostmanEnvironment(variables)
    content.write_to_file("./Test-env.postman_environment.json")


print("Creating...")
create_test_environment()
print("Done")
