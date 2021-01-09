#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmatphoneNode(Node):
    def __init__(self):
        super().__init__('smatphone')
        self.get_logger().info('Initializing py_test')
        self.subscriber = self.create_subscription(String, 'power_topic', self.callback, 10)

    def callback(self, msg):
        self.get_logger().warning(msg.data)

def main(args=None):
    try:
        rclpy.init(args=args)
        node = SmatphoneNode()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
