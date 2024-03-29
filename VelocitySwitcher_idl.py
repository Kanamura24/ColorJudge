# Python stubs generated by omniidl from idl/VelocitySwitcher.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "KanamuraRobotics"
#
__name__ = "KanamuraRobotics"
_0_KanamuraRobotics = omniORB.openModule("KanamuraRobotics", r"idl/VelocitySwitcher.idl")
_0_KanamuraRobotics__POA = omniORB.openModule("KanamuraRobotics__POA", r"idl/VelocitySwitcher.idl")


# interface VelocitySwitcherService
_0_KanamuraRobotics._d_VelocitySwitcherService = (omniORB.tcInternal.tv_objref, "IDL:KanamuraRobotics/VelocitySwitcherService:1.0", "VelocitySwitcherService")
omniORB.typeMapping["IDL:KanamuraRobotics/VelocitySwitcherService:1.0"] = _0_KanamuraRobotics._d_VelocitySwitcherService
_0_KanamuraRobotics.VelocitySwitcherService = omniORB.newEmptyClass()
class VelocitySwitcherService :
    _NP_RepositoryId = _0_KanamuraRobotics._d_VelocitySwitcherService[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_KanamuraRobotics.VelocitySwitcherService = VelocitySwitcherService
_0_KanamuraRobotics._tc_VelocitySwitcherService = omniORB.tcInternal.createTypeCode(_0_KanamuraRobotics._d_VelocitySwitcherService)
omniORB.registerType(VelocitySwitcherService._NP_RepositoryId, _0_KanamuraRobotics._d_VelocitySwitcherService, _0_KanamuraRobotics._tc_VelocitySwitcherService)

# VelocitySwitcherService operations and attributes
VelocitySwitcherService._d_getSwitch = ((), (omniORB.tcInternal.tv_boolean, ), None)
VelocitySwitcherService._d_setSwitch = ((omniORB.tcInternal.tv_boolean, ), (omniORB.tcInternal.tv_long, ), None)

# VelocitySwitcherService object reference
class _objref_VelocitySwitcherService (CORBA.Object):
    _NP_RepositoryId = VelocitySwitcherService._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def getSwitch(self, *args):
        return _omnipy.invoke(self, "getSwitch", _0_KanamuraRobotics.VelocitySwitcherService._d_getSwitch, args)

    def setSwitch(self, *args):
        return _omnipy.invoke(self, "setSwitch", _0_KanamuraRobotics.VelocitySwitcherService._d_setSwitch, args)

    __methods__ = ["getSwitch", "setSwitch"] + CORBA.Object.__methods__

omniORB.registerObjref(VelocitySwitcherService._NP_RepositoryId, _objref_VelocitySwitcherService)
_0_KanamuraRobotics._objref_VelocitySwitcherService = _objref_VelocitySwitcherService
del VelocitySwitcherService, _objref_VelocitySwitcherService

# VelocitySwitcherService skeleton
__name__ = "KanamuraRobotics__POA"
class VelocitySwitcherService (PortableServer.Servant):
    _NP_RepositoryId = _0_KanamuraRobotics.VelocitySwitcherService._NP_RepositoryId


    _omni_op_d = {"getSwitch": _0_KanamuraRobotics.VelocitySwitcherService._d_getSwitch, "setSwitch": _0_KanamuraRobotics.VelocitySwitcherService._d_setSwitch}

VelocitySwitcherService._omni_skeleton = VelocitySwitcherService
_0_KanamuraRobotics__POA.VelocitySwitcherService = VelocitySwitcherService
omniORB.registerSkeleton(VelocitySwitcherService._NP_RepositoryId, VelocitySwitcherService)
del VelocitySwitcherService
__name__ = "KanamuraRobotics"

#
# End of module "KanamuraRobotics"
#
__name__ = "VelocitySwitcher_idl"

_exported_modules = ( "KanamuraRobotics", )

# The end.
