import time

import mujoco
from mujoco import viewer

m = mujoco.MjModel.from_xml_path('F:/mujoco_learning/szc_mujoco/mujoco_benchmark/robotic_assets/panda/panda_robot.xml')
d = mujoco.MjData(m)

with viewer.launch_passive(m, d) as viewer:

    viewer.sync()

    while viewer.is_running():

        # Step the physics.
        mujoco.mj_step(m, d)

        viewer.sync()
    