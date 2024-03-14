from datetime import datetime
from datetime import timedelta
import random

import numpy as np
import pandas as pd


def generate_data() -> None:
    random.seed(0)
    np.random.seed(0)
    dates = []
    curr = datetime(2020, 1, 1)
    limit = datetime(2024, 1, 1)
    while curr < limit:
        dates.append(curr)
        curr += timedelta(minutes=round(random.expovariate(0.1)))

    item_id = np.arange(len(dates))
    num_feature = np.random.rand(len(dates))
    cat_feature = np.random.choice(
        ["a", "b", "c", "d", "e"], len(dates), p=[0.1, 0.2, 0.05, 0.4, 0.25]
    )
    target = np.random.choice([0, 1], len(dates), p=[0.7, 0.3])
    pos_probs = np.random.beta(5, 2, len(dates))
    neg_probs = np.random.beta(1, 5, len(dates))
    prediction = np.where(target, pos_probs, neg_probs)

    pd.DataFrame(
        {
            "item_id": item_id,
            "created": dates,
            "num_feature": num_feature,
            "cat_feature": cat_feature,
            "target": target,
            "prediction": prediction,
        }
    ).to_parquet("data/data.pq")
