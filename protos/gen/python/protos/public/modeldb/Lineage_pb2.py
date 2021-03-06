# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modeldb/Lineage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modeldb/Lineage.proto',
  package='ai.verta.modeldb',
  syntax='proto3',
  serialized_options=b'P\001Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb',
  serialized_pb=b'\n\x15modeldb/Lineage.proto\x12\x10\x61i.verta.modeldb\x1a\x1cgoogle/api/annotations.proto\"\\\n\x10LineageEntryEnum\"H\n\x10LineageEntryType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0e\x45XPERIMENT_RUN\x10\x01\x12\x13\n\x0f\x44\x41TASET_VERSION\x10\x02\"w\n\x0cLineageEntry\x12\x41\n\x04type\x18\x01 \x01(\x0e\x32\x33.ai.verta.modeldb.LineageEntryEnum.LineageEntryType\x12\x15\n\x0b\x65xternal_id\x18\x02 \x01(\tH\x00\x42\r\n\x0b\x64\x65scription\"B\n\x11LineageEntryBatch\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\"\x87\x01\n\nAddLineage\x12-\n\x05input\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x12.\n\x06output\x18\x02 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x8a\x01\n\rDeleteLineage\x12-\n\x05input\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x12.\n\x06output\x18\x02 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\x7f\n\rFindAllInputs\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x1a?\n\x08Response\x12\x33\n\x06inputs\x18\x01 \x03(\x0b\x32#.ai.verta.modeldb.LineageEntryBatch\"\x81\x01\n\x0e\x46indAllOutputs\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x1a@\n\x08Response\x12\x34\n\x07outputs\x18\x01 \x03(\x0b\x32#.ai.verta.modeldb.LineageEntryBatch\"\xbc\x01\n\x14\x46indAllInputsOutputs\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.ai.verta.modeldb.LineageEntry\x1au\n\x08Response\x12\x33\n\x06inputs\x18\x01 \x03(\x0b\x32#.ai.verta.modeldb.LineageEntryBatch\x12\x34\n\x07outputs\x18\x02 \x03(\x0b\x32#.ai.verta.modeldb.LineageEntryBatch2\xb2\x05\n\x0eLineageService\x12t\n\naddLineage\x12\x1c.ai.verta.modeldb.AddLineage\x1a%.ai.verta.modeldb.AddLineage.Response\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/lineage/addLineage:\x01*\x12\x80\x01\n\rdeleteLineage\x12\x1f.ai.verta.modeldb.DeleteLineage\x1a(.ai.verta.modeldb.DeleteLineage.Response\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/lineage/deleteLineage:\x01*\x12\x80\x01\n\rfindAllInputs\x12\x1f.ai.verta.modeldb.FindAllInputs\x1a(.ai.verta.modeldb.FindAllInputs.Response\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/lineage/findAllInputs:\x01*\x12\x84\x01\n\x0e\x66indAllOutputs\x12 .ai.verta.modeldb.FindAllOutputs\x1a).ai.verta.modeldb.FindAllOutputs.Response\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/lineage/findAllOutputs:\x01*\x12\x9c\x01\n\x14\x66indAllInputsOutputs\x12&.ai.verta.modeldb.FindAllInputsOutputs\x1a/.ai.verta.modeldb.FindAllInputsOutputs.Response\"+\x82\xd3\xe4\x93\x02%\" /v1/lineage/findAllInputsOutputs:\x01*BBP\x01Z>github.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldbb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_LINEAGEENTRYENUM_LINEAGEENTRYTYPE = _descriptor.EnumDescriptor(
  name='LineageEntryType',
  full_name='ai.verta.modeldb.LineageEntryEnum.LineageEntryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPERIMENT_RUN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATASET_VERSION', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=93,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_LINEAGEENTRYENUM_LINEAGEENTRYTYPE)


_LINEAGEENTRYENUM = _descriptor.Descriptor(
  name='LineageEntryEnum',
  full_name='ai.verta.modeldb.LineageEntryEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LINEAGEENTRYENUM_LINEAGEENTRYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=165,
)


_LINEAGEENTRY = _descriptor.Descriptor(
  name='LineageEntry',
  full_name='ai.verta.modeldb.LineageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ai.verta.modeldb.LineageEntry.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_id', full_name='ai.verta.modeldb.LineageEntry.external_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='description', full_name='ai.verta.modeldb.LineageEntry.description',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=167,
  serialized_end=286,
)


_LINEAGEENTRYBATCH = _descriptor.Descriptor(
  name='LineageEntryBatch',
  full_name='ai.verta.modeldb.LineageEntryBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ai.verta.modeldb.LineageEntryBatch.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=354,
)


_ADDLINEAGE_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.AddLineage.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.modeldb.AddLineage.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=492,
)

_ADDLINEAGE = _descriptor.Descriptor(
  name='AddLineage',
  full_name='ai.verta.modeldb.AddLineage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='ai.verta.modeldb.AddLineage.input', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='ai.verta.modeldb.AddLineage.output', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADDLINEAGE_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=492,
)


_DELETELINEAGE_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.DeleteLineage.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.modeldb.DeleteLineage.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=492,
)

_DELETELINEAGE = _descriptor.Descriptor(
  name='DeleteLineage',
  full_name='ai.verta.modeldb.DeleteLineage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='ai.verta.modeldb.DeleteLineage.input', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='ai.verta.modeldb.DeleteLineage.output', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETELINEAGE_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=633,
)


_FINDALLINPUTS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.FindAllInputs.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='ai.verta.modeldb.FindAllInputs.Response.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=699,
  serialized_end=762,
)

_FINDALLINPUTS = _descriptor.Descriptor(
  name='FindAllInputs',
  full_name='ai.verta.modeldb.FindAllInputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ai.verta.modeldb.FindAllInputs.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDALLINPUTS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=762,
)


_FINDALLOUTPUTS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.FindAllOutputs.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='ai.verta.modeldb.FindAllOutputs.Response.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=894,
)

_FINDALLOUTPUTS = _descriptor.Descriptor(
  name='FindAllOutputs',
  full_name='ai.verta.modeldb.FindAllOutputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ai.verta.modeldb.FindAllOutputs.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDALLOUTPUTS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=894,
)


_FINDALLINPUTSOUTPUTS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.modeldb.FindAllInputsOutputs.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='ai.verta.modeldb.FindAllInputsOutputs.Response.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='ai.verta.modeldb.FindAllInputsOutputs.Response.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1085,
)

_FINDALLINPUTSOUTPUTS = _descriptor.Descriptor(
  name='FindAllInputsOutputs',
  full_name='ai.verta.modeldb.FindAllInputsOutputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='ai.verta.modeldb.FindAllInputsOutputs.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDALLINPUTSOUTPUTS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=897,
  serialized_end=1085,
)

_LINEAGEENTRYENUM_LINEAGEENTRYTYPE.containing_type = _LINEAGEENTRYENUM
_LINEAGEENTRY.fields_by_name['type'].enum_type = _LINEAGEENTRYENUM_LINEAGEENTRYTYPE
_LINEAGEENTRY.oneofs_by_name['description'].fields.append(
  _LINEAGEENTRY.fields_by_name['external_id'])
_LINEAGEENTRY.fields_by_name['external_id'].containing_oneof = _LINEAGEENTRY.oneofs_by_name['description']
_LINEAGEENTRYBATCH.fields_by_name['items'].message_type = _LINEAGEENTRY
_ADDLINEAGE_RESPONSE.containing_type = _ADDLINEAGE
_ADDLINEAGE.fields_by_name['input'].message_type = _LINEAGEENTRY
_ADDLINEAGE.fields_by_name['output'].message_type = _LINEAGEENTRY
_DELETELINEAGE_RESPONSE.containing_type = _DELETELINEAGE
_DELETELINEAGE.fields_by_name['input'].message_type = _LINEAGEENTRY
_DELETELINEAGE.fields_by_name['output'].message_type = _LINEAGEENTRY
_FINDALLINPUTS_RESPONSE.fields_by_name['inputs'].message_type = _LINEAGEENTRYBATCH
_FINDALLINPUTS_RESPONSE.containing_type = _FINDALLINPUTS
_FINDALLINPUTS.fields_by_name['items'].message_type = _LINEAGEENTRY
_FINDALLOUTPUTS_RESPONSE.fields_by_name['outputs'].message_type = _LINEAGEENTRYBATCH
_FINDALLOUTPUTS_RESPONSE.containing_type = _FINDALLOUTPUTS
_FINDALLOUTPUTS.fields_by_name['items'].message_type = _LINEAGEENTRY
_FINDALLINPUTSOUTPUTS_RESPONSE.fields_by_name['inputs'].message_type = _LINEAGEENTRYBATCH
_FINDALLINPUTSOUTPUTS_RESPONSE.fields_by_name['outputs'].message_type = _LINEAGEENTRYBATCH
_FINDALLINPUTSOUTPUTS_RESPONSE.containing_type = _FINDALLINPUTSOUTPUTS
_FINDALLINPUTSOUTPUTS.fields_by_name['items'].message_type = _LINEAGEENTRY
DESCRIPTOR.message_types_by_name['LineageEntryEnum'] = _LINEAGEENTRYENUM
DESCRIPTOR.message_types_by_name['LineageEntry'] = _LINEAGEENTRY
DESCRIPTOR.message_types_by_name['LineageEntryBatch'] = _LINEAGEENTRYBATCH
DESCRIPTOR.message_types_by_name['AddLineage'] = _ADDLINEAGE
DESCRIPTOR.message_types_by_name['DeleteLineage'] = _DELETELINEAGE
DESCRIPTOR.message_types_by_name['FindAllInputs'] = _FINDALLINPUTS
DESCRIPTOR.message_types_by_name['FindAllOutputs'] = _FINDALLOUTPUTS
DESCRIPTOR.message_types_by_name['FindAllInputsOutputs'] = _FINDALLINPUTSOUTPUTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LineageEntryEnum = _reflection.GeneratedProtocolMessageType('LineageEntryEnum', (_message.Message,), {
  'DESCRIPTOR' : _LINEAGEENTRYENUM,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.LineageEntryEnum)
  })
_sym_db.RegisterMessage(LineageEntryEnum)

LineageEntry = _reflection.GeneratedProtocolMessageType('LineageEntry', (_message.Message,), {
  'DESCRIPTOR' : _LINEAGEENTRY,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.LineageEntry)
  })
_sym_db.RegisterMessage(LineageEntry)

LineageEntryBatch = _reflection.GeneratedProtocolMessageType('LineageEntryBatch', (_message.Message,), {
  'DESCRIPTOR' : _LINEAGEENTRYBATCH,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.LineageEntryBatch)
  })
_sym_db.RegisterMessage(LineageEntryBatch)

AddLineage = _reflection.GeneratedProtocolMessageType('AddLineage', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _ADDLINEAGE_RESPONSE,
    '__module__' : 'modeldb.Lineage_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.AddLineage.Response)
    })
  ,
  'DESCRIPTOR' : _ADDLINEAGE,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.AddLineage)
  })
_sym_db.RegisterMessage(AddLineage)
_sym_db.RegisterMessage(AddLineage.Response)

DeleteLineage = _reflection.GeneratedProtocolMessageType('DeleteLineage', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _DELETELINEAGE_RESPONSE,
    '__module__' : 'modeldb.Lineage_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteLineage.Response)
    })
  ,
  'DESCRIPTOR' : _DELETELINEAGE,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.DeleteLineage)
  })
_sym_db.RegisterMessage(DeleteLineage)
_sym_db.RegisterMessage(DeleteLineage.Response)

FindAllInputs = _reflection.GeneratedProtocolMessageType('FindAllInputs', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDALLINPUTS_RESPONSE,
    '__module__' : 'modeldb.Lineage_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllInputs.Response)
    })
  ,
  'DESCRIPTOR' : _FINDALLINPUTS,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllInputs)
  })
_sym_db.RegisterMessage(FindAllInputs)
_sym_db.RegisterMessage(FindAllInputs.Response)

FindAllOutputs = _reflection.GeneratedProtocolMessageType('FindAllOutputs', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDALLOUTPUTS_RESPONSE,
    '__module__' : 'modeldb.Lineage_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllOutputs.Response)
    })
  ,
  'DESCRIPTOR' : _FINDALLOUTPUTS,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllOutputs)
  })
_sym_db.RegisterMessage(FindAllOutputs)
_sym_db.RegisterMessage(FindAllOutputs.Response)

FindAllInputsOutputs = _reflection.GeneratedProtocolMessageType('FindAllInputsOutputs', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDALLINPUTSOUTPUTS_RESPONSE,
    '__module__' : 'modeldb.Lineage_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllInputsOutputs.Response)
    })
  ,
  'DESCRIPTOR' : _FINDALLINPUTSOUTPUTS,
  '__module__' : 'modeldb.Lineage_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.FindAllInputsOutputs)
  })
_sym_db.RegisterMessage(FindAllInputsOutputs)
_sym_db.RegisterMessage(FindAllInputsOutputs.Response)


DESCRIPTOR._options = None

_LINEAGESERVICE = _descriptor.ServiceDescriptor(
  name='LineageService',
  full_name='ai.verta.modeldb.LineageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1088,
  serialized_end=1778,
  methods=[
  _descriptor.MethodDescriptor(
    name='addLineage',
    full_name='ai.verta.modeldb.LineageService.addLineage',
    index=0,
    containing_service=None,
    input_type=_ADDLINEAGE,
    output_type=_ADDLINEAGE_RESPONSE,
    serialized_options=b'\202\323\344\223\002\033\"\026/v1/lineage/addLineage:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='deleteLineage',
    full_name='ai.verta.modeldb.LineageService.deleteLineage',
    index=1,
    containing_service=None,
    input_type=_DELETELINEAGE,
    output_type=_DELETELINEAGE_RESPONSE,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/lineage/deleteLineage:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findAllInputs',
    full_name='ai.verta.modeldb.LineageService.findAllInputs',
    index=2,
    containing_service=None,
    input_type=_FINDALLINPUTS,
    output_type=_FINDALLINPUTS_RESPONSE,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/lineage/findAllInputs:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findAllOutputs',
    full_name='ai.verta.modeldb.LineageService.findAllOutputs',
    index=3,
    containing_service=None,
    input_type=_FINDALLOUTPUTS,
    output_type=_FINDALLOUTPUTS_RESPONSE,
    serialized_options=b'\202\323\344\223\002\037\"\032/v1/lineage/findAllOutputs:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findAllInputsOutputs',
    full_name='ai.verta.modeldb.LineageService.findAllInputsOutputs',
    index=4,
    containing_service=None,
    input_type=_FINDALLINPUTSOUTPUTS,
    output_type=_FINDALLINPUTSOUTPUTS_RESPONSE,
    serialized_options=b'\202\323\344\223\002%\" /v1/lineage/findAllInputsOutputs:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_LINEAGESERVICE)

DESCRIPTOR.services_by_name['LineageService'] = _LINEAGESERVICE

# @@protoc_insertion_point(module_scope)
