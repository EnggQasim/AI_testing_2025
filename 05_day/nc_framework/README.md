# AI Model Testing Framework

A comprehensive framework for evaluating ML, DL, and generative AI models. This framework provides various metrics for both classification and regression tasks.

## Features

- Automatic task type detection (classification vs regression)
- Support for numpy arrays, lists, and PyTorch tensors
- Comprehensive metrics calculation:
  - Classification: accuracy, precision, recall, F1-score, ROC AUC, confusion matrix
  - Regression: MSE, RMSE, MAE, R², MAPE, residuals analysis
- Per-class metrics for classification tasks
- Detailed error analysis and statistics

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.ml.confusion_metrics import ModelMetrics

# Example for classification
actual_y = [0, 1, 0, 1, 1, 0]
predicted_y = [0, 1, 0, 0, 1, 0]

metrics = ModelMetrics(actual_y, predicted_y)
metrics.print_metrics()  # For formatted output
results = metrics.get_metrics()  # For raw metrics dictionary

# Example for regression
actual_y = [1.5, 2.1, 3.3, 4.7, 5.8]
predicted_y = [1.7, 2.0, 3.1, 4.9, 5.5]

metrics = ModelMetrics(actual_y, predicted_y)
metrics.print_metrics()
```

## Output Example

### Classification Task
```
=== Model Evaluation Metrics ===
Task Type: Classification

Metrics:
accuracy: 0.833
precision: 0.857
recall: 0.833
f1: 0.844
roc_auc: 0.875

confusion_matrix:
[[3 0]
 [1 2]]

per_class_metrics:
  class_0:
    precision: 0.750
    recall: 1.000
    f1: 0.857
  class_1:
    precision: 1.000
    recall: 0.667
    f1: 0.800
```

### Regression Task
```
=== Model Evaluation Metrics ===
Task Type: Regression

Metrics:
mse: 0.034
rmse: 0.184
mae: 0.160
r2: 0.989
explained_variance: 0.991
mape: 3.842

residuals_stats:
  mean: -0.020
  std: 0.187
  max: 0.200
  min: -0.300
```

## Contributing

Feel free to submit issues and enhancement requests!
