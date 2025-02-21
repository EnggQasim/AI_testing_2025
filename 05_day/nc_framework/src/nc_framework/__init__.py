from .ml.confusion_metrics import ModelMetrics
import numpy as np

def main() -> None:
    print("Hello from nc-framework!")

def demo_confusion_metrics() -> None:
    # Create dummy classification data
    # Example for classification
    actual_y = [0, 1, 0, 1, 1, 0]
    predicted_y = [0, 1, 0, 0, 1, 0]
    print("Classification Example")
    print(actual_y)
    print(predicted_y)

    metrics = ModelMetrics(actual_y, predicted_y)
    metrics.print_metrics()  # For formatted output
    results = metrics.get_metrics()  # For raw metrics dictionary

    # Example for regression
    actual_y = [1.5, 2.1, 3.3, 4.7, 5.8]
    predicted_y = [1.7, 2.0, 3.1, 4.9, 5.5]
    print("Regression Example")
    print(actual_y)
    print(predicted_y)

    metrics = ModelMetrics(actual_y, predicted_y)
    metrics.print_metrics()

    # Create ModelMetr    cs instance
    
