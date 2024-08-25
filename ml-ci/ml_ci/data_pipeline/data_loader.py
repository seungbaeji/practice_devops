import pandas as pd
from sklearn.datasets import load_iris

from .data_model import IrisData, IrisTarget


def load_iris_data() -> tuple[IrisData, IrisTarget]:
    dataset = load_iris(as_frame=True)
    iris_data: pd.DataFrame = dataset['data']
    iris_target: pd.Series = dataset['target']

    iris_data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    return iris_data, iris_target
