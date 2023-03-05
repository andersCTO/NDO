from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os


def generate_launch_description():
    pkg_name = "ndo_description"
    pkg_share = FindPackageShare(package=pkg_name).find(pkg_name)
    default_model_path = os.path.join(pkg_share, "urdf", "ndo.urdf.xacro")

    use_sim_time = LaunchConfiguration("use_sim_time")

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "use_sim_time": use_sim_time,
                "robot_description": Command(
                    [
                        "xacro ",
                        LaunchConfiguration("model"),
                        " use_sim_ctrl:=",
                        use_sim_time,
                    ]
                ),
            }
        ],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="model",
                default_value=default_model_path,
                description="Absolute path to robot urdf file",
            ),
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use sim time if true",
            ),
            robot_state_publisher_node,
        ]
    )
