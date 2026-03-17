# dfcleanerpro

![PyPI](https://img.shields.io/pypi/v/dfcleanerpro)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> A lightweight and efficient DataFrame preprocessing library designed for modern data workflows.

---

## Installation

```
pip install dfcleanerpro
```

---

## Key Capabilities

- Automated data cleaning pipeline
- Intelligent handling of missing values
- Standardized column name formatting
- Duplicate record elimination
- Removal of low-information columns
- String normalization for text fields
- Simple and intuitive API design

---

## Getting Started

### Basic Usage

```python
import pandas as pd
from dfcleanerpro import DataCleaner

df = pd.read_csv("data.csv")

cleaned_df = DataCleaner(df).run_all()
```

---

### Example Transformation

```python
data = {
    "Name ": ["Nishanth", "Arun", "Arun", "Azar", "None"],
    "Age": [27, None, 26, 27, 30],
    "City": [" Bangalore", "Chennai", "Chennai", None, "Mumbai"],
    "Constant": [1,1,1,1,1]
}

df = pd.DataFrame(data)

cleaned = DataCleaner(df).run_all()
print(cleaned)
```

---

## What It Handles

| Task              | Description                           |
| ----------------- | ------------------------------------- |
| Missing Values    | Replaces nulls using smart strategies |
| Column Formatting | Converts names to clean snake_case    |
| Duplicate Rows    | Identifies and removes duplicates     |
| Constant Columns  | Drops columns with no variance        |
| String Cleanup    | Removes unwanted whitespace           |

---

## Design Philosophy

Data preprocessing is a repetitive but critical step in any data workflow.
This library focuses on:

- Simplicity over complexity
- Clean and readable transformations
- Reusability across projects

---

## Built With

- Python
- Pandas
- NumPy

---

## Use Cases

- Data Engineering pipelines
- Data Science preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning data preparation

---

## Future Enhancements

- [ ] CLI support for CSV processing
- [ ] Data validation rules
- [ ] Outlier detection utilities
- [ ] Data profiling reports
- [ ] Integration with big data tools

---

## Contributions

Contributions, issues, and feature requests are welcome!

## License

MIT License
