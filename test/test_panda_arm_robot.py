import mujoco
from robotic_assets.panda.panda_arm_robot import PandaPickAndPlace
from mujoco import viewer


if __name__ == "__main__":
    robot = PandaPickAndPlace(xml_path="F:/mujoco_learning/szc_mujoco/mujoco_benchmark/robopal_part/assets/panda_pick_place.xml")
    with viewer.launch_passive(robot.robot_model, robot.robot_data) as viewer:

        viewer.sync()

        while viewer.is_running():

            # Step the physics.
            mujoco.mj_step(robot.robot_model, robot.robot_data)

            viewer.sync()
    