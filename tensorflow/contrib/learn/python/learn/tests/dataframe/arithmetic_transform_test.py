# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Tests for arithmetic transforms."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.contrib.learn.python.learn.dataframe import tensorflow_dataframe as df


class SumTestCase(tf.test.TestCase):
  """Test class for `Sum` transform."""

  def testSum(self):
    num_rows = 100

    pandas_df = pd.DataFrame({"a": np.arange(num_rows),
                              "b": np.arange(num_rows, 2 * num_rows)})

    frame = df.TensorFlowDataFrame.from_pandas(
        pandas_df, shuffle=False, batch_size=num_rows)

    frame["a+b"] = frame["a"] + frame["b"]

    expected_sum = pandas_df["a"] + pandas_df["b"]
    actual_sum = frame.run_once()["a+b"]
    np.testing.assert_array_equal(expected_sum, actual_sum)


if __name__ == "__main__":
  tf.test.main()
