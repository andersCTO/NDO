from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():

    pkg_name = "ndo_nav"
    pkg_share = FindPackageShare(package=pkg_name).find(pkg_name)
    ekf_config = os.path.join(pkg_share, "config", "ekf_localization.yaml")

    ekf_node = Node(
        name="ekf_node",
        package="robot_localization",
        executable="ekf_node",
        output="screen",
        parameters=[ekf_config]
    )

    return LaunchDescription(
        [
            ekf_node
        ]
    )
