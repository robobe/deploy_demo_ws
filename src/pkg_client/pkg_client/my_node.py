#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from pkg_interface.srv import Demo

TOPIC_NAME = 'my_service'

class MyNode(Node):
    def __init__(self):
        node_name="client"
        super().__init__(node_name)
        self.get_logger().info("Hello client")
        self.client = self.create_client(Demo, TOPIC_NAME)
        self.client.wait_for_service()
        
        self.future = None
        self.call_service() 

    def call_service(self):
        self.req = Demo.Request()
        self.get_logger().info('Call serice')
        self.future = self.client.call_async(self.req)
        self.future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response: Demo.Response = future.result()
            self.get_logger().info('Service call success')
            self.get_logger().info(response.message)
        except Exception as e:
            self.get_logger().info('Service call failed %r' % (e,))
            

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()