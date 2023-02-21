from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    diff_ctrl_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["diff_ctrl"],
    )
    
    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_broad"],
    )

    return LaunchDescription([diff_ctrl_spawner, joint_broad_spawner])
