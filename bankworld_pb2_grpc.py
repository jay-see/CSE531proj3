# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bankworld_pb2 as bankworld__pb2


class CustomerStub(object):
    """The customer service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createStub = channel.unary_unary(
                '/bankworld.Customer/createStub',
                request_serializer=bankworld__pb2.StubEvent.SerializeToString,
                response_deserializer=bankworld__pb2.StubDone.FromString,
                )
        self.executeEvents = channel.unary_unary(
                '/bankworld.Customer/executeEvents',
                request_serializer=bankworld__pb2.StubEvent.SerializeToString,
                response_deserializer=bankworld__pb2.StubDone.FromString,
                )


class CustomerServicer(object):
    """The customer service definition.
    """

    def createStub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def executeEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createStub': grpc.unary_unary_rpc_method_handler(
                    servicer.createStub,
                    request_deserializer=bankworld__pb2.StubEvent.FromString,
                    response_serializer=bankworld__pb2.StubDone.SerializeToString,
            ),
            'executeEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.executeEvents,
                    request_deserializer=bankworld__pb2.StubEvent.FromString,
                    response_serializer=bankworld__pb2.StubDone.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bankworld.Customer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Customer(object):
    """The customer service definition.
    """

    @staticmethod
    def createStub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bankworld.Customer/createStub',
            bankworld__pb2.StubEvent.SerializeToString,
            bankworld__pb2.StubDone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def executeEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bankworld.Customer/executeEvents',
            bankworld__pb2.StubEvent.SerializeToString,
            bankworld__pb2.StubDone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BranchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createStub = channel.unary_unary(
                '/bankworld.Branch/createStub',
                request_serializer=bankworld__pb2.StubEvent.SerializeToString,
                response_deserializer=bankworld__pb2.StubDone.FromString,
                )
        self.MsgDelivery = channel.unary_unary(
                '/bankworld.Branch/MsgDelivery',
                request_serializer=bankworld__pb2.BranchRequest.SerializeToString,
                response_deserializer=bankworld__pb2.BranchReply.FromString,
                )
        self.Get_Balance = channel.unary_unary(
                '/bankworld.Branch/Get_Balance',
                request_serializer=bankworld__pb2.BalanceRequest.SerializeToString,
                response_deserializer=bankworld__pb2.BalanceReply.FromString,
                )


class BranchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createStub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MsgDelivery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_Balance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BranchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createStub': grpc.unary_unary_rpc_method_handler(
                    servicer.createStub,
                    request_deserializer=bankworld__pb2.StubEvent.FromString,
                    response_serializer=bankworld__pb2.StubDone.SerializeToString,
            ),
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=bankworld__pb2.BranchRequest.FromString,
                    response_serializer=bankworld__pb2.BranchReply.SerializeToString,
            ),
            'Get_Balance': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_Balance,
                    request_deserializer=bankworld__pb2.BalanceRequest.FromString,
                    response_serializer=bankworld__pb2.BalanceReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bankworld.Branch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Branch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createStub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bankworld.Branch/createStub',
            bankworld__pb2.StubEvent.SerializeToString,
            bankworld__pb2.StubDone.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bankworld.Branch/MsgDelivery',
            bankworld__pb2.BranchRequest.SerializeToString,
            bankworld__pb2.BranchReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_Balance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bankworld.Branch/Get_Balance',
            bankworld__pb2.BalanceRequest.SerializeToString,
            bankworld__pb2.BalanceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
