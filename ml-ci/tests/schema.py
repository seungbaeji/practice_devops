import numpy as np
from pandera import SeriesSchema, DataFrameSchema, Column, Check, Index


check_positive = Check(lambda x: x > 0)

iris_data_schema = DataFrameSchema(
    columns={
        "sepal_length": Column(float, check_positive),
        "sepal_width": Column(float, check_positive),
        "petal_length": Column(float, check_positive),
        "petal_width": Column(float, check_positive),
    },
    index=Index(int, name=None)
)

iris_target_schema = SeriesSchema(
    np.int64,
    checks = [Check.in_range(0, 2)],
    nullable=False,
    index=Index(int, name=None)
)
