// Code generated by protoc-gen-go. DO NOT EDIT.
// source: aggregator/api.proto

package aggregator

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type SensorPacket struct {
	Id                   uint32   `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Seq                  uint32   `protobuf:"varint,2,opt,name=seq,proto3" json:"seq,omitempty"`
	Rssi                 float32  `protobuf:"fixed32,3,opt,name=rssi,proto3" json:"rssi,omitempty"`
	Lqi                  uint32   `protobuf:"varint,4,opt,name=lqi,proto3" json:"lqi,omitempty"`
	Raw                  []byte   `protobuf:"bytes,5,opt,name=raw,proto3" json:"raw,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *SensorPacket) Reset()         { *m = SensorPacket{} }
func (m *SensorPacket) String() string { return proto.CompactTextString(m) }
func (*SensorPacket) ProtoMessage()    {}
func (*SensorPacket) Descriptor() ([]byte, []int) {
	return fileDescriptor_c61064fd1e012251, []int{0}
}

func (m *SensorPacket) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SensorPacket.Unmarshal(m, b)
}
func (m *SensorPacket) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SensorPacket.Marshal(b, m, deterministic)
}
func (m *SensorPacket) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SensorPacket.Merge(m, src)
}
func (m *SensorPacket) XXX_Size() int {
	return xxx_messageInfo_SensorPacket.Size(m)
}
func (m *SensorPacket) XXX_DiscardUnknown() {
	xxx_messageInfo_SensorPacket.DiscardUnknown(m)
}

var xxx_messageInfo_SensorPacket proto.InternalMessageInfo

func (m *SensorPacket) GetId() uint32 {
	if m != nil {
		return m.Id
	}
	return 0
}

func (m *SensorPacket) GetSeq() uint32 {
	if m != nil {
		return m.Seq
	}
	return 0
}

func (m *SensorPacket) GetRssi() float32 {
	if m != nil {
		return m.Rssi
	}
	return 0
}

func (m *SensorPacket) GetLqi() uint32 {
	if m != nil {
		return m.Lqi
	}
	return 0
}

func (m *SensorPacket) GetRaw() []byte {
	if m != nil {
		return m.Raw
	}
	return nil
}

type FeedResponse struct {
	Processed            bool     `protobuf:"varint,1,opt,name=processed,proto3" json:"processed,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *FeedResponse) Reset()         { *m = FeedResponse{} }
func (m *FeedResponse) String() string { return proto.CompactTextString(m) }
func (*FeedResponse) ProtoMessage()    {}
func (*FeedResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_c61064fd1e012251, []int{1}
}

func (m *FeedResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FeedResponse.Unmarshal(m, b)
}
func (m *FeedResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FeedResponse.Marshal(b, m, deterministic)
}
func (m *FeedResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FeedResponse.Merge(m, src)
}
func (m *FeedResponse) XXX_Size() int {
	return xxx_messageInfo_FeedResponse.Size(m)
}
func (m *FeedResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_FeedResponse.DiscardUnknown(m)
}

var xxx_messageInfo_FeedResponse proto.InternalMessageInfo

func (m *FeedResponse) GetProcessed() bool {
	if m != nil {
		return m.Processed
	}
	return false
}

func init() {
	proto.RegisterType((*SensorPacket)(nil), "aggregator.SensorPacket")
	proto.RegisterType((*FeedResponse)(nil), "aggregator.FeedResponse")
}

func init() { proto.RegisterFile("aggregator/api.proto", fileDescriptor_c61064fd1e012251) }

var fileDescriptor_c61064fd1e012251 = []byte{
	// 242 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x54, 0x90, 0x41, 0x4f, 0x83, 0x40,
	0x10, 0x85, 0x85, 0x56, 0xa3, 0x13, 0x34, 0xcd, 0xc6, 0xc3, 0xc6, 0x78, 0x20, 0x9c, 0x38, 0x28,
	0x44, 0xfb, 0x0b, 0xf4, 0x60, 0x3c, 0x9a, 0x35, 0xf1, 0xe0, 0x6d, 0x0b, 0x13, 0x58, 0x69, 0x19,
	0x98, 0x59, 0x63, 0xec, 0xaf, 0x37, 0xd0, 0x44, 0xca, 0xed, 0xe5, 0x7b, 0x6f, 0xf7, 0xbd, 0x5d,
	0xb8, 0xb6, 0x55, 0xc5, 0x58, 0x59, 0x4f, 0x9c, 0xdb, 0xce, 0x65, 0x1d, 0x93, 0x27, 0x05, 0x13,
	0x4d, 0x6a, 0x88, 0xde, 0xb1, 0x15, 0xe2, 0x37, 0x5b, 0x34, 0xe8, 0xd5, 0x15, 0x84, 0xae, 0xd4,
	0x41, 0x1c, 0xa4, 0x97, 0x26, 0x74, 0xa5, 0x5a, 0xc1, 0x42, 0xb0, 0xd7, 0xe1, 0x08, 0x06, 0xa9,
	0x14, 0x2c, 0x59, 0xc4, 0xe9, 0x45, 0x1c, 0xa4, 0xa1, 0x19, 0xf5, 0x90, 0xda, 0xf6, 0x4e, 0x2f,
	0x0f, 0xa9, 0x6d, 0x3f, 0x12, 0xb6, 0x3f, 0xfa, 0x34, 0x0e, 0xd2, 0xc8, 0x0c, 0x32, 0xb9, 0x83,
	0xe8, 0x05, 0xb1, 0x34, 0x28, 0x1d, 0xb5, 0x82, 0xea, 0x16, 0x2e, 0x3a, 0xa6, 0x02, 0x45, 0xf0,
	0x50, 0x78, 0x6e, 0x26, 0xf0, 0xf8, 0x01, 0xf0, 0xf4, 0xbf, 0x52, 0xbd, 0xc2, 0x6a, 0x38, 0x3b,
	0x5b, 0xaa, 0xb3, 0xe9, 0x19, 0xd9, 0xb1, 0x73, 0x33, 0x73, 0x8e, 0x3b, 0x93, 0x93, 0xe7, 0xf5,
	0xe7, 0x43, 0xe5, 0x7c, 0xfd, 0xbd, 0xc9, 0x0a, 0xda, 0xe5, 0xdc, 0xd0, 0x17, 0x96, 0x7b, 0xd7,
	0xca, 0xbe, 0xf9, 0xcd, 0x7d, 0x8d, 0xbc, 0xa3, 0xfb, 0x02, 0x5b, 0x8f, 0x9c, 0x4f, 0x77, 0x6c,
	0xce, 0xc6, 0x7f, 0x5b, 0xff, 0x05, 0x00, 0x00, 0xff, 0xff, 0x2a, 0x59, 0x48, 0xb5, 0x4f, 0x01,
	0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// AggregatorClient is the client API for Aggregator service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type AggregatorClient interface {
	// Feed packet to processor
	FeedSensorPacket(ctx context.Context, in *SensorPacket, opts ...grpc.CallOption) (*FeedResponse, error)
}

type aggregatorClient struct {
	cc *grpc.ClientConn
}

func NewAggregatorClient(cc *grpc.ClientConn) AggregatorClient {
	return &aggregatorClient{cc}
}

func (c *aggregatorClient) FeedSensorPacket(ctx context.Context, in *SensorPacket, opts ...grpc.CallOption) (*FeedResponse, error) {
	out := new(FeedResponse)
	err := c.cc.Invoke(ctx, "/aggregator.Aggregator/FeedSensorPacket", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// AggregatorServer is the server API for Aggregator service.
type AggregatorServer interface {
	// Feed packet to processor
	FeedSensorPacket(context.Context, *SensorPacket) (*FeedResponse, error)
}

// UnimplementedAggregatorServer can be embedded to have forward compatible implementations.
type UnimplementedAggregatorServer struct {
}

func (*UnimplementedAggregatorServer) FeedSensorPacket(ctx context.Context, req *SensorPacket) (*FeedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FeedSensorPacket not implemented")
}

func RegisterAggregatorServer(s *grpc.Server, srv AggregatorServer) {
	s.RegisterService(&_Aggregator_serviceDesc, srv)
}

func _Aggregator_FeedSensorPacket_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SensorPacket)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(AggregatorServer).FeedSensorPacket(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/aggregator.Aggregator/FeedSensorPacket",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(AggregatorServer).FeedSensorPacket(ctx, req.(*SensorPacket))
	}
	return interceptor(ctx, in, info, handler)
}

var _Aggregator_serviceDesc = grpc.ServiceDesc{
	ServiceName: "aggregator.Aggregator",
	HandlerType: (*AggregatorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "FeedSensorPacket",
			Handler:    _Aggregator_FeedSensorPacket_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "aggregator/api.proto",
}