import bentoml
import numpy as np

# Load the model imported from MLflow
iris_model = bentoml.mlflow.get("iris_bento:latest")

@bentoml.service(
    name="iris_classifier_service",
    traffic={"timeout": 60},
)
class IrisService:
    # This automatically handles the model loading/runner logic
    model_ref = iris_model

    def __init__(self):
        # Load the model runner/model into memory
        self.model = self.model_ref.load_model()

    @bentoml.api
    def predict(self, input_data: np.ndarray) -> np.ndarray:
        # Standard sklearn predict call
        prediction = self.model.predict(input_data)
        return prediction
