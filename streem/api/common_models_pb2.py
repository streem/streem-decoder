# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streem/api/common_models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1estreem/api/common_models.proto\x12\nstreem.api\x1a\x19google/protobuf/any.proto\"(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\x02\x12\x0e\n\x06height\x18\x02 \x01(\x02\"*\n\x04Pose\x12\x10\n\x08position\x18\x01 \x03(\x02\x12\x10\n\x08rotation\x18\x02 \x03(\x02\">\n\tTransform\x12\x10\n\x08position\x18\x01 \x03(\x02\x12\x10\n\x08rotation\x18\x02 \x03(\x02\x12\r\n\x05scale\x18\x03 \x03(\x02\"\xb7\x01\n\rErrorResponse\x12\x15\n\thttp_code\x18\x01 \x01(\x05\x42\x02\x18\x01\x12\x13\n\x07message\x18\x02 \x01(\tB\x02\x18\x01\x12.\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1f.streem.api.ErrorResponse.Error\x1aJ\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\"\n\x04meta\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any*e\n\nVideoCodec\x12\x17\n\x13VIDEO_CODEC_INVALID\x10\x00\x12\x14\n\x10VIDEO_CODEC_H264\x10\x01\x12\x13\n\x0fVIDEO_CODEC_VP8\x10\x02\x12\x13\n\x0fVIDEO_CODEC_VP9\x10\x03*`\n\rVideoPlatform\x12\x1a\n\x16VIDEO_PLATFORM_INVALID\x10\x00\x12\x19\n\x15VIDEO_PLATFORM_TWILIO\x10\x01\x12\x18\n\x14VIDEO_PLATFORM_ARAAS\x10\x02*]\n\x0cWallPlatform\x12\x19\n\x15WALL_PLATFORM_INVALID\x10\x00\x12\x18\n\x14WALL_PLATFORM_TWILIO\x10\x01\x12\x18\n\x14WALL_PLATFORM_STREEM\x10\x02\x42?\n\x1epro.streem.commons.model.protoB\x11\x43ommonModelsProtoP\x01\xba\x02\x07Streem_b\x06proto3')

_VIDEOCODEC = DESCRIPTOR.enum_types_by_name['VideoCodec']
VideoCodec = enum_type_wrapper.EnumTypeWrapper(_VIDEOCODEC)
_VIDEOPLATFORM = DESCRIPTOR.enum_types_by_name['VideoPlatform']
VideoPlatform = enum_type_wrapper.EnumTypeWrapper(_VIDEOPLATFORM)
_WALLPLATFORM = DESCRIPTOR.enum_types_by_name['WallPlatform']
WallPlatform = enum_type_wrapper.EnumTypeWrapper(_WALLPLATFORM)
VIDEO_CODEC_INVALID = 0
VIDEO_CODEC_H264 = 1
VIDEO_CODEC_VP8 = 2
VIDEO_CODEC_VP9 = 3
VIDEO_PLATFORM_INVALID = 0
VIDEO_PLATFORM_TWILIO = 1
VIDEO_PLATFORM_ARAAS = 2
WALL_PLATFORM_INVALID = 0
WALL_PLATFORM_TWILIO = 1
WALL_PLATFORM_STREEM = 2


_POINT = DESCRIPTOR.message_types_by_name['Point']
_SIZE = DESCRIPTOR.message_types_by_name['Size']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_TRANSFORM = DESCRIPTOR.message_types_by_name['Transform']
_ERRORRESPONSE = DESCRIPTOR.message_types_by_name['ErrorResponse']
_ERRORRESPONSE_ERROR = _ERRORRESPONSE.nested_types_by_name['Error']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'streem.api.common_models_pb2'
  # @@protoc_insertion_point(class_scope:streem.api.Point)
  })
_sym_db.RegisterMessage(Point)

Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), {
  'DESCRIPTOR' : _SIZE,
  '__module__' : 'streem.api.common_models_pb2'
  # @@protoc_insertion_point(class_scope:streem.api.Size)
  })
_sym_db.RegisterMessage(Size)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'streem.api.common_models_pb2'
  # @@protoc_insertion_point(class_scope:streem.api.Pose)
  })
_sym_db.RegisterMessage(Pose)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORM,
  '__module__' : 'streem.api.common_models_pb2'
  # @@protoc_insertion_point(class_scope:streem.api.Transform)
  })
_sym_db.RegisterMessage(Transform)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), {

  'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
    'DESCRIPTOR' : _ERRORRESPONSE_ERROR,
    '__module__' : 'streem.api.common_models_pb2'
    # @@protoc_insertion_point(class_scope:streem.api.ErrorResponse.Error)
    })
  ,
  'DESCRIPTOR' : _ERRORRESPONSE,
  '__module__' : 'streem.api.common_models_pb2'
  # @@protoc_insertion_point(class_scope:streem.api.ErrorResponse)
  })
_sym_db.RegisterMessage(ErrorResponse)
_sym_db.RegisterMessage(ErrorResponse.Error)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036pro.streem.commons.model.protoB\021CommonModelsProtoP\001\272\002\007Streem_'
  _ERRORRESPONSE.fields_by_name['http_code']._options = None
  _ERRORRESPONSE.fields_by_name['http_code']._serialized_options = b'\030\001'
  _ERRORRESPONSE.fields_by_name['message']._options = None
  _ERRORRESPONSE.fields_by_name['message']._serialized_options = b'\030\001'
  _VIDEOCODEC._serialized_start=448
  _VIDEOCODEC._serialized_end=549
  _VIDEOPLATFORM._serialized_start=551
  _VIDEOPLATFORM._serialized_end=647
  _WALLPLATFORM._serialized_start=649
  _WALLPLATFORM._serialized_end=742
  _POINT._serialized_start=73
  _POINT._serialized_end=113
  _SIZE._serialized_start=115
  _SIZE._serialized_end=152
  _POSE._serialized_start=154
  _POSE._serialized_end=196
  _TRANSFORM._serialized_start=198
  _TRANSFORM._serialized_end=260
  _ERRORRESPONSE._serialized_start=263
  _ERRORRESPONSE._serialized_end=446
  _ERRORRESPONSE_ERROR._serialized_start=372
  _ERRORRESPONSE_ERROR._serialized_end=446
# @@protoc_insertion_point(module_scope)
