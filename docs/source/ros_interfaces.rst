ROS 接口说明
============

传感器消息
----------

``sensor_msgs/JointState`` (ROS 内置):

.. code-block:: text

   std_msgs/Header header
   string[] name
   float64[] position
   float64[] velocity
   float64[] effort

``sensor_msgs/Imu`` (ROS 内置):

.. code-block:: text

   std_msgs/Header header
   geometry_msgs/Quaternion orientation
   float64[9] orientation_covariance
   geometry_msgs/Vector3 angular_velocity
   float64[9] angular_velocity_covariance
   geometry_msgs/Vector3 linear_acceleration
   float64[9] linear_acceleration_covariance

SBUS 遥控映射
-------------

基于当前代码行为（边沿触发 + 阈值）：

1. ``ch4 (SA)``：软急停切换（阈值 ``992``，边沿触发 ``force_stop_mode``）。
2. ``ch7 (SD)``：``/force_disable`` 切换（阈值 ``992``）。
3. ``ch8 (SE)``：站立 / 跳跃 / wink 状态触发（受 stop 与 standing 条件限制）。
4. ``ch6 (SC)``：NNMPC 模式开关（阈值 ``600``，开启时重置参考量）。
5. ``ch5 (SB)``：速度档位（``>=600`` 快速模式，``<600`` 普通模式）。
6. ``ch1``：``x_vel_target``，以 ``992`` 为中心线性映射。
7. ``ch0``：``yaw_vel_target``，以 ``992`` 为中心线性映射，符号为负。
8. ``ch2``：``l0_pid_ref = 0.25 + scaled_input``。
9. ``ch3``：``roll_pid_ref = 0.05 + scaled_input``。
10. ``ch9 (SF)``：跳跃允许与高度映射（``>200`` 可跳跃）。

控制输出逻辑
------------

``control_callback`` 的核心分支可概括为：

.. code-block:: text

   if not force_stop_mode:
       full joint torque output
   elif standing:
       only wheel torque output
   else:
       all torque zero

这表示系统在急停后仍可在站立状态下保留轮扭矩，完全非站立时才清零所有执行器。

调试命令
--------

.. code-block:: bash

   rostopic list
   rostopic echo /joint_state
   rostopic echo /imu
   rostopic echo /sbus
   rostopic hz /torque_command
   rosnode info controller
   rosnode info serial_proxy
