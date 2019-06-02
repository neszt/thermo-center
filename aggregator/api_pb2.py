# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aggregator/api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aggregator/api.proto',
  package='aggregator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x61ggregator/api.proto\x12\naggregator\"O\n\x0cSensorPacket\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x0c\n\x04rssi\x18\x03 \x01(\x02\x12\x0b\n\x03lqi\x18\x04 \x01(\r\x12\x0b\n\x03raw\x18\x05 \x01(\x0c\"!\n\x0c\x46\x65\x65\x64Response\x12\x11\n\tprocessed\x18\x01 \x01(\x08\x32V\n\nAggregator\x12H\n\x10\x46\x65\x65\x64SensorPacket\x12\x18.aggregator.SensorPacket\x1a\x18.aggregator.FeedResponse\"\x00\x62\x06proto3')
)




_SENSORPACKET = _descriptor.Descriptor(
  name='SensorPacket',
  full_name='aggregator.SensorPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='aggregator.SensorPacket.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='aggregator.SensorPacket.seq', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='aggregator.SensorPacket.rssi', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lqi', full_name='aggregator.SensorPacket.lqi', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='aggregator.SensorPacket.raw', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=115,
)


_FEEDRESPONSE = _descriptor.Descriptor(
  name='FeedResponse',
  full_name='aggregator.FeedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processed', full_name='aggregator.FeedResponse.processed', index=0,
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
  serialized_start=117,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['SensorPacket'] = _SENSORPACKET
DESCRIPTOR.message_types_by_name['FeedResponse'] = _FEEDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorPacket = _reflection.GeneratedProtocolMessageType('SensorPacket', (_message.Message,), dict(
  DESCRIPTOR = _SENSORPACKET,
  __module__ = 'aggregator.api_pb2'
  # @@protoc_insertion_point(class_scope:aggregator.SensorPacket)
  ))
_sym_db.RegisterMessage(SensorPacket)

FeedResponse = _reflection.GeneratedProtocolMessageType('FeedResponse', (_message.Message,), dict(
  DESCRIPTOR = _FEEDRESPONSE,
  __module__ = 'aggregator.api_pb2'
  # @@protoc_insertion_point(class_scope:aggregator.FeedResponse)
  ))
_sym_db.RegisterMessage(FeedResponse)



_AGGREGATOR = _descriptor.ServiceDescriptor(
  name='Aggregator',
  full_name='aggregator.Aggregator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=152,
  serialized_end=238,
  methods=[
  _descriptor.MethodDescriptor(
    name='FeedSensorPacket',
    full_name='aggregator.Aggregator.FeedSensorPacket',
    index=0,
    containing_service=None,
    input_type=_SENSORPACKET,
    output_type=_FEEDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGGREGATOR)

DESCRIPTOR.services_by_name['Aggregator'] = _AGGREGATOR

# @@protoc_insertion_point(module_scope)
