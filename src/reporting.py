from evidently import ColumnMapping
from evidently.metric_preset import ClassificationPreset
from evidently.metric_preset import DataDriftPreset
from evidently.report import Report
import pandas as pd


def generate_report(reference_data: pd.DataFrame, current_data: pd.DataFrame) -> str:
    column_mapping = ColumnMapping(
        target="target",
        numerical_features=["num_feature"],
        categorical_features=["cat_feature"],
        prediction="prediction",
    )

    report = Report(metrics=[ClassificationPreset(), DataDriftPreset()])
    report.run(
        reference_data=reference_data, current_data=current_data, column_mapping=column_mapping
    )
    return report.get_html()
