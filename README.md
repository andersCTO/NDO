# NDO

## Installation for development
1. Create a ROS2 workspace or use [NDO workspace for VSCode](https://github.com/JPDF/vscode_ndo_ros2_ws).
2. Copy this repo to your workspace. Your workspace should now look like this:
```
workspace
└──src
    └──ndo <-- THIS REPO
       │  README.md
       │  ...
       └──ndo
       └──ndo_description
       └──ndo_nav
       └──ndo_teleop
```
3. Install dependencies `rosdep install --from-paths src --ignore-src -y`
4. Build project `colcon build`


