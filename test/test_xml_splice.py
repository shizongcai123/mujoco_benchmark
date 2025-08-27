import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from robopal_part.base import *
from mujoco import viewer
import logging

logging.basicConfig(level=logging.DEBUG)  # 确保 INFO 及以上级别会被打印

if __name__ == "__main__":
    robot = BaseRobot(
        scene='default',
        manipulator='Panda',
        gripper='PandaHand',
        mount='top_point',
        attached_body='0_attachment',
    )
    print("+===================")
    robot.mjcf_generator.save_xml("szc_panda")
    print("==============================")
    with viewer.launch_passive(robot.robot_model, robot.robot_data) as viewer:

        viewer.sync()

        while viewer.is_running():

            # Step the physics.
            mujoco.mj_step(robot.robot_model, robot.robot_data)

            viewer.sync()
    