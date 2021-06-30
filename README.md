# postman-automation
Some scripts for working with Postman and the newman CLI tool.


# Setup

Install [Postman](https://www.postman.com/downloads/) and create any [collection](https://learning.postman.com/docs/sending-requests/intro-to-collections/) of requests you want.

Install [newman-cli](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

<i>Note: This will require you having [Node.js](https://nodejs.org/en/download/current/) installed.</i>

```bash
npm install -g newman
```

# Running

Create your Postman environment file using the `create_env.py` Python script.

```bash
python create_env.py
```

Run your Postman collection with your newly created environment file:

```bash
newman run <path-to-collection.json> -e <path-to-created-envinoment.json>
```