from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit


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

    return LaunchDescription(
        [
            joint_broad_spawner,
            RegisterEventHandler(
                event_handler=OnProcessExit(
                    target_action=joint_broad_spawner,
                    on_exit=[diff_ctrl_spawner],
                )
            ),
        ]
    )
