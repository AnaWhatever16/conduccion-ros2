#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64

class Speedometer(Node):
    def __init__(self):
        super().__init__('speedometer')
        self.get_logger().info('Initializing Speedometer')
        self.subscriber = self.create_subscription(Float64, 'speed', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Speed: {msg.data}')

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Speedometer()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
