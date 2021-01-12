#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class ADAS(Node):
    def __init__(self):
        super().__init__('ADAS')
        self.get_logger().info('Initializing ADAS')
        self.create_timer(0.1, self.publish_msg)
        self.publisher = self.create_publisher(Float64, 'speed', 10)

    def publish_msg(self):
        msg = Float64()
        msg.data = 50.0
        self.publisher.publish(msg)

def main(args=None):
    try:
        rclpy.init(args=args)
        node = ADAS()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
