#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class SpeedAlarm(Node):
    def __init__(self):
        super().__init__('SpeedAlarm')
        self.get_logger().info('Initializing SpeedAlarm')
        self.publisher = self.create_publisher(Float64, 'camera', 10)
        self.subscriber = self.create_subscription(Float64, 'camera', self.queryAlarm, 10)
        self.subscriber = self.create_subscription(Float64, 'speed', self.speedCallback, 5)
        self.realSpeed = 50.0
        msg = Float64()
        msg.data = self.realSpeed
        self.publisher.publish(msg)

    def queryAlarm(self, msg):
        if(self.realSpeed > msg.data):
            self.get_logger().warning(f'ALARM!!! Overspeeding by {self.realSpeed - msg.data} km/h')
    
    def speedCallback(self, msg):
        self.realSpeed = msg.data

def main(args=None):
    try:
        rclpy.init(args=args)
        node = SpeedAlarm()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()