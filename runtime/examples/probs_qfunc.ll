; Copyright 2022-2023 Xanadu Quantum Technologies Inc.

; Licensed under the Apache License, Version 2.0 (the "License");
; you may not use this file except in compliance with the License.
; You may obtain a copy of the License at

;     http://www.apache.org/licenses/LICENSE-2.0

; Unless required by applicable law or agreed to in writing, software
; distributed under the License is distributed on an "AS IS" BASIS,
; WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
; See the License for the specific language governing permissions and
; limitations under the License.

; ModuleID = 'probs_qfunc'
source_filename = "probs_qfunc"
target triple = "x86_64-pc-linux-gnu"

%Result = type opaque
%Qubit = type opaque
%Array = type opaque

%struct.MemRefT = type { double*, double*, i64, [1 x i64], [1 x i64] }

@.str = private constant [16 x i8] c"probs[%d] = %f\0A\00", align 1

declare void @__quantum__rt__initialize()

declare void @__quantum__rt__finalize()

declare void @__quantum__qis__RY(%Qubit*, double, i8)

declare void @__quantum__qis__Hadamard(%Qubit*, i8)

declare i8* @__quantum__rt__array_get_element_ptr_1d(%Array*, i64)

declare %Array* @__quantum__rt__qubit_allocate_array(i64)

declare void @__quantum__qis__Probs(%struct.MemRefT*, i64)

declare i8* @malloc(i64)

declare i32 @printf(i8*, ...)

declare void @free(i8*)

; Print probabilities at index
define void @print_probs_at(double* %0, i64 %1) {
  %3 = getelementptr inbounds double, double* %0, i64 %1
  %4 = load double, double* %3, align 8
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str, i64 0, i64 0), i64 %1, double %4)
  ret void
}

define i32 @main() {
  ; Initialize quantum runtime
  call void @__quantum__rt__initialize()

  ; Allocate 2 qubits
  %1 = call %Array* @__quantum__rt__qubit_allocate_array(i64 2)
  %2 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %1, i64 0)
  %3 = bitcast i8* %2 to %Qubit**
  %4 = load %Qubit*, %Qubit** %3, align 8

  ; Apply quantum operations
  call void @__quantum__qis__Hadamard(%Qubit* %4, i8 0)
  call void @__quantum__qis__RY(%Qubit* %4, double 0.7, i8 0)

  ; Apply the measurement process (probability)
  %5 = call i8* @malloc(i64 40)
  %6 = bitcast i8* %5 to %struct.MemRefT*
  call void @__quantum__qis__Probs(%struct.MemRefT* %6, i64 0)

  ; Print results
  %7 = getelementptr %struct.MemRefT, %struct.MemRefT* %6, i32 0, i32 0
  %8 = load double*, double** %7, align 8
  call void @print_probs_at(double* %8, i64 0)
  call void @print_probs_at(double* %8, i64 1)
  call void @print_probs_at(double* %8, i64 2)
  call void @print_probs_at(double* %8, i64 3)

  ; Close the context and free memory
  call void @free(i8* %5)
  call void @__quantum__rt__finalize()
  ret i32 0
}
