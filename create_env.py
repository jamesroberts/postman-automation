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
    name: str
    values: List[PostmanVariable]

    def write_to_file(self, filepath: str):
        with open(filepath, "w") as file:
            file.write(json.dumps(asdict(self)))


def get_aws_credentials(profile: str, filepath: str):
    filename = path.expanduser(filepath)
    if path.isfile(filename):
        config = configparser.RawConfigParser()
        config.read(filename)
        return Credentials(*config[profile].values())
    else:
        raise FileNotFoundError(f"{filepath} could not be found.")


def write_environment_to_file(environment: PostmanEnvironment, filepath: str):
    environment.write_to_file(filepath)


def create_test_environment():
    return PostmanEnvironment("TestEnv", [PostmanVariable("size", "5")])


def create_aws_sigV4_environment(credentials: Credentials):
    return PostmanEnvironment("AWS SigV4", [
        PostmanVariable("AWS_ACCESS_KEY_ID", credentials.access_key),
        PostmanVariable("AWS_SECRET_ACCESS_KEY", credentials.secret_key),
        PostmanVariable("AWS_SESSION_TOKEN", credentials.token),
    ])


print("Creating...")
test_env = create_test_environment()
credentials = get_aws_credentials("default", "~/.aws/credentials")
aws_env = create_aws_sigV4_environment(credentials)

write_environment_to_file(aws_env,  "./aws-env.json")
write_environment_to_file(test_env, "./test-env.json")

print("Done")
