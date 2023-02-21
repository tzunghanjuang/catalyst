
# Autogenerated by mlir-tblgen; don't manually edit.

from jaxlib.mlir.dialects._ods_common import _cext as _ods_cext
from jaxlib.mlir.dialects._ods_common import extend_opview_class as _ods_extend_opview_class, segmented_accessor as _ods_segmented_accessor, equally_sized_accessor as _ods_equally_sized_accessor, get_default_loc_context as _ods_get_default_loc_context, get_op_result_or_value as _get_op_result_or_value, get_op_results_or_values as _get_op_results_or_values
_ods_ir = _ods_cext.ir

try:
  from . import _quantum_ops_ext as _ods_ext_module
except ImportError:
  _ods_ext_module = None

import builtins


@_ods_cext.register_dialect
class _Dialect(_ods_ir.Dialect):
  DIALECT_NAMESPACE = "quantum"
  pass


@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class AllocOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.alloc"

  _ODS_REGIONS = (0, True)

  def __init__(self, qreg, *, nqubits=None, nqubits_attr=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    if nqubits is not None: operands.append(_get_op_result_or_value(nqubits))
    if nqubits_attr is not None: attributes["nqubits_attr"] = nqubits_attr
    results.append(qreg)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def nqubits(self):
    return None if len(self.operation.operands) < 1 else self.operation.operands[0]

  @builtins.property
  def nqubits_attr(self):
    if "nqubits_attr" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["nqubits_attr"])

  @nqubits_attr.setter
  def nqubits_attr(self, value):
    if value is not None:
      self.operation.attributes["nqubits_attr"] = value
    elif "nqubits_attr" in self.operation.attributes:
      del self.operation.attributes["nqubits_attr"]

  @nqubits_attr.deleter
  def nqubits_attr(self):
    del self.operation.attributes["nqubits_attr"]

  @builtins.property
  def qreg(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ComputationalBasisOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.compbasis"

  _ODS_REGIONS = (0, True)

  def __init__(self, obs, qubits, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(qubits))
    results.append(obs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def qubits(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def obs(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CountsOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.counts"

  _ODS_REGIONS = (0, True)

  def __init__(self, eigvals, counts, obs, shots, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    attributes["shots"] = shots
    results.append(eigvals)
    results.append(counts)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def shots(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["shots"])

  @shots.setter
  def shots(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["shots"] = value

  @builtins.property
  def eigvals(self):
    return self.operation.results[0]

  @builtins.property
  def counts(self):
    return self.operation.results[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class CustomOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.custom"

  _ODS_OPERAND_SEGMENTS = [-1,-1,]

  _ODS_REGIONS = (0, True)

  def __init__(self, out_qubits, params, in_qubits, gate_name, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_results_or_values(params))
    operands.append(_get_op_results_or_values(in_qubits))
    attributes["gate_name"] = gate_name
    results.extend(out_qubits)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def params(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 0)
    return operand_range

  @builtins.property
  def in_qubits(self):
    operand_range = _ods_segmented_accessor(
         self.operation.operands,
         self.operation.attributes["operand_segment_sizes"], 1)
    return operand_range

  @builtins.property
  def gate_name(self):
    return _ods_ir.StringAttr(self.operation.attributes["gate_name"])

  @gate_name.setter
  def gate_name(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["gate_name"] = value

  @builtins.property
  def out_qubits(self):
    _ods_variadic_group_length = len(self.operation.results) - 1 + 1
    return self.operation.results[0:0 + _ods_variadic_group_length]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class DeallocOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.dealloc"

  _ODS_REGIONS = (0, True)

  def __init__(self, qreg, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(qreg))
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def qreg(self):
    return self.operation.operands[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ExpvalOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.expval"

  _ODS_REGIONS = (0, True)

  def __init__(self, expval, obs, *, shots=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    if shots is not None: attributes["shots"] = shots
    results.append(expval)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def shots(self):
    if "shots" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["shots"])

  @shots.setter
  def shots(self, value):
    if value is not None:
      self.operation.attributes["shots"] = value
    elif "shots" in self.operation.attributes:
      del self.operation.attributes["shots"]

  @shots.deleter
  def shots(self):
    del self.operation.attributes["shots"]

  @builtins.property
  def expval(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ExtractOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.extract"

  _ODS_REGIONS = (0, True)

  def __init__(self, qubit, qreg, *, idx=None, idx_attr=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(qreg))
    if idx is not None: operands.append(_get_op_result_or_value(idx))
    if idx_attr is not None: attributes["idx_attr"] = idx_attr
    results.append(qubit)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def qreg(self):
    return self.operation.operands[0]

  @builtins.property
  def idx(self):
    return None if len(self.operation.operands) < 2 else self.operation.operands[1]

  @builtins.property
  def idx_attr(self):
    if "idx_attr" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["idx_attr"])

  @idx_attr.setter
  def idx_attr(self, value):
    if value is not None:
      self.operation.attributes["idx_attr"] = value
    elif "idx_attr" in self.operation.attributes:
      del self.operation.attributes["idx_attr"]

  @idx_attr.deleter
  def idx_attr(self):
    del self.operation.attributes["idx_attr"]

  @builtins.property
  def qubit(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class HamiltonianOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.hamiltonian"

  _ODS_REGIONS = (0, True)

  def __init__(self, obs, coeffs, terms, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(coeffs))
    operands.extend(_get_op_results_or_values(terms))
    results.append(obs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def coeffs(self):
    return self.operation.operands[0]

  @builtins.property
  def terms(self):
    _ods_variadic_group_length = len(self.operation.operands) - 2 + 1
    return self.operation.operands[1:1 + _ods_variadic_group_length]

  @builtins.property
  def obs(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class HermitianOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.hermitian"

  _ODS_REGIONS = (0, True)

  def __init__(self, obs, matrix, qubits, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(matrix))
    operands.extend(_get_op_results_or_values(qubits))
    results.append(obs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def matrix(self):
    return self.operation.operands[0]

  @builtins.property
  def qubits(self):
    _ods_variadic_group_length = len(self.operation.operands) - 2 + 1
    return self.operation.operands[1:1 + _ods_variadic_group_length]

  @builtins.property
  def obs(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class InsertOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.insert"

  _ODS_REGIONS = (0, True)

  def __init__(self, out_qreg, in_qreg, qubit, *, idx=None, idx_attr=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(in_qreg))
    if idx is not None: operands.append(_get_op_result_or_value(idx))
    operands.append(_get_op_result_or_value(qubit))
    if idx_attr is not None: attributes["idx_attr"] = idx_attr
    results.append(out_qreg)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def in_qreg(self):
    return self.operation.operands[0]

  @builtins.property
  def idx(self):
    return None if len(self.operation.operands) < 3 else self.operation.operands[1]

  @builtins.property
  def qubit(self):
    _ods_variadic_group_length = len(self.operation.operands) - 3 + 1
    return self.operation.operands[2 + _ods_variadic_group_length - 1]

  @builtins.property
  def idx_attr(self):
    if "idx_attr" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["idx_attr"])

  @idx_attr.setter
  def idx_attr(self, value):
    if value is not None:
      self.operation.attributes["idx_attr"] = value
    elif "idx_attr" in self.operation.attributes:
      del self.operation.attributes["idx_attr"]

  @idx_attr.deleter
  def idx_attr(self):
    del self.operation.attributes["idx_attr"]

  @builtins.property
  def out_qreg(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MeasureOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.measure"

  _ODS_REGIONS = (0, True)

  def __init__(self, mres, out_qubit, in_qubit, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(in_qubit))
    results.append(mres)
    results.append(out_qubit)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def in_qubit(self):
    return self.operation.operands[0]

  @builtins.property
  def mres(self):
    return self.operation.results[0]

  @builtins.property
  def out_qubit(self):
    return self.operation.results[1]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class MultiRZOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.multirz"

  _ODS_REGIONS = (0, True)

  def __init__(self, out_qubits, theta, in_qubits, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(theta))
    operands.extend(_get_op_results_or_values(in_qubits))
    results.extend(out_qubits)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def theta(self):
    return self.operation.operands[0]

  @builtins.property
  def in_qubits(self):
    _ods_variadic_group_length = len(self.operation.operands) - 2 + 1
    return self.operation.operands[1:1 + _ods_variadic_group_length]

  @builtins.property
  def out_qubits(self):
    _ods_variadic_group_length = len(self.operation.results) - 1 + 1
    return self.operation.results[0:0 + _ods_variadic_group_length]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class NamedObsOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.namedobs"

  _ODS_REGIONS = (0, True)

  def __init__(self, obs, qubit, type, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(qubit))
    attributes["type"] = type
    results.append(obs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def qubit(self):
    return self.operation.operands[0]

  @builtins.property
  def type(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["type"])

  @type.setter
  def type(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["type"] = value

  @builtins.property
  def obs(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class ProbsOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.probs"

  _ODS_REGIONS = (0, True)

  def __init__(self, probabilities, obs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    results.append(probabilities)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def probabilities(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class QubitUnitaryOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.unitary"

  _ODS_REGIONS = (0, True)

  def __init__(self, out_qubits, matrix, in_qubits, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(matrix))
    operands.extend(_get_op_results_or_values(in_qubits))
    results.extend(out_qubits)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def matrix(self):
    return self.operation.operands[0]

  @builtins.property
  def in_qubits(self):
    _ods_variadic_group_length = len(self.operation.operands) - 2 + 1
    return self.operation.operands[1:1 + _ods_variadic_group_length]

  @builtins.property
  def out_qubits(self):
    _ods_variadic_group_length = len(self.operation.results) - 1 + 1
    return self.operation.results[0:0 + _ods_variadic_group_length]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class SampleOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.sample"

  _ODS_REGIONS = (0, True)

  def __init__(self, samples, obs, shots, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    attributes["shots"] = shots
    results.append(samples)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def shots(self):
    return _ods_ir.IntegerAttr(self.operation.attributes["shots"])

  @shots.setter
  def shots(self, value):
    if value is None:
      raise ValueError("'None' not allowed as value for mandatory attributes")
    self.operation.attributes["shots"] = value

  @builtins.property
  def samples(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class StateOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.state"

  _ODS_REGIONS = (0, True)

  def __init__(self, state, obs, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    results.append(state)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def state(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class TensorOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.tensor"

  _ODS_REGIONS = (0, True)

  def __init__(self, obs, terms, *, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.extend(_get_op_results_or_values(terms))
    results.append(obs)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def terms(self):
    _ods_variadic_group_length = len(self.operation.operands) - 1 + 1
    return self.operation.operands[0:0 + _ods_variadic_group_length]

  @builtins.property
  def obs(self):
    return self.operation.results[0]

@_ods_cext.register_operation(_Dialect)
@_ods_extend_opview_class(_ods_ext_module)
class VarianceOp(_ods_ir.OpView):
  OPERATION_NAME = "quantum.var"

  _ODS_REGIONS = (0, True)

  def __init__(self, variance, obs, *, shots=None, loc=None, ip=None):
    operands = []
    results = []
    attributes = {}
    regions = None
    operands.append(_get_op_result_or_value(obs))
    if shots is not None: attributes["shots"] = shots
    results.append(variance)
    _ods_successors = None
    super().__init__(self.build_generic(
      attributes=attributes, results=results, operands=operands,
      successors=_ods_successors, regions=regions, loc=loc, ip=ip))

  @builtins.property
  def obs(self):
    return self.operation.operands[0]

  @builtins.property
  def shots(self):
    if "shots" not in self.operation.attributes:
      return None
    return _ods_ir.IntegerAttr(self.operation.attributes["shots"])

  @shots.setter
  def shots(self, value):
    if value is not None:
      self.operation.attributes["shots"] = value
    elif "shots" in self.operation.attributes:
      del self.operation.attributes["shots"]

  @shots.deleter
  def shots(self):
    del self.operation.attributes["shots"]

  @builtins.property
  def variance(self):
    return self.operation.results[0]
