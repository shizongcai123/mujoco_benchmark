
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from robotic_assets.robot_base import BaseRobot
import mujoco
from mujoco import viewer
import logging

logging.basicConfig(level=logging.DEBUG)  # 确保 INFO 及以上级别会被打印

if __name__ == "__main__":
    robot = BaseRobot(
        name = 'szc_test_robot',
        scene='F:/mujoco_learning/szc_mujoco/mujoco_benchmark/robopal_part/assets/scenes/grasping.xml', # grasping have some bug need to be fixed
        # mount='F:/mujoco_learning/szc_mujoco/mujoco_benchmark/robotic_assets/mounts/top_point/top_point.xml',
        mount=None,
        robot='F:/mujoco_learning/szc_mujoco/mujoco_benchmark/robopal_part/assets/szc_panda.xml',
    )
    with viewer.launch_passive(robot.robot_model, robot.robot_data) as viewer:

        viewer.sync()

        while viewer.is_running():

            # Step the physics.
            mujoco.mj_step(robot.robot_model, robot.robot_data)

            viewer.sync()
    