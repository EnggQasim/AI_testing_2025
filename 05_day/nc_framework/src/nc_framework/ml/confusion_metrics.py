import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, mean_squared_error,
    mean_absolute_error, r2_score
)
from typing import Union, Dict, List, Tuple
import torch

class ModelMetrics:
    """A comprehensive framework for calculating various ML/DL model evaluation metrics."""
    
    def __init__(self, actual_y: Union[np.ndarray, List, torch.Tensor], 
                 predicted_y: Union[np.ndarray, List, torch.Tensor]):
        """
        Initialize the ModelMetrics class.
        
        Args:
            actual_y: Ground truth labels/values
            predicted_y: Predicted labels/values
        """
        # Convert inputs to numpy arrays
        self.actual_y = self._convert_to_numpy(actual_y)
        self.predicted_y = self._convert_to_numpy(predicted_y)
        
        # Determine if it's a classification or regression task
        self.is_classification = self._is_classification_task()
    
    def _convert_to_numpy(self, data: Union[np.ndarray, List, torch.Tensor]) -> np.ndarray:
        """Convert different input types to numpy array."""
        if isinstance(data, torch.Tensor):
            return data.detach().cpu().numpy()
        return np.array(data)
    
    def _is_classification_task(self) -> bool:
        """Determine if the task is classification or regression."""
        unique_values = np.unique(self.actual_y)
        return len(unique_values) < 10 or np.all(np.mod(unique_values, 1) == 0)
    
    def calculate_classification_metrics(self) -> Dict:
        """Calculate metrics for classification tasks."""
        if not self.is_classification:
            raise ValueError("This appears to be a regression task. Use calculate_regression_metrics instead.")
        
        metrics = {}
        
        # Basic metrics
        metrics['accuracy'] = accuracy_score(self.actual_y, self.predicted_y)
        
        try:
            metrics['precision'] = precision_score(self.actual_y, self.predicted_y, average='weighted')
            metrics['recall'] = recall_score(self.actual_y, self.predicted_y, average='weighted')
            metrics['f1'] = f1_score(self.actual_y, self.predicted_y, average='weighted')
            
            # Confusion matrix
            cm = confusion_matrix(self.actual_y, self.predicted_y)
            metrics['confusion_matrix'] = cm
            
            # Calculate per-class metrics
            unique_classes = np.unique(self.actual_y)
            per_class_metrics = {}
            for cls in unique_classes:
                per_class_metrics[f'class_{cls}'] = {
                    'precision': precision_score(self.actual_y, self.predicted_y, labels=[cls], average='micro'),
                    'recall': recall_score(self.actual_y, self.predicted_y, labels=[cls], average='micro'),
                    'f1': f1_score(self.actual_y, self.predicted_y, labels=[cls], average='micro')
                }
            metrics['per_class_metrics'] = per_class_metrics
            
            # Try to calculate ROC AUC if applicable
            try:
                metrics['roc_auc'] = roc_auc_score(self.actual_y, self.predicted_y)
            except:
                pass
                
        except Exception as e:
            print(f"Warning: Some metrics couldn't be calculated: {str(e)}")
        
        return metrics
    
    def calculate_regression_metrics(self) -> Dict:
        """Calculate metrics for regression tasks."""
        if self.is_classification:
            raise ValueError("This appears to be a classification task. Use calculate_classification_metrics instead.")
        
        metrics = {
            'mse': mean_squared_error(self.actual_y, self.predicted_y),
            'rmse': np.sqrt(mean_squared_error(self.actual_y, self.predicted_y)),
            'mae': mean_absolute_error(self.actual_y, self.predicted_y),
            'r2': r2_score(self.actual_y, self.predicted_y),
            'explained_variance': np.var(self.predicted_y) / np.var(self.actual_y)
        }
        
        # Calculate custom metrics
        metrics['mape'] = np.mean(np.abs((self.actual_y - self.predicted_y) / self.actual_y)) * 100
        metrics['residuals'] = self.actual_y - self.predicted_y
        metrics['residuals_stats'] = {
            'mean': np.mean(metrics['residuals']),
            'std': np.std(metrics['residuals']),
            'max': np.max(metrics['residuals']),
            'min': np.min(metrics['residuals'])
        }
        
        return metrics
    
    def get_metrics(self) -> Dict:
        """Get all relevant metrics based on the task type."""
        if self.is_classification:
            return self.calculate_classification_metrics()
        return self.calculate_regression_metrics()
    
    def print_metrics(self) -> None:
        """Print all metrics in a formatted way."""
        metrics = self.get_metrics()
        print("\n=== Model Evaluation Metrics ===")
        print(f"Task Type: {'Classification' if self.is_classification else 'Regression'}")
        print("\nMetrics:")
        for metric_name, value in metrics.items():
            if isinstance(value, dict):
                print(f"\n{metric_name}:")
                for sub_metric, sub_value in value.items():
                    print(f"  {sub_metric}: {sub_value}")
            elif isinstance(value, np.ndarray):
                print(f"\n{metric_name}:\n{value}")
            else:
                print(f"{metric_name}: {value}")
