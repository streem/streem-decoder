# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streem/room/ar/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streem.room import rooms_pb2 as streem_dot_room_dot_rooms__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreem/room/ar/common.proto\x12\x0estreem.room.ar\x1a\x17streem/room/rooms.proto\"\x8d\x02\n\x04Mesh\x12\x1f\n\x08vertices\x18\x01 \x01(\x0b\x32\r.VectorBuffer\x12\x1c\n\x05\x66\x61\x63\x65s\x18\x02 \x01(\x0b\x32\r.VectorBuffer\x12\x1e\n\x07normals\x18\x03 \x01(\x0b\x32\r.VectorBuffer\x12+\n\x14\x66\x61\x63\x65_classifications\x18\x04 \x01(\x0b\x32\r.VectorBuffer\x12/\n\x08platform\x18\x05 \x01(\x0e\x32\x1d.streem.room.ar.Mesh.Platform\"H\n\x08Platform\x12\x14\n\x10PLATFORM_INVALID\x10\x00\x12\x10\n\x0cPLATFORM_IOS\x10\x01\x12\x14\n\x10PLATFORM_ANDROID\x10\x02\x42I\n&pro.streem.commons.model.proto.room.arB\x0b\x43ommonProtoP\x01\xba\x02\x0fStreem_Room_Ar_b\x06proto3')



_MESH = DESCRIPTOR.message_types_by_name['Mesh']
_MESH_PLATFORM = _MESH.enum_types_by_name['Platform']
Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), {
  'DESCRIPTOR' : _MESH,
  '__module__' : 'streem.room.ar.common_pb2'
  # @@protoc_insertion_point(class_scope:streem.room.ar.Mesh)
  })
_sym_db.RegisterMessage(Mesh)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&pro.streem.commons.model.proto.room.arB\013CommonProtoP\001\272\002\017Streem_Room_Ar_'
  _MESH._serialized_start=73
  _MESH._serialized_end=342
  _MESH_PLATFORM._serialized_start=270
  _MESH_PLATFORM._serialized_end=342
# @@protoc_insertion_point(module_scope)
