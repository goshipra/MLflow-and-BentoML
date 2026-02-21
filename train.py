import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Start MLflow experiment tracking
mlflow.set_experiment("Iris_Project")

with mlflow.start_run():
    # Load data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

    # Train Model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Log metrics & Model
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)
    
    # Register the model in MLflow Registry
    mlflow.sklearn.log_model(
        sk_model=model, 
        artifact_path="iris-model", 
        registered_model_name="iris_classifier"
    )
    print(f"Model trained with accuracy: {accuracy}")
