import pandas as pd
import numpy as np
from confusion_metrics import ModelMetrics
from datetime import datetime

def create_classification_example():
    # Create dummy classification data
    actual_y = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1])
    predicted_y = np.array([0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1])
    
    # Calculate metrics
    metrics = ModelMetrics(actual_y, predicted_y)
    results = metrics.get_metrics()
    
    # Create DataFrames
    data_df = pd.DataFrame({
        'Sample_ID': range(1, len(actual_y) + 1),
        'Actual_Label': actual_y,
        'Predicted_Label': predicted_y,
        'Correct_Prediction': actual_y == predicted_y
    })
    
    # Extract metrics
    metrics_data = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC'],
        'Value': [
            results['accuracy'],
            results['precision'],
            results['recall'],
            results['f1'],
            results.get('roc_auc', 'N/A')
        ]
    }
    metrics_df = pd.DataFrame(metrics_data)
    
    # Create confusion matrix DataFrame
    cm = results['confusion_matrix']
    cm_df = pd.DataFrame(cm, 
                        columns=['Predicted_0', 'Predicted_1'],
                        index=['Actual_0', 'Actual_1'])
    
    # Per-class metrics
    per_class = results['per_class_metrics']
    per_class_data = []
    for cls in per_class:
        metrics = per_class[cls]
        per_class_data.append({
            'Class': cls,
            'Precision': metrics['precision'],
            'Recall': metrics['recall'],
            'F1': metrics['f1']
        })
    per_class_df = pd.DataFrame(per_class_data)
    
    return data_df, metrics_df, cm_df, per_class_df

def create_regression_example():
    # Create dummy regression data
    np.random.seed(42)
    actual_y = np.array([1.5, 2.1, 3.3, 4.7, 5.8, 2.4, 3.9, 4.1, 5.2, 6.7])
    noise = np.random.normal(0, 0.2, len(actual_y))
    predicted_y = actual_y + noise
    
    # Calculate metrics
    metrics = ModelMetrics(actual_y, predicted_y)
    results = metrics.get_metrics()
    
    # Create DataFrames
    data_df = pd.DataFrame({
        'Sample_ID': range(1, len(actual_y) + 1),
        'Actual_Value': actual_y,
        'Predicted_Value': predicted_y,
        'Residual': results['residuals']
    })
    
    # Extract metrics
    metrics_data = {
        'Metric': ['MSE', 'RMSE', 'MAE', 'R²', 'Explained Variance', 'MAPE'],
        'Value': [
            results['mse'],
            results['rmse'],
            results['mae'],
            results['r2'],
            results['explained_variance'],
            results['mape']
        ]
    }
    metrics_df = pd.DataFrame(metrics_data)
    
    # Residuals statistics
    residuals_stats = pd.DataFrame({
        'Statistic': ['Mean', 'Standard Deviation', 'Maximum', 'Minimum'],
        'Value': [
            results['residuals_stats']['mean'],
            results['residuals_stats']['std'],
            results['residuals_stats']['max'],
            results['residuals_stats']['min']
        ]
    })
    
    return data_df, metrics_df, residuals_stats

def create_excel_template(output_file='ai_testing_results.xlsx'):
    # Create Excel writer
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Get the workbook and create a format
        workbook = writer.book
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#D9E1F2',
            'border': 1
        })
        
        # Classification example
        class_data, class_metrics, cm, per_class = create_classification_example()
        
        # Write classification sheets
        class_data.to_excel(writer, sheet_name='Classification_Data', index=False)
        class_metrics.to_excel(writer, sheet_name='Classification_Metrics', index=False)
        cm.to_excel(writer, sheet_name='Confusion_Matrix')
        per_class.to_excel(writer, sheet_name='Per_Class_Metrics', index=False)
        
        # Regression example
        reg_data, reg_metrics, res_stats = create_regression_example()
        
        # Write regression sheets
        reg_data.to_excel(writer, sheet_name='Regression_Data', index=False)
        reg_metrics.to_excel(writer, sheet_name='Regression_Metrics', index=False)
        res_stats.to_excel(writer, sheet_name='Residuals_Statistics', index=False)
        
        # Add metadata sheet
        metadata = pd.DataFrame({
            'Property': ['Generated Date', 'Framework Version', 'Total Samples'],
            'Value': [datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                     '1.0.0',
                     len(class_data) + len(reg_data)]
        })
        metadata.to_excel(writer, sheet_name='Metadata', index=False)
        
        # Format all sheets
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            for col_num, value in enumerate(worksheet.table.columns):
                worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(0, worksheet.table.columns.size - 1, 15)

if __name__ == "__main__":
    create_excel_template() 