from datetime import datetime
from datetime import timedelta
import random
from typing import Iterable

import numpy as np
import pandas as pd


def generate_data(
    start_year: int,
    end_year: int,
    num_param: int,
    cat_p: Iterable[float],
    target_p: Iterable[float],
    pos_prob_params: Iterable[int],
    neg_prob_params: Iterable[int],
) -> pd.DataFrame:
    dates = []
    curr = datetime(start_year, 1, 1)
    limit = datetime(end_year, 1, 1)
    while curr < limit:
        dates.append(curr)
        curr += timedelta(minutes=round(random.expovariate(0.1)))
    n = len(dates)
    item_id = np.arange(n)
    num_feature = np.random.rand(n, num_param).mean(1)
    cat_feature = np.random.choice(["a", "b", "c", "d", "e"], n, p=cat_p)
    target = np.random.choice([0, 1], n, p=target_p)
    pos_probs = np.random.beta(*pos_prob_params, n)
    neg_probs = np.random.beta(*neg_prob_params, n)
    prediction = np.where(target, pos_probs, neg_probs)

    return pd.DataFrame(
        {
            "item_id": item_id,
            "created": dates,
            "num_feature": num_feature,
            "cat_feature": cat_feature,
            "target": target,
            "prediction": prediction,
        }
    )


def generate_samples() -> None:
    generate_data(
        2020,
        2023,
        2,
        [0.1, 0.2, 0.05, 0.4, 0.25],
        [0.7, 0.3],
        pos_prob_params=[5, 2],
        neg_prob_params=[1, 5],
    ).to_parquet("data/ref.pq")

    generate_data(
        2023,
        2024,
        3,
        [0.0998, 0.1644, 0.0777, 0.4470, 0.2111],
        [0.74, 0.26],
        pos_prob_params=[5, 3],
        neg_prob_params=[1.3, 5],
    ).to_parquet("data/prod.pq")
