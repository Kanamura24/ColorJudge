#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ColorJudgeTest.py
 @brief judge the color of anemy 
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import VelocitySwitcher_idl
import Img

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import KanamuraRobotics, KanamuraRobotics__POA
import Img, Img__POA


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
colorjudgetest_spec = ["implementation_id", "ColorJudgeTest", 
		 "type_name",         "ColorJudgeTest", 
		 "description",       "judge the color of anemy ", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.team_color", "red",

		 "conf.__widget__.team_color", "radio",
		 "conf.__constraints__.team_color", "(red, blue)",

         "conf.__type__.team_color", "long",

		 ""]
# </rtc-template>

##
# @class ColorJudgeTest
# @brief judge the color of anemy 
# 
# 
class ColorJudgeTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_color = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
		"""
		"""
		self._colorIn = OpenRTM_aist.InPort("color", self._d_color)
		self._d_cameraImage = OpenRTM_aist.instantiateDataType(Img.TimedCameraImage)
		"""
		"""
		self._cameraImageOut = OpenRTM_aist.OutPort("cameraImage", self._d_cameraImage)

		"""
		"""
		self._colorSwitcherPort = OpenRTM_aist.CorbaPort("colorSwitcher")

		"""
		"""
		self._colorSwitcherService = VelocitySwitcherService_i()
		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  team_color
		 - DefaultValue: red
		"""
		self._team_color = [red]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("team_color", self._team_color, "red")
		
		# Set InPort buffers
		self.addInPort("color",self._colorIn)
		
		# Set OutPort buffers
		self.addOutPort("cameraImage",self._cameraImageOut)
		
		# Set service provider to Ports
		self._colorSwitcherPort.registerProvider("KanamuraRobotics::VelocitySwitcherService", "KanamuraRobotics::VelocitySwitcherService", self._colorSwitcherService)
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		self.addPort(self._colorSwitcherPort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def ColorJudgeTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=colorjudgetest_spec)
    manager.registerFactory(profile,
                            ColorJudgeTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ColorJudgeTestInit(manager)

    # Create a component
    comp = manager.createComponent("ColorJudgeTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

