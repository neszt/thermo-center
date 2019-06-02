# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from configurator import api_pb2 as configurator_dot_api__pb2


class ConfiguratorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetRadioCfg = channel.unary_unary(
        '/configurator.Configurator/GetRadioCfg',
        request_serializer=configurator_dot_api__pb2.RadioCfgRequest.SerializeToString,
        response_deserializer=configurator_dot_api__pb2.RadioCfgResponse.FromString,
        )


class ConfiguratorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetRadioCfg(self, request, context):
    """Return radio configuration for receiver
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConfiguratorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetRadioCfg': grpc.unary_unary_rpc_method_handler(
          servicer.GetRadioCfg,
          request_deserializer=configurator_dot_api__pb2.RadioCfgRequest.FromString,
          response_serializer=configurator_dot_api__pb2.RadioCfgResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'configurator.Configurator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
