from typing import TypeVar, Generic
import pandas as pd

T = TypeVar('T')
ColumnType = TypeVar('ColumnType')

class Index(Generic[T], pd.Index):
    pass

class Series(Generic[T], pd.Series):
    pass

class IrisData(Generic[T], pd.DataFrame):
    idx: Index[int]
    sepal_length: Series[float]
    sepal_width: Series[float]
    petal_length: Series[float]
    petal_width: Series[float]


class IrisTarget(Series):
    idx: Index[int]
