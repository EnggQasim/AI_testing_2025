from create_excel_template import create_excel_template

def main():
    print("Generating AI testing framework Excel template...")
    try:
        create_excel_template('ai_model_testing_results.xlsx')
        print("\nExcel template generated successfully!")
        print("The file 'ai_model_testing_results.xlsx' contains the following sheets:")
        print("1. Classification_Data - Sample classification predictions")
        print("2. Classification_Metrics - Overall classification metrics")
        print("3. Confusion_Matrix - Confusion matrix for classification")
        print("4. Per_Class_Metrics - Per-class performance metrics")
        print("5. Regression_Data - Sample regression predictions")
        print("6. Regression_Metrics - Overall regression metrics")
        print("7. Residuals_Statistics - Detailed residuals analysis")
        print("8. Metadata - Generation information")
    except Exception as e:
        print(f"\nError generating Excel template: {str(e)}")
        print("Please ensure all required packages are installed using:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    main() 