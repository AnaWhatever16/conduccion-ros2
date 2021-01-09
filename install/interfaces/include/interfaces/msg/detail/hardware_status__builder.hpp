// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/HardwareStatus.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_

#include "interfaces/msg/detail/hardware_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_HardwareStatus_debug
{
public:
  explicit Init_HardwareStatus_debug(::interfaces::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::HardwareStatus debug(::interfaces::msg::HardwareStatus::_debug_type arg)
  {
    msg_.debug = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_is_working
{
public:
  explicit Init_HardwareStatus_is_working(::interfaces::msg::HardwareStatus & msg)
  : msg_(msg)
  {}
  Init_HardwareStatus_debug is_working(::interfaces::msg::HardwareStatus::_is_working_type arg)
  {
    msg_.is_working = std::move(arg);
    return Init_HardwareStatus_debug(msg_);
  }

private:
  ::interfaces::msg::HardwareStatus msg_;
};

class Init_HardwareStatus_wind_speed
{
public:
  Init_HardwareStatus_wind_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HardwareStatus_is_working wind_speed(::interfaces::msg::HardwareStatus::_wind_speed_type arg)
  {
    msg_.wind_speed = std::move(arg);
    return Init_HardwareStatus_is_working(msg_);
  }

private:
  ::interfaces::msg::HardwareStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::HardwareStatus>()
{
  return interfaces::msg::builder::Init_HardwareStatus_wind_speed();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__HARDWARE_STATUS__BUILDER_HPP_
