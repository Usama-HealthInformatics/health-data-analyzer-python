import pandas as pd

data = pd.read_csv("patients.csv")

print("Dataset Preview:")
print(data.head())

print("\nDiagnosis Count:")
print(data['diagnosis'].value_counts())
