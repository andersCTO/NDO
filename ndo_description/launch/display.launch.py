from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import UnlessCondition, IfCondition

import os


def generate_launch_description():
    pkg_name = "ndo_description"
    pkg_share = FindPackageShare(package=pkg_name).find(pkg_name)
    rsp_launch_file = os.path.join(pkg_share, "launch", "rsp.launch.py")
    default_model_path = os.path.join(pkg_share, "urdf", "ndo.urdf.xacro")
    default_rviz_config_path = os.path.join(pkg_share, "rviz", "urdf_config.rviz")

    use_sim_time = LaunchConfiguration("use_sim_time")

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rsp_launch_file),
        launch_arguments={
            "use_sim_time": use_sim_time,
            "model": LaunchConfiguration("model"),
        }.items(),
    )
    jsp = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        condition=UnlessCondition(LaunchConfiguration("gui")),
    )
    jsp_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        condition=IfCondition(LaunchConfiguration("gui")),
    )
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", LaunchConfiguration("rvizconfig")],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="gui",
                default_value="True",
                description="Flag to enable joint_state_publisher_gui",
            ),
            DeclareLaunchArgument(
                name="model",
                default_value=default_model_path,
                description="Absolute path to robot urdf file",
            ),
            DeclareLaunchArgument(
                name="rvizconfig",
                default_value=default_rviz_config_path,
                description="Absolute path to rviz config file",
            ),
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use sim time if true",
            ),
            rsp,
            jsp,
            jsp_gui,
            rviz,
        ]
    )
