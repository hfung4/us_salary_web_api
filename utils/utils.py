from pathlib import Path
import pandas as pd
import numpy as np

# Get the US personal income distribution
df_income_dist = pd.read_csv(Path("utils", "artifacts", "income_dist.csv"))

# Get the income bins
income_bins = df_income_dist["personal_income"].tolist()


def get_percentile(income):
    percentile = np.digitize([income], income_bins) + 1
    return percentile.item()


if __name__ == "__main__":
    print(get_percentile(120000))
