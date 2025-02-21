from .ml.confusion_metrics import ModelMetrics
import numpy as np

def main() -> None:
    print("Hello from nc-framework!")

def demo_confusion_metrics() -> None:
    # Create dummy classification data
    actual_y = np.array([0, 1, 0, 1, 1, 0, 1, 0, 0, 1])
    predicted_y = np.array([0, 1, 0, 0, 1, 1, 1, 0, 0, 1])

    obj = ModelMetrics(actual_y, predicted_y)
    print(obj.print_metrics())

    # Create ModelMetr    cs instance
    
