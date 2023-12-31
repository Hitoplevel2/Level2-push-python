# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import entity_pb2 as entity__pb2
import proxy_pb2 as proxy__pb2


class ProxyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSubscription = channel.unary_unary(
            '/sa.rpc.cli.proxy.Proxy/GetSubscription',
            request_serializer=entity__pb2.Void.SerializeToString,
            response_deserializer=proxy__pb2.SubscriptionRsp.FromString,
        )
        self.AddSubscription = channel.unary_unary(
            '/sa.rpc.cli.proxy.Proxy/AddSubscription',
            request_serializer=entity__pb2.String.SerializeToString,
            response_deserializer=proxy__pb2.Rsp.FromString,
        )
        self.DelSubscription = channel.unary_unary(
            '/sa.rpc.cli.proxy.Proxy/DelSubscription',
            request_serializer=entity__pb2.String.SerializeToString,
            response_deserializer=proxy__pb2.Rsp.FromString,
        )
        self.NewTickRecordStream = channel.unary_stream(
            '/sa.rpc.cli.proxy.Proxy/NewTickRecordStream',
            request_serializer=entity__pb2.Void.SerializeToString,
            response_deserializer=entity__pb2.TickRecord.FromString,
        )
        self.NewOrderRecordStream = channel.unary_stream(
            '/sa.rpc.cli.proxy.Proxy/NewOrderRecordStream',
            request_serializer=entity__pb2.Void.SerializeToString,
            response_deserializer=entity__pb2.OrderRecord.FromString,
        )
        self.NewOrderQueueRecordStream = channel.unary_stream(
            '/sa.rpc.cli.proxy.Proxy/NewOrderQueueRecordStream',
            request_serializer=entity__pb2.Void.SerializeToString,
            response_deserializer=entity__pb2.OrderQueueRecord.FromString,
        )
        self.NewStockQuoteRecordStream = channel.unary_stream(
            '/sa.rpc.cli.proxy.Proxy/NewStockQuoteRecordStream',
            request_serializer=entity__pb2.Void.SerializeToString,
            response_deserializer=entity__pb2.StockQuoteRecord.FromString,
        )


class ProxyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSubscription(self, request, context):
        """查询订阅
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSubscription(self, request, context):
        """新增订阅
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelSubscription(self, request, context):
        """取消订阅
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewTickRecordStream(self, request, context):
        """推送逐笔成交行情数据
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewOrderRecordStream(self, request, context):
        """推送逐笔委托行情数据
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewOrderQueueRecordStream(self, request, context):
        """推送委托队列行情数据
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewStockQuoteRecordStream(self, request, context):
        """推送股票十档行情行情数据
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProxyServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetSubscription': grpc.unary_unary_rpc_method_handler(
            servicer.GetSubscription,
            request_deserializer=entity__pb2.Void.FromString,
            response_serializer=proxy__pb2.SubscriptionRsp.SerializeToString,
        ),
        'AddSubscription': grpc.unary_unary_rpc_method_handler(
            servicer.AddSubscription,
            request_deserializer=entity__pb2.String.FromString,
            response_serializer=proxy__pb2.Rsp.SerializeToString,
        ),
        'DelSubscription': grpc.unary_unary_rpc_method_handler(
            servicer.DelSubscription,
            request_deserializer=entity__pb2.String.FromString,
            response_serializer=proxy__pb2.Rsp.SerializeToString,
        ),
        'NewTickRecordStream': grpc.unary_stream_rpc_method_handler(
            servicer.NewTickRecordStream,
            request_deserializer=entity__pb2.Void.FromString,
            response_serializer=entity__pb2.TickRecord.SerializeToString,
        ),
        'NewOrderRecordStream': grpc.unary_stream_rpc_method_handler(
            servicer.NewOrderRecordStream,
            request_deserializer=entity__pb2.Void.FromString,
            response_serializer=entity__pb2.OrderRecord.SerializeToString,
        ),
        'NewOrderQueueRecordStream': grpc.unary_stream_rpc_method_handler(
            servicer.NewOrderQueueRecordStream,
            request_deserializer=entity__pb2.Void.FromString,
            response_serializer=entity__pb2.OrderQueueRecord.SerializeToString,
        ),
        'NewStockQuoteRecordStream': grpc.unary_stream_rpc_method_handler(
            servicer.NewStockQuoteRecordStream,
            request_deserializer=entity__pb2.Void.FromString,
            response_serializer=entity__pb2.StockQuoteRecord.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'sa.rpc.cli.proxy.Proxy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Proxy(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSubscription(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sa.rpc.cli.proxy.Proxy/GetSubscription',
                                             entity__pb2.Void.SerializeToString,
                                             proxy__pb2.SubscriptionRsp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSubscription(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sa.rpc.cli.proxy.Proxy/AddSubscription',
                                             entity__pb2.String.SerializeToString,
                                             proxy__pb2.Rsp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelSubscription(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sa.rpc.cli.proxy.Proxy/DelSubscription',
                                             entity__pb2.String.SerializeToString,
                                             proxy__pb2.Rsp.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewTickRecordStream(request,
                            target,
                            options=(),
                            channel_credentials=None,
                            call_credentials=None,
                            insecure=False,
                            compression=None,
                            wait_for_ready=None,
                            timeout=None,
                            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sa.rpc.cli.proxy.Proxy/NewTickRecordStream',
                                              entity__pb2.Void.SerializeToString,
                                              entity__pb2.TickRecord.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)

    @staticmethod
    def NewOrderRecordStream(request,
                             target,
                             options=(),
                             channel_credentials=None,
                             call_credentials=None,
                             insecure=False,
                             compression=None,
                             wait_for_ready=None,
                             timeout=None,
                             metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sa.rpc.cli.proxy.Proxy/NewOrderRecordStream',
                                              entity__pb2.Void.SerializeToString,
                                              entity__pb2.OrderRecord.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)

    @staticmethod
    def NewOrderQueueRecordStream(request,
                                  target,
                                  options=(),
                                  channel_credentials=None,
                                  call_credentials=None,
                                  insecure=False,
                                  compression=None,
                                  wait_for_ready=None,
                                  timeout=None,
                                  metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sa.rpc.cli.proxy.Proxy/NewOrderQueueRecordStream',
                                              entity__pb2.Void.SerializeToString,
                                              entity__pb2.OrderQueueRecord.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)

    @staticmethod
    def NewStockQuoteRecordStream(request,
                                  target,
                                  options=(),
                                  channel_credentials=None,
                                  call_credentials=None,
                                  insecure=False,
                                  compression=None,
                                  wait_for_ready=None,
                                  timeout=None,
                                  metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sa.rpc.cli.proxy.Proxy/NewStockQuoteRecordStream',
                                              entity__pb2.Void.SerializeToString,
                                              entity__pb2.StockQuoteRecord.FromString,
                                              options, channel_credentials,
                                              insecure, call_credentials, compression, wait_for_ready, timeout,
                                              metadata)
