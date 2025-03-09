#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from pkg_interface.srv import Demo

TOPIC_NAME = 'my_service'

class MyNode(Node):
    def __init__(self):
        node_name="client"
        super().__init__(node_name)
        self.get_logger().info("Hello server")
        self.server = self.create_service(Demo, TOPIC_NAME, self.callback)

    def callback(self, request: Demo.Request, response: Demo.Response):
        self.get_logger().info('Service called')
        response.message = "Hello from server"
        return response

            

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()