# Copyright 2022-2023 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import jax


class Signature:
    """Signature: class representing a python's function signature. Used for
    type deduction during abstract evaluation.

    Args:
        xs: the domain of the function
        ys: the range of the function
    """

    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def __repr__(self):
        return "{} -> {}".format(self.xs, self.ys)

    def get_input(self, i):
        return self.xs[i]

    def get_inputs(self):
        return self.xs

    def get_result(self, i):
        return self.ys[i]

    def get_results(self):
        return self.ys

    @staticmethod
    def is_tensor(x):
        return isinstance(x, jax.core.ShapedArray)


def calculate_grad_shape(signature, indices):
    """calculate_grad_shape: Given a signature and a list of indices over which arguments
    to differentiate, deduce the new signature.

    Args:
        signature: a signature.
        indices: a list of integers that correspond to parameters in signature s.
    """
    grad_result_types = []
    for index in indices:
        diff_arg_type = signature.get_input(index)
        diff_arg_shape = []

        if Signature.is_tensor(diff_arg_type):
            for axis in diff_arg_type.shape:
                diff_arg_shape.append(axis)

        for y in signature.get_results():
            grad_res_shape = diff_arg_shape
            if Signature.is_tensor(y):
                for axis in y.shape:
                    grad_res_shape.append(axis)
                element_type = y.dtype

            grad_res_type = (
                jax.core.ShapedArray(grad_res_shape, element_type) if grad_res_shape else y
            )
            grad_result_types.append(grad_res_type)

    return Signature(signature.get_inputs(), grad_result_types)
