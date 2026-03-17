from .utils import (
    normalize_missing,
    clean_column_names,
    trim_strings,
    drop_constant_columns,
    remove_duplicates,
    fill_missing_values
)

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
        self.original_shape = df.shape

    def run_all(self):
        self.df = normalize_missing(self.df)
        self.df = clean_column_names(self.df)
        self.df = trim_strings(self.df)
        self.df = drop_constant_columns(self.df)
        self.df = remove_duplicates(self.df)
        self.df = fill_missing_values(self.df)

        return self.df

    def report(self):
        return {
            "before": self.original_shape,
            "after": self.df.shape
        }