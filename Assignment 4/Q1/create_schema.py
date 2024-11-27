import weaviate
import json

# Connect to Weaviate
client = weaviate.Client("http://localhost:8080")

# Define the schema
schema = {
    "classes": [
        {
            "class": "SimSearch",
            "properties": [
                {"name": "Category", "dataType": ["string"]},
                {"name": "Question", "dataType": ["string"]},
                {"name": "Answer", "dataType": ["string"]},
            ],
        }
    ]
}

# Check if schema exists
schema_exists = False
current_schema = client.schema.get()
for cls in current_schema.get("classes", []):
    if cls["class"] == "SimSearch":
        schema_exists = True
        break

# Create schema if missing
if not schema_exists:
    client.schema.create(schema)
    print("Schema created successfully!")
else:
    print("Schema already exists!")

# Load data
with open("data.json", "r") as f:
    data = json.load(f)
for item in data:
    client.data_object.create(item, "SimSearch")
print("Data uploaded successfully!")
