import pandas as pd
import numpy as np
import re

def normalize_missing(df):
    return df.replace(["None", "none", "NULL", "null", ""], np.nan)

def clean_column_names(df):
    df = df.copy()
    df.columns = [
        re.sub(r'[^a-z0-9]+', '_', col.strip().lower()).strip('_')
        for col in df.columns
    ]
    return df

def trim_strings(df):
    df = df.copy()
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()
    return df

def drop_constant_columns(df):
    return df.loc[:, df.nunique() > 1]

def remove_duplicates(df, subset=None, keep="first"):
    return df.drop_duplicates(subset=subset, keep=keep)

def fill_missing_values(df, method="mean"):
    df = df.copy()

    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(exclude=np.number).columns

    if method == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    elif method == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    elif method == "mode":
        for col in categorical_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

    elif method == "ffill":
        df = df.fillna(method="ffill")

    elif method == "bfill":
        df = df.fillna(method="bfill")

    else:
        raise ValueError(f"Invalid method: {method}")

    return df