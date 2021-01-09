#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from interfaces.msg import HardwareStatus

class MyNode(Node):
    def __init__(self):
        super().__init__('py_test')
        self.get_logger().info('Initializing py_test')
        self.i = 0
        self.create_timer(0.1, self.publish_msg)
        self.publisher = self.create_publisher(HardwareStatus, 'power_topic', 10)

    def publish_msg(self):
        self.get_logger().warning(f'Peligro {self.i}')

        msg = HardwareStatus()
        msg.wind_speed = 30
        msg.is_working = True
        msg.debug = 'debugeado'
        self.publisher.publish(msg)

        self.i+=1

def main(args=None):
    try:
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
