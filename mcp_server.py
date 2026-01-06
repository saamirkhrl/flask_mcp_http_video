# @app.route("/tools/get_announcements", methods=["GET"])

"""
curl -X POST http://localhost:5001/tools/create \
  -H "Content-Type: application/json" \
  -d '{"title":"New announcement","content":"This is the announcement content."}'
"""

# python3 -m venv [name your ve here]

# [ve]\Scripts\activate

from flask import Flask, request

app = Flask(__name__)

announcements = []



@app.route("/tools", methods=["GET"])
def get_tools():
    return {
        "tools": [
            {
                "name": "get_recent_announcements",
                "description": "Fetches the newest announcements from the database",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            {
                "name": "create_announcement",
                "description": "Creates a new announcement",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["title", "content"]
                }
            }
        ]
    }

@app.route("/tools/create", methods=["POST"])
def create_announcement():
    data = request.get_json()

    new_post = {
        "title": data["title"],
        "content": data["content"]
    }

    announcements.append(new_post)

    return {
        "content": [
            {
                "type": "text",
                "text": f"Created new announcement titled {data['title']}"
            }
        ]
    }

@app.route("/tools/get_announcements", methods=["GET"])
def get_announcements():
    return {
        "content": [
            {
                "type": "text",
                "text": f"Recent announcements: {announcements[-2:]}"
            }
        ]
    }

if __name__ == "__main__":
    app.run(debug=True, port=5001)
