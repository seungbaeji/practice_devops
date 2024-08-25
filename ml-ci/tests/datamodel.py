import pandera as pa
from pandera.typing import Index, DataFrame, Series

class IrisDataModel(pa.DataFrameModel):
    idx: Index[int] = pa.Index(ge=0)
    sepal_length: Series[float] = pa.Field(ge=0)
    sepal_width: Series[float] = pa.Field(ge=0)
    petal_length: Series[float] = pa.Field(ge=0)
    petal_width: Series[float] = pa.Field(ge=0)

    class Config:
        stric = True

class IrisTargetModel(pa.DataFrameModel):
    idx: Index[int] = pa.Index(ge=0)
    target: Series[int] = pa.Field(in_range={"min_value": 0, "max_value": 2}, nullable=False)
