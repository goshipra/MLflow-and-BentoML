import bentoml

# The URI points to the model in the MLflow Registry
# Format: "models:/<model_name>/<version_or_stage>"
model_uri = "models:/iris_classifier/1"

# Import into BentoML local store
bento_model = bentoml.mlflow.import_model("iris_bento", model_uri)

print(f"Model imported to BentoML: {bento_model}")
