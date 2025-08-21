import os
import numpy as np
import mujoco
import copy
import logging

class PandaPickAndPlace():
    """ Panda robot base class. """
    def __init__(self,
                 xml_path=None
                 ):
        if xml_path ==None:
            logging.info(f'not have model file, please give a path')
            raise TypeError
        self.robot_model = mujoco.MjModel.from_xml_path(filename=xml_path, assets=None)
        self.robot_data = mujoco.MjData(self.robot_model)
        # deepcopy for computing kinematics.
        self.kine_data: mujoco.MjData = copy.deepcopy(self.robot_data)
        self.arm_joint_names = {self.__class__.__name__: ['0_joint1', '0_joint2', '0_joint3', '0_joint4', '0_joint5', '0_joint6', '0_joint7']}
        self.arm_actuator_names = {self.__class__.__name__: ['0_actuator1', '0_actuator2', '0_actuator3', '0_actuator4', '0_actuator5', '0_actuator6', '0_actuator7']}
        self.base_link_name = {self.__class__.__name__: '0_link0'}
        self.end_name = {self.__class__.__name__: '0_attachment'}

        self.pos_max_bound = np.array([0.6, 0.2, 0.37])
        self.pos_min_bound = np.array([0.3, -0.2, 0.02])

    @property
    def init_qpos(self):
        """ Robot's init joint position. """
        return {self.agents[0]: np.array([-0.61,  -0.84,  0.47, -2.54,  0.35,  1.75, 0.44])}
