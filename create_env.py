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
    environment = PostmanEnvironment([PostmanVariable("size", "5")])
    environment.write_to_file('test-env.json')


def create_aws_sigV4_environment(credentials):
    environment = PostmanEnvironment([
        PostmanVariable("AWS_ACCESS_KEY_ID", credentials.access_key),
        PostmanVariable("AWS_SECRET_ACCESS_KEY", credentials.secret_key),
        PostmanVariable("AWS_SESSION_TOKEN", credentials.token),
    ])
    environment.write_to_file('aws-env.json')


print("Creating...")
create_test_environment()
credentials = get_aws_credentials("default", "~/.aws/credentials")
create_aws_sigV4_environment(credentials)
print("Done")
