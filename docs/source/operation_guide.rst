快速操作流程
============

前置准备
--------

1. Ubuntu + ROS 环境正常（建议先执行 ``roscore`` 验证）。
2. 主控与底层板串口连接正常，供电稳定。
3. SBUS 接收机已绑定，通道方向已校准。
4. 机器人离地或有支撑，便于首次联调。

启动步骤（建议顺序）
--------------------

1. 启动 ROS Master：

.. code-block:: bash

   roscore

2. 启动串口代理节点（根据你的包名替换）：

.. code-block:: bash

   roslaunch <your_pkg> serial_proxy.launch

3. 启动控制节点：

.. code-block:: bash

   roslaunch <your_pkg> controller.launch

4. 可选：启动导航栈（``move_base``）：

.. code-block:: bash

   roslaunch <your_nav_pkg> move_base.launch

5. 终端检查关键话题：

.. code-block:: bash

   rostopic echo /power_voltage
   rostopic echo /state/velocity
   rostopic echo /force_disable

联调检查清单
------------

1. ``/imu`` 与 ``/joint_state`` 持续更新，无长时间卡死。
2. 切换 ``SA`` 后，扭矩输出符合急停逻辑。
3. 切换 ``SD`` 后，底层 ``/force_disable`` 收发一致。
4. ``SB`` 快慢档切换后，速度目标幅值变化符合预期。
5. ``move_base`` 下发 ``/cmd_vel`` 时，机器人方向与速度符号正确。

导航接入建议（Move Base）
-------------------------

1. 先做原地旋转和短距离直行，验证 ``/cmd_vel`` 映射。
2. 再接局部代价地图，最后启用全局地图与路径规划。
3. 限制最大线速度、角速度，避免导航首轮过激动作。
4. 在急停逻辑稳定前，不建议开启跳跃动作。

安全建议
--------

1. 首次上电调试时保持手持遥控，优先验证急停通道。
2. 开环测试时，轮腿应离地或加机械限位。
3. 记录每次参数变更（阈值、增益、模式切换策略）并版本化。

