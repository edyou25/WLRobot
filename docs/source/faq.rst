常见问题
========

1) ``sphinx-build: command not found``
--------------------------------------

在文档目录安装依赖后再构建：

.. code-block:: bash

   cd docs
   pip install -r requirements.txt
   make html

2) 主题不是 Read the Docs 风格
------------------------------

确认 ``conf.py`` 中包含：

.. code-block:: python

   html_theme = "sphinx_rtd_theme"

并确认已安装 ``sphinx-rtd-theme``。

3) 遥控切换无效
---------------

1. 先看 ``/sbus`` 数据是否变化。
2. 检查阈值（``992`` / ``600`` / ``200``）与遥控器校准区间是否匹配。
3. 确认边沿触发逻辑是否被“上一次值”初始化影响。

4) 导航会冲击或方向反
----------------------

1. 限制 ``/cmd_vel`` 最大速度。
2. 逐轴验证线速度与角速度符号。
3. 排查 IMU 朝向与机体坐标系定义。

