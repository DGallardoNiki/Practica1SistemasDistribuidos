# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WordCount.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WordCount.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fWordCount.proto\"D\n\x0egetInformation\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x0e\n\x06option\x18\x02 \x01(\x05\x12\x10\n\x08idWorker\x18\x03 \x01(\x05\"\x1c\n\x08\x66ileData\x12\x10\n\x08\x66ileData\x18\x01 \x01(\t\"!\n\temptyData\x12\x14\n\x0c\x65mptyMessage\x18\x01 \x01(\t2a\n\tWordCount\x12*\n\nelContador\x12\x0f.getInformation\x1a\t.fileData\"\x00\x12(\n\x0cmensajeVacio\x12\n.emptyData\x1a\n.emptyData\"\x00\x62\x06proto3'
)




_GETINFORMATION = _descriptor.Descriptor(
  name='getInformation',
  full_name='getInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='getInformation.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='option', full_name='getInformation.option', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idWorker', full_name='getInformation.idWorker', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=19,
  serialized_end=87,
)


_FILEDATA = _descriptor.Descriptor(
  name='fileData',
  full_name='fileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileData', full_name='fileData.fileData', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=89,
  serialized_end=117,
)


_EMPTYDATA = _descriptor.Descriptor(
  name='emptyData',
  full_name='emptyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='emptyMessage', full_name='emptyData.emptyMessage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=119,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['getInformation'] = _GETINFORMATION
DESCRIPTOR.message_types_by_name['fileData'] = _FILEDATA
DESCRIPTOR.message_types_by_name['emptyData'] = _EMPTYDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

getInformation = _reflection.GeneratedProtocolMessageType('getInformation', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORMATION,
  '__module__' : 'WordCount_pb2'
  # @@protoc_insertion_point(class_scope:getInformation)
  })
_sym_db.RegisterMessage(getInformation)

fileData = _reflection.GeneratedProtocolMessageType('fileData', (_message.Message,), {
  'DESCRIPTOR' : _FILEDATA,
  '__module__' : 'WordCount_pb2'
  # @@protoc_insertion_point(class_scope:fileData)
  })
_sym_db.RegisterMessage(fileData)

emptyData = _reflection.GeneratedProtocolMessageType('emptyData', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYDATA,
  '__module__' : 'WordCount_pb2'
  # @@protoc_insertion_point(class_scope:emptyData)
  })
_sym_db.RegisterMessage(emptyData)



_WORDCOUNT = _descriptor.ServiceDescriptor(
  name='WordCount',
  full_name='WordCount',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=154,
  serialized_end=251,
  methods=[
  _descriptor.MethodDescriptor(
    name='elContador',
    full_name='WordCount.elContador',
    index=0,
    containing_service=None,
    input_type=_GETINFORMATION,
    output_type=_FILEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='mensajeVacio',
    full_name='WordCount.mensajeVacio',
    index=1,
    containing_service=None,
    input_type=_EMPTYDATA,
    output_type=_EMPTYDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORDCOUNT)

DESCRIPTOR.services_by_name['WordCount'] = _WORDCOUNT

# @@protoc_insertion_point(module_scope)