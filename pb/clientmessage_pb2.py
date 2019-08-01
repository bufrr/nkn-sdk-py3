# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/clientmessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/clientmessage.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16pb/clientmessage.proto\x12\x02pb\"M\n\rClientMessage\x12+\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x15.pb.ClientMessageType\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"\x93\x01\n\x0fOutboundMessage\x12\x0c\n\x04\x64\x65st\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\r\n\x05\x64\x65sts\x18\x03 \x03(\t\x12\x1b\n\x13max_holding_seconds\x18\x04 \x01(\r\x12\r\n\x05nonce\x18\x05 \x01(\r\x12\x12\n\nblock_hash\x18\x06 \x01(\x0c\x12\x12\n\nsignatures\x18\x07 \x03(\x0c\"F\n\x0eInboundMessage\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x16\n\x0eprev_signature\x18\x03 \x01(\x0c\"4\n\x07Receipt\x12\x16\n\x0eprev_signature\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c*K\n\x11\x43lientMessageType\x12\x14\n\x10OUTBOUND_MESSAGE\x10\x00\x12\x13\n\x0fINBOUND_MESSAGE\x10\x01\x12\x0b\n\x07RECEIPT\x10\x02\x62\x06proto3')
)

_CLIENTMESSAGETYPE = _descriptor.EnumDescriptor(
  name='ClientMessageType',
  full_name='pb.ClientMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OUTBOUND_MESSAGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INBOUND_MESSAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECEIPT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=385,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGETYPE)

ClientMessageType = enum_type_wrapper.EnumTypeWrapper(_CLIENTMESSAGETYPE)
OUTBOUND_MESSAGE = 0
INBOUND_MESSAGE = 1
RECEIPT = 2



_CLIENTMESSAGE = _descriptor.Descriptor(
  name='ClientMessage',
  full_name='pb.ClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='pb.ClientMessage.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pb.ClientMessage.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=30,
  serialized_end=107,
)


_OUTBOUNDMESSAGE = _descriptor.Descriptor(
  name='OutboundMessage',
  full_name='pb.OutboundMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dest', full_name='pb.OutboundMessage.dest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pb.OutboundMessage.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dests', full_name='pb.OutboundMessage.dests', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_holding_seconds', full_name='pb.OutboundMessage.max_holding_seconds', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='pb.OutboundMessage.nonce', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='pb.OutboundMessage.block_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='pb.OutboundMessage.signatures', index=6,
      number=7, type=12, cpp_type=9, label=3,
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
  serialized_start=110,
  serialized_end=257,
)


_INBOUNDMESSAGE = _descriptor.Descriptor(
  name='InboundMessage',
  full_name='pb.InboundMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='pb.InboundMessage.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pb.InboundMessage.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_signature', full_name='pb.InboundMessage.prev_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=259,
  serialized_end=329,
)


_RECEIPT = _descriptor.Descriptor(
  name='Receipt',
  full_name='pb.Receipt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prev_signature', full_name='pb.Receipt.prev_signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='pb.Receipt.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=331,
  serialized_end=383,
)

_CLIENTMESSAGE.fields_by_name['message_type'].enum_type = _CLIENTMESSAGETYPE
DESCRIPTOR.message_types_by_name['ClientMessage'] = _CLIENTMESSAGE
DESCRIPTOR.message_types_by_name['OutboundMessage'] = _OUTBOUNDMESSAGE
DESCRIPTOR.message_types_by_name['InboundMessage'] = _INBOUNDMESSAGE
DESCRIPTOR.message_types_by_name['Receipt'] = _RECEIPT
DESCRIPTOR.enum_types_by_name['ClientMessageType'] = _CLIENTMESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientMessage = _reflection.GeneratedProtocolMessageType('ClientMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMESSAGE,
  __module__ = 'pb.clientmessage_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClientMessage)
  ))
_sym_db.RegisterMessage(ClientMessage)

OutboundMessage = _reflection.GeneratedProtocolMessageType('OutboundMessage', (_message.Message,), dict(
  DESCRIPTOR = _OUTBOUNDMESSAGE,
  __module__ = 'pb.clientmessage_pb2'
  # @@protoc_insertion_point(class_scope:pb.OutboundMessage)
  ))
_sym_db.RegisterMessage(OutboundMessage)

InboundMessage = _reflection.GeneratedProtocolMessageType('InboundMessage', (_message.Message,), dict(
  DESCRIPTOR = _INBOUNDMESSAGE,
  __module__ = 'pb.clientmessage_pb2'
  # @@protoc_insertion_point(class_scope:pb.InboundMessage)
  ))
_sym_db.RegisterMessage(InboundMessage)

Receipt = _reflection.GeneratedProtocolMessageType('Receipt', (_message.Message,), dict(
  DESCRIPTOR = _RECEIPT,
  __module__ = 'pb.clientmessage_pb2'
  # @@protoc_insertion_point(class_scope:pb.Receipt)
  ))
_sym_db.RegisterMessage(Receipt)


# @@protoc_insertion_point(module_scope)