// Generated by gencpp from file ex/ex_srvResponse.msg
// DO NOT EDIT!


#ifndef EX_MESSAGE_EX_SRVRESPONSE_H
#define EX_MESSAGE_EX_SRVRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ex
{
template <class ContainerAllocator>
struct ex_srvResponse_
{
  typedef ex_srvResponse_<ContainerAllocator> Type;

  ex_srvResponse_()
    : sum(0)  {
    }
  ex_srvResponse_(const ContainerAllocator& _alloc)
    : sum(0)  {
    }



   typedef int32_t _sum_type;
  _sum_type sum;




  typedef boost::shared_ptr< ::ex::ex_srvResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ex::ex_srvResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ex_srvResponse_

typedef ::ex::ex_srvResponse_<std::allocator<void> > ex_srvResponse;

typedef boost::shared_ptr< ::ex::ex_srvResponse > ex_srvResponsePtr;
typedef boost::shared_ptr< ::ex::ex_srvResponse const> ex_srvResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ex::ex_srvResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ex::ex_srvResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ex

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'ex': ['/home/saruman/workspaces/ros_workspace/case_robotics/nasa/catkin_wkspace/src/ex/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ex::ex_srvResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ex::ex_srvResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ex::ex_srvResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ex::ex_srvResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ex::ex_srvResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ex::ex_srvResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ex::ex_srvResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0ba699c25c9418c0366f3595c0c8e8ec";
  }

  static const char* value(const ::ex::ex_srvResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0ba699c25c9418c0ULL;
  static const uint64_t static_value2 = 0x366f3595c0c8e8ecULL;
};

template<class ContainerAllocator>
struct DataType< ::ex::ex_srvResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ex/ex_srvResponse";
  }

  static const char* value(const ::ex::ex_srvResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ex::ex_srvResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
int32 sum\n\
\n\
";
  }

  static const char* value(const ::ex::ex_srvResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ex::ex_srvResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sum);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ex_srvResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ex::ex_srvResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ex::ex_srvResponse_<ContainerAllocator>& v)
  {
    s << indent << "sum: ";
    Printer<int32_t>::stream(s, indent + "  ", v.sum);
  }
};

} // namespace message_operations
} // namespace ros

#endif // EX_MESSAGE_EX_SRVRESPONSE_H