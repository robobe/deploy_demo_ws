from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pkg_server',
            executable='my_node.py',
            name='server_node',
            output='screen'
        ),
        Node(
            package='pkg_client',
            executable='my_node.py',
            name='client_node',
            output='screen'
        )
    ])