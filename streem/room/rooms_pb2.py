# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streem/room/rooms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17streem/room/rooms.proto\")\n\nRoomString\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\x91\x01\n\x10\x43\x61meraIntrinsics\x12\x19\n\x11\x66ocal_length_px_x\x18\x01 \x01(\x02\x12\x19\n\x11\x66ocal_length_px_y\x18\x02 \x01(\x02\x12\x11\n\taxis_skew\x18\x03 \x01(\x02\x12\x19\n\x11principal_point_x\x18\x04 \x01(\x02\x12\x19\n\x11principal_point_y\x18\x05 \x01(\x02\"\x86\x04\n\x0cVectorBuffer\x12\r\n\x05\x62ytes\x18\x01 \x01(\x0c\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x33\n\x0e\x63omponent_type\x18\x03 \x01(\x0e\x32\x1b.VectorBuffer.ComponentType\x12\x18\n\x10\x63omponent_stride\x18\x04 \x01(\x05\x12\x1d\n\x15\x63omponents_per_vector\x18\x05 \x01(\x05\x12\x15\n\rvector_stride\x18\x06 \x01(\x05\x12\x14\n\x0cvector_count\x18\x07 \x01(\x05\x12+\n\nbyte_order\x18\x08 \x01(\x0e\x32\x17.VectorBuffer.ByteOrder\"\xb0\x01\n\rComponentType\x12\x1a\n\x16\x43OMPONENT_TYPE_INVALID\x10\x00\x12\x18\n\x14\x43OMPONENT_TYPE_FLOAT\x10\x01\x12\x19\n\x15\x43OMPONENT_TYPE_DOUBLE\x10\x02\x12\x19\n\x15\x43OMPONENT_TYPE_UINT32\x10\x03\x12\x18\n\x14\x43OMPONENT_TYPE_UINT8\x10\x04\x12\x19\n\x15\x43OMPONENT_TYPE_UINT16\x10\x05\"\\\n\tByteOrder\x12\x16\n\x12\x42YTE_ORDER_INVALID\x10\x00\x12\x19\n\x15\x42YTE_ORDER_BIG_ENDIAN\x10\x01\x12\x1c\n\x18\x42YTE_ORDER_LITTLE_ENDIAN\x10\x02*_\n\rCameraSubject\x12\x18\n\x14\x43\x41MERA_SUBJECT_WORLD\x10\x00\x12\x19\n\x15\x43\x41MERA_SUBJECT_PERSON\x10\x01\x12\x19\n\x15\x43\x41MERA_SUBJECT_SCREEN\x10\x02*\xa0\x01\n\x18StreamingMessageProvider\x12&\n\"STREAMING_MESSAGE_PROVIDER_INVALID\x10\x00\x12\x31\n-STREAMING_MESSAGE_PROVIDER_TWILIO_SYNC_STREAM\x10\x01\x12)\n%STREAMING_MESSAGE_PROVIDER_DATA_TRACK\x10\x02\x42/\n\x16pro.streem.model.protoB\x05Rooms\xba\x02\rStreem_Rooms_b\x06proto3')

_CAMERASUBJECT = DESCRIPTOR.enum_types_by_name['CameraSubject']
CameraSubject = enum_type_wrapper.EnumTypeWrapper(_CAMERASUBJECT)
_STREAMINGMESSAGEPROVIDER = DESCRIPTOR.enum_types_by_name['StreamingMessageProvider']
StreamingMessageProvider = enum_type_wrapper.EnumTypeWrapper(_STREAMINGMESSAGEPROVIDER)
CAMERA_SUBJECT_WORLD = 0
CAMERA_SUBJECT_PERSON = 1
CAMERA_SUBJECT_SCREEN = 2
STREAMING_MESSAGE_PROVIDER_INVALID = 0
STREAMING_MESSAGE_PROVIDER_TWILIO_SYNC_STREAM = 1
STREAMING_MESSAGE_PROVIDER_DATA_TRACK = 2


_ROOMSTRING = DESCRIPTOR.message_types_by_name['RoomString']
_CAMERAINTRINSICS = DESCRIPTOR.message_types_by_name['CameraIntrinsics']
_VECTORBUFFER = DESCRIPTOR.message_types_by_name['VectorBuffer']
_VECTORBUFFER_COMPONENTTYPE = _VECTORBUFFER.enum_types_by_name['ComponentType']
_VECTORBUFFER_BYTEORDER = _VECTORBUFFER.enum_types_by_name['ByteOrder']
RoomString = _reflection.GeneratedProtocolMessageType('RoomString', (_message.Message,), {
  'DESCRIPTOR' : _ROOMSTRING,
  '__module__' : 'streem.room.rooms_pb2'
  # @@protoc_insertion_point(class_scope:RoomString)
  })
_sym_db.RegisterMessage(RoomString)

CameraIntrinsics = _reflection.GeneratedProtocolMessageType('CameraIntrinsics', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAINTRINSICS,
  '__module__' : 'streem.room.rooms_pb2'
  # @@protoc_insertion_point(class_scope:CameraIntrinsics)
  })
_sym_db.RegisterMessage(CameraIntrinsics)

VectorBuffer = _reflection.GeneratedProtocolMessageType('VectorBuffer', (_message.Message,), {
  'DESCRIPTOR' : _VECTORBUFFER,
  '__module__' : 'streem.room.rooms_pb2'
  # @@protoc_insertion_point(class_scope:VectorBuffer)
  })
_sym_db.RegisterMessage(VectorBuffer)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026pro.streem.model.protoB\005Rooms\272\002\rStreem_Rooms_'
  _CAMERASUBJECT._serialized_start=739
  _CAMERASUBJECT._serialized_end=834
  _STREAMINGMESSAGEPROVIDER._serialized_start=837
  _STREAMINGMESSAGEPROVIDER._serialized_end=997
  _ROOMSTRING._serialized_start=27
  _ROOMSTRING._serialized_end=68
  _CAMERAINTRINSICS._serialized_start=71
  _CAMERAINTRINSICS._serialized_end=216
  _VECTORBUFFER._serialized_start=219
  _VECTORBUFFER._serialized_end=737
  _VECTORBUFFER_COMPONENTTYPE._serialized_start=467
  _VECTORBUFFER_COMPONENTTYPE._serialized_end=643
  _VECTORBUFFER_BYTEORDER._serialized_start=645
  _VECTORBUFFER_BYTEORDER._serialized_end=737
# @@protoc_insertion_point(module_scope)
