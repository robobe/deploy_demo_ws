import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class MyNode(Node):
    def __init__(self):
        node_name="server"
        super().__init__(node_name)
        self.get_logger().info("Hello Server")
        self.server = self.create_service(Empty, 'my_service', self.callback)

    def callback(self, request, response):
        self.get_logger().info('Service called')
        return response   

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()