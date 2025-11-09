from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start VESC driver
        Node(
            package='vesc_driver',
            executable='vesc_driver_node',
            name='vesc_driver',
            output='screen',
            parameters=['/home/chrono/vesc_ws/src/vesc/config/vesc_params.yaml']
        ),

        # Start slider GUI
        Node(
            package='vesc_slider',
            executable='vesc_slider',
            name='vesc_slider',
            output='screen'
        ),
    ])
