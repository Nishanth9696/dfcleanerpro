import pandas as pd
from dfcleanerpro import DataCleaner

def test_pipeline():
    data = {
        "Name ": ["A", "B", "B", "None"],
        "Age": [10, None, 10, 20],
        "City": [" Chennai", "Delhi ", "Delhi ", None],
        "Constant": [1,1,1,1]
    }

    df = pd.DataFrame(data)

    cleaner = DataCleaner(df)
    result = cleaner.run_all()

    assert result.shape[0] > 0
    assert "constant" not in result.columns