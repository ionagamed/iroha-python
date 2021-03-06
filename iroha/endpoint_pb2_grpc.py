# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import endpoint_pb2 as endpoint__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import qry_responses_pb2 as qry__responses__pb2
from . import queries_pb2 as queries__pb2
from . import transaction_pb2 as transaction__pb2


class CommandService_v1Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Torii = channel.unary_unary(
        '/iroha.protocol.CommandService_v1/Torii',
        request_serializer=transaction__pb2.Transaction.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListTorii = channel.unary_unary(
        '/iroha.protocol.CommandService_v1/ListTorii',
        request_serializer=endpoint__pb2.TxList.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Status = channel.unary_unary(
        '/iroha.protocol.CommandService_v1/Status',
        request_serializer=endpoint__pb2.TxStatusRequest.SerializeToString,
        response_deserializer=endpoint__pb2.ToriiResponse.FromString,
        )
    self.StatusStream = channel.unary_stream(
        '/iroha.protocol.CommandService_v1/StatusStream',
        request_serializer=endpoint__pb2.TxStatusRequest.SerializeToString,
        response_deserializer=endpoint__pb2.ToriiResponse.FromString,
        )


class CommandService_v1Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Torii(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTorii(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StatusStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommandService_v1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Torii': grpc.unary_unary_rpc_method_handler(
          servicer.Torii,
          request_deserializer=transaction__pb2.Transaction.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListTorii': grpc.unary_unary_rpc_method_handler(
          servicer.ListTorii,
          request_deserializer=endpoint__pb2.TxList.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=endpoint__pb2.TxStatusRequest.FromString,
          response_serializer=endpoint__pb2.ToriiResponse.SerializeToString,
      ),
      'StatusStream': grpc.unary_stream_rpc_method_handler(
          servicer.StatusStream,
          request_deserializer=endpoint__pb2.TxStatusRequest.FromString,
          response_serializer=endpoint__pb2.ToriiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'iroha.protocol.CommandService_v1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class QueryService_v1Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/iroha.protocol.QueryService_v1/Find',
        request_serializer=queries__pb2.Query.SerializeToString,
        response_deserializer=qry__responses__pb2.QueryResponse.FromString,
        )
    self.FetchCommits = channel.unary_stream(
        '/iroha.protocol.QueryService_v1/FetchCommits',
        request_serializer=queries__pb2.BlocksQuery.SerializeToString,
        response_deserializer=qry__responses__pb2.BlockQueryResponse.FromString,
        )


class QueryService_v1Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Find(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchCommits(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QueryService_v1Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=queries__pb2.Query.FromString,
          response_serializer=qry__responses__pb2.QueryResponse.SerializeToString,
      ),
      'FetchCommits': grpc.unary_stream_rpc_method_handler(
          servicer.FetchCommits,
          request_deserializer=queries__pb2.BlocksQuery.FromString,
          response_serializer=qry__responses__pb2.BlockQueryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'iroha.protocol.QueryService_v1', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
