from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='super_pkg',
            namespace='super_pkg',
            executable='adas',
            name='sim1'
        ),
        Node(
            package='super_pkg',
            namespace='super_pkg',
            executable='speedometer',
            name='sim2'
        ),
        Node(
            package='super_pkg',
            namespace='super_pkg',
            executable='speed_alarm',
            name='decide'
        )
    ])