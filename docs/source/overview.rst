系统概览
========

定位
----

WLRobot 是一个基于 ROS 的轮足机器人实验系统，核心包含：

1. 机载控制（``controller``）
2. 底层串口桥接（``serial_proxy``）
3. 传感与遥控输入（IMU、关节编码器、SBUS）
4. 可选导航栈（``move_base``）
5. 监控与可视化客户端（``wl_client``）

核心节点关系
------------

``controller`` 节点（高层控制）：

.. code-block:: text

   Publications:
    * /debug_plot [std_msgs/Float32MultiArray]
    * /force_disable [std_msgs/Bool]
    * /led [std_msgs/UInt8MultiArray]
    * /send_heartbeat [std_msgs/Empty]
    * /state/body_height [std_msgs/Float64]
    * /state/var [std_msgs/Float32MultiArray]
    * /state/velocity [geometry_msgs/Twist]
    * /torque_command [std_msgs/Float32MultiArray]

   Subscriptions:
    * /cmd_vel
    * /current_slope
    * /imu [sensor_msgs/Imu]
    * /joint_state [sensor_msgs/JointState]
    * /joy [sensor_msgs/Joy]
    * /sbus [std_msgs/Float32MultiArray]
    * /trigger_jump

``serial_proxy`` 节点（底层通信）：

.. code-block:: text

   Publications:
    * /imu [sensor_msgs/Imu]
    * /joint_state [sensor_msgs/JointState]
    * /latency_test_recv [std_msgs/Empty]
    * /power_voltage [std_msgs/Float32]
    * /sbus [std_msgs/Float32MultiArray]

   Subscriptions:
    * /force_disable [std_msgs/Bool]
    * /latency_test_send
    * /led [std_msgs/UInt8MultiArray]
    * /reset_driver
    * /send_heartbeat [std_msgs/Empty]
    * /torque_command [std_msgs/Float32MultiArray]

运行模式（建议）
----------------

1. ``上电自检``：确认 IMU、关节、SBUS 数据可读。
2. ``站立控制``：仅保留必要闭环，避免一开始进入高速状态。
3. ``速度跟踪``：通过 ``/cmd_vel`` 或 SBUS 进行小速度闭环测试。
4. ``导航模式``：接入 ``move_base``，逐步启用地图与路径规划。
