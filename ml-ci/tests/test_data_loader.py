import pandas as pd

from ml_ci.data_pipeline.data_loader import load_iris_data
from .schema import iris_data_schema, iris_target_schema


def test_load_iris_data() -> tuple[pd.DataFrame, pd.Series]:
    data, target = load_iris_data()
    assert data.shape == (150, 4)  # 피처는 150개의 샘플과 4개의 피처로 구성
    assert len(target) == 150  # 타겟은 150개의 값으로 구성

    validated_data = iris_data_schema.validate(data)
    validated_target = iris_target_schema.validate(target)

    assert validated_data.equals(data)
    assert validated_target.equals(target)

