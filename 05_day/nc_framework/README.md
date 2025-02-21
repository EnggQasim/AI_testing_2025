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
pip install .
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

you can also run the demo by running `uv run nc-framework-demo`

### console commands
```cmd
(my-env) m.qasim@Muhammads-MacBook-Pro nc_framework % conda activate my-env
(my-env) m.qasim@Muhammads-MacBook-Pro nc_framework % pip install .
Processing /Users/m.qasim/Desktop/Nescom/AI_testing_2025/AI_testing_2025/05_day/nc_framework
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting numpy>=1.24.4 (from nc-framework==0.1.0)
  Downloading numpy-2.2.3-cp312-cp312-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting scikit-learn>=1.3.2 (from nc-framework==0.1.0)
  Downloading scikit_learn-1.6.1-cp312-cp312-macosx_12_0_arm64.whl.metadata (31 kB)
Collecting torch>=2.5.1 (from nc-framework==0.1.0)
  Downloading torch-2.6.0-cp312-none-macosx_11_0_arm64.whl.metadata (28 kB)
Collecting scipy>=1.6.0 (from scikit-learn>=1.3.2->nc-framework==0.1.0)
  Downloading scipy-1.15.2-cp312-cp312-macosx_14_0_arm64.whl.metadata (61 kB)
Collecting joblib>=1.2.0 (from scikit-learn>=1.3.2->nc-framework==0.1.0)
  Downloading joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn>=1.3.2->nc-framework==0.1.0)
  Downloading threadpoolctl-3.5.0-py3-none-any.whl.metadata (13 kB)
Collecting filelock (from torch>=2.5.1->nc-framework==0.1.0)
  Downloading filelock-3.17.0-py3-none-any.whl.metadata (2.9 kB)
Collecting typing-extensions>=4.10.0 (from torch>=2.5.1->nc-framework==0.1.0)
  Using cached typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting networkx (from torch>=2.5.1->nc-framework==0.1.0)
  Downloading networkx-3.4.2-py3-none-any.whl.metadata (6.3 kB)
Collecting jinja2 (from torch>=2.5.1->nc-framework==0.1.0)
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting fsspec (from torch>=2.5.1->nc-framework==0.1.0)
  Downloading fsspec-2025.2.0-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: setuptools in /Users/m.qasim/anaconda3/envs/my-env/lib/python3.12/site-packages (from torch>=2.5.1->nc-framework==0.1.0) (75.8.0)
Collecting sympy==1.13.1 (from torch>=2.5.1->nc-framework==0.1.0)
  Downloading sympy-1.13.1-py3-none-any.whl.metadata (12 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy==1.13.1->torch>=2.5.1->nc-framework==0.1.0)
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch>=2.5.1->nc-framework==0.1.0)
  Using cached MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl.metadata (4.0 kB)
Downloading numpy-2.2.3-cp312-cp312-macosx_14_0_arm64.whl (5.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 392.9 kB/s eta 0:00:00
Downloading scikit_learn-1.6.1-cp312-cp312-macosx_12_0_arm64.whl (11.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 2.1 MB/s eta 0:00:00
Downloading torch-2.6.0-cp312-none-macosx_11_0_arm64.whl (66.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.5/66.5 MB 817.9 kB/s eta 0:00:00
Downloading sympy-1.13.1-py3-none-any.whl (6.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 1.5 MB/s eta 0:00:00
Downloading joblib-1.4.2-py3-none-any.whl (301 kB)
Downloading scipy-1.15.2-cp312-cp312-macosx_14_0_arm64.whl (22.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.4/22.4 MB 743.0 kB/s eta 0:00:00
Downloading threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Downloading filelock-3.17.0-py3-none-any.whl (16 kB)
Downloading fsspec-2025.2.0-py3-none-any.whl (184 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Downloading networkx-3.4.2-py3-none-any.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 380.7 kB/s eta 0:00:00
Using cached MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl (12 kB)
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 889.3 kB/s eta 0:00:00
Building wheels for collected packages: nc-framework
  Building wheel for nc-framework (pyproject.toml) ... done
  Created wheel for nc-framework: filename=nc_framework-0.1.0-py3-none-any.whl size=6507 sha256=433501a5cd8b522828c676a7661b48515856507cb56c108cc0ee02e6a189e47d
  Stored in directory: /private/var/folders/42/ftm2w6v12wn_x2jpcxj8gk4h0000gn/T/pip-ephem-wheel-cache-h28xdw5a/wheels/84/9b/73/b3ffed8ad81d493f07dc7395ee4837c369cd887b9d95c42ebd
Successfully built nc-framework
Installing collected packages: mpmath, typing-extensions, threadpoolctl, sympy, numpy, networkx, MarkupSafe, joblib, fsspec, filelock, scipy, jinja2, torch, scikit-learn, nc-framework
  Attempting uninstall: nc-framework
    Found existing installation: nc-framework 0.1.0
    Uninstalling nc-framework-0.1.0:
      Successfully uninstalled nc-framework-0.1.0
Successfully installed MarkupSafe-3.0.2 filelock-3.17.0 fsspec-2025.2.0 jinja2-3.1.5 joblib-1.4.2 mpmath-1.3.0 nc-framework-0.1.0 networkx-3.4.2 numpy-2.2.3 scikit-learn-1.6.1 scipy-1.15.2 sympy-1.13.1 threadpoolctl-3.5.0 torch-2.6.0 typing-extensions-4.12.2
(my-env) m.qasim@Muhammads-MacBook-Pro nc_framework % uv run demo
[0 1 0 1 1 0 1 0 0 1]
[0 1 0 0 1 1 1 0 0 1]

=== Model Evaluation Metrics ===
Task Type: Classification

Metrics:
accuracy: 0.8
precision: 0.8
recall: 0.8
f1: 0.8

confusion_matrix:
[[4 1]
 [1 4]]

per_class_metrics:
  class_0: {'precision': 0.8, 'recall': 0.8, 'f1': 0.8}
  class_1: {'precision': 0.8, 'recall': 0.8, 'f1': 0.8}
roc_auc: 0.8
```
