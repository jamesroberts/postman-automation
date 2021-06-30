import json
import uuid


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
