# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nchat.proto\",\n\x05Inbox\x12#\n\x0c\x63onversation\x18\x01 \x03(\x0b\x32\r.Conversation\"^\n\x0c\x43onversation\x12\n\n\x02id\x18\x04 \x01(\x03\x12\x13\n\x0bparticipant\x18\x01 \x03(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x19\n\x07message\x18\x03 \x03(\x0b\x32\x08.Message\"\x90\x02\n\x07Message\x12\x13\n\x0bsender_name\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12*\n\x0c\x63ontent_type\x18\x04 \x01(\x0e\x32\x14.Message.ContentType\x12\x11\n\tmedia_uri\x18\x05 \x03(\t\"\x8c\x01\n\x0b\x43ontentType\x12\x0e\n\nCT_UNKNOWN\x10\x00\x12\r\n\tCT_IGNORE\x10\x01\x12\x0b\n\x07\x43T_TEXT\x10\x02\x12\x0c\n\x08\x43T_PHOTO\x10\x03\x12\x0e\n\nCT_STICKER\x10\x04\x12\n\n\x06\x43T_GIF\x10\x05\x12\x0b\n\x07\x43T_FILE\x10\x06\x12\x0c\n\x08\x43T_VIDEO\x10\x07\x12\x0c\n\x08\x43T_AUDIO\x10\x08\x62\x06proto3')
)



_MESSAGE_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='Message.ContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CT_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_IGNORE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_TEXT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_PHOTO', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_STICKER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_GIF', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_FILE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_VIDEO', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CT_AUDIO', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=289,
  serialized_end=429,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_CONTENTTYPE)


_INBOX = _descriptor.Descriptor(
  name='Inbox',
  full_name='Inbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conversation', full_name='Inbox.conversation', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=58,
)


_CONVERSATION = _descriptor.Descriptor(
  name='Conversation',
  full_name='Conversation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Conversation.id', index=0,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='participant', full_name='Conversation.participant', index=1,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='Conversation.group_name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Conversation.message', index=3,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=154,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='Message.sender_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Message.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='Message.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='Message.content_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media_uri', full_name='Message.media_uri', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_CONTENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=429,
)

_INBOX.fields_by_name['conversation'].message_type = _CONVERSATION
_CONVERSATION.fields_by_name['message'].message_type = _MESSAGE
_MESSAGE.fields_by_name['content_type'].enum_type = _MESSAGE_CONTENTTYPE
_MESSAGE_CONTENTTYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Inbox'] = _INBOX
DESCRIPTOR.message_types_by_name['Conversation'] = _CONVERSATION
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Inbox = _reflection.GeneratedProtocolMessageType('Inbox', (_message.Message,), dict(
  DESCRIPTOR = _INBOX,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:Inbox)
  ))
_sym_db.RegisterMessage(Inbox)

Conversation = _reflection.GeneratedProtocolMessageType('Conversation', (_message.Message,), dict(
  DESCRIPTOR = _CONVERSATION,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:Conversation)
  ))
_sym_db.RegisterMessage(Conversation)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)