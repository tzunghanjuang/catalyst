// Copyright 2022-2023 Xanadu Quantum Technologies Inc.

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <complex>
#include <stdexcept>
#include <vector>

#include "Types.h"

#if __has_include("StateVectorKokkos.hpp")
// this macro is used in the C++ test suite
#define _KOKKOS
#endif

namespace Catalyst::Runtime::Simulator {
template <typename T> using VectorCplxT = std::vector<std::complex<T>>;

static void QFailIf(bool condition, const char *message)
{
    if (condition) {
        throw std::runtime_error(message);
    }
}
} // namespace Catalyst::Runtime::Simulator
