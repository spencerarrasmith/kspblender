# KSPBlender 1.04
# 1/1/15
# Spencer Arrasmith

#############################
### IMPORT STUFF
#############################

import os, string, time
import bpy, mathutils, math
os.chdir("C:\\Users\\Spencer.Satan-PC\\Art\\Projects\\ksp\\kspblender") # current working directory... need to have the .craft file in this same folder for now

#FIGURE OUT A BETTER WAY TO MANAGE OPENING CONSOLE
#bpy.ops.wm.console_toggle()

#############################
### DIRECTORY STUFF
#############################

kspexedirectory = "S:\\Games\\SteamApps\\common\\Kerbal Space Program"

def partdirectory():
    """Makes a big stupid dictionary of where each part is located. Making this function sucked."""
    
    partdir = {}
    
    # Pods
    partdir['mk1pod']                   = ["\\GameData\\Squad\\Parts\\Command\\mk1pod\\model.mu","pod"]
    partdir['seatExternalCmd']          = ["\\GameData\\Squad\\Parts\\Command\\externalCommandSeat\\model.mu","pod"]
    partdir['Mark1Cockpit']             = ["\\GameData\\Squad\\Parts\\Command\\mk1Cockpit\\model.mu","pod"]
    partdir['Mark2Cockpit']             = ["\\GameData\\Squad\\Parts\\Command\\mk1InlineCockpit\\model.mu","pod"]
    partdir['landerCabinSmall']         = ["\\GameData\\Squad\\Parts\\Command\\mk1LanderCan\\model.mu","pod"]
    partdir['Mark1-2Pod']               = ["\\GameData\\Squad\\Parts\\Command\\Mk1-2Pod\\model.mu","pod"]
    partdir['mk2Cockpit.Standard']      = ["\\GameData\\Squad\\SPP\\Mk2CockpitStandard\\model.mu","pod"]
    partdir['mk2DroneCore']             = ["\\GameData\\Squad\\SPP\\Mk2DroneCore\\model.mu","pod"]
    partdir['mk2Cockpit.Inline']        = ["\\GameData\\Squad\\SPP\\Mk2Cockpit_Inline\\model.mu","pod"]
    partdir['mk2LanderCabin']           = ["\\GameData\\Squad\\Parts\\Command\\mk2LanderCan\\model.mu","pod"]
    partdir['mk3Cockpit.Shuttle']       = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Cockpit_Shuttle\\model.mu","pod"]
    partdir['cupola']                   = ["\\GameData\\Squad\\Parts\\Command\\cupola\\model.mu","pod"]
    partdir['probeCoreHex']             = ["\\GameData\\Squad\\Parts\\Command\\probeCoreHex\\model.mu","pod"]
    partdir['probeCoreOcto']            = ["\\GameData\\Squad\\Parts\\Command\\probeCoreOcto\\model.mu","pod"]
    partdir['probeCoreOcto2']           = ["\\GameData\\Squad\\Parts\\Command\\probeCoreOcto2\\model.mu","pod"]
    partdir['probeCoreCube']            = ["\\GameData\\Squad\\Parts\\Command\\probeCoreCube\\model.mu","pod"]
    partdir['probeStackSmall']          = ["\\GameData\\Squad\\Parts\\Command\\probeStackSmall\\model.mu","pod"]
    partdir['probeStackLarge']          = ["\\GameData\\Squad\\Parts\\Command\\probeStackLarge\\model.mu","pod"]
    partdir['probeCoreSphere']          = ["\\GameData\\Squad\\Parts\\Command\\probeStackSphere\\model.mu","pod"]
    
    # Fuel Tanks
    partdir['adapterSize2-Mk2']         = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Size2-Mk2.mu","fuel"]
    partdir['adapterSize2-Size1']       = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Size2-Size1.mu","fuel"]
    partdir['adapterSize2-Size1Slant']  = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Size2-Size1Slant.mu","fuel"]
    partdir['RCSTank1-2']               = ["\\GameData\\Squad\\Parts\\FuelTank\\RCSFuelTankR1\\model.mu","fuel"]
    partdir['rcsTankMini']              = ["\\GameData\\Squad\\Parts\\FuelTank\\RCSFuelTankR10\\model.mu","fuel"]
    partdir['RCSFuelTank']              = ["\\GameData\\Squad\\Parts\\FuelTank\\RCSFuelTankR25\\model.mu","fuel"]
    partdir['fuelTankSmallFlat']        = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankT100\\model.mu","fuel"]
    partdir['fuelTankSmall']            = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankT200\\model.mu","fuel"]
    partdir['fuelTank']                 = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankT400\\model.mu","fuel"]
    partdir['fuelTank.long']            = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankT800\\model.mu","fuel"]
    partdir['fuelLine']                 = ["\\GameData\\Squad\\Parts\\CompoundParts\\fuelLine\\model.mu","fuel"]
    partdir['Size3LargeTank']           = ["\\GameData\\NASAmission\\Parts\\Size3LargeTank\\Size3LargeTank.mu","fuel"]
    partdir['Size3SmallTank']           = ["\\GameData\\NASAmission\\Parts\\Size3SmallTank\\Size3SmallTank.mu","fuel"]
    partdir['Size3MediumTank']          = ["\\GameData\\NASAmission\\Parts\\Size3MediumTank\\Size3MediumTank.mu","fuel"]
    partdir['MK1Fuselage']              = ["\\GameData\\Squad\\Parts\\Mk1\\mk1fuselage.mu","fuel"]
    partdir['mk2.1m.Bicoupler']         = ["\\GameData\\Squad\\SPP\\Mk2Adapters\\bicoupler.mu","fuel"]
    partdir['mk2Fuselage']              = ["\\GameData\\Squad\\SPP\\Mk2FuselageLong\\FuselageLongLiquid.mu","fuel"]
    partdir['mk2FuselageShortLiquid']   = ["\\GameData\\Squad\\SPP\\Mk2FuselageShort\\FuselageShortLiquid.mu","fuel"]
    partdir['mk2FuselageShortMono']     = ["\\GameData\\Squad\\SPP\\Mk2FuselageShort\\FuselageShortMono.mu","fuel"]
    partdir['mk2FuselageLongLFO']       = ["\\GameData\\Squad\\SPP\\Mk2FuselageLong\\FuselageLongLFO.mu","fuel"]
    partdir['mk2FuselageShortLFO']      = ["\\GameData\\Squad\\SPP\\Mk2FuselageShort\\FuselageShortLFO.mu","fuel"]
    partdir['mk2SpacePlaneAdapter']     = ["\\GameData\\Squad\\SPP\\Mk2Adapters\\standard.mu","fuel"]
    partdir['mk2.1m.AdapterLong']       = ["\\GameData\\Squad\\SPP\\Mk2Adapters\\long.mu","fuel"]
    partdir['mk3FuselageLF.50']         = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LF_50.mu","fuel"]
    partdir['mk3FuselageLF.100']        = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LF_100.mu","fuel"]
    partdir['mk3FuselageLF.25']         = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LF_25.mu","fuel"]
    partdir['mk3FuselageMONO']          = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\MONO.mu","fuel"]
    partdir['mk3FuselageLFO.50']        = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LFO_50.mu","fuel"]
    partdir['mk3FuselageLFO.100']       = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LFO_100.mu","fuel"]
    partdir['mk3FuselageLFO.25']        = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\LFO_25.mu","fuel"]
    partdir['adapterMk3-Size2']         = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Mk3-Size2.mu","fuel"]
    partdir['adapterMk3-Size2Slant']    = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Mk3-Size2Slant.mu","fuel"]
    partdir['adapterSize3-Mk3']         = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Size3-Mk3.mu","fuel"]
    partdir['adapterMk3-Mk2']           = ["\\GameData\\Squad\\Parts\\FuelTank\\adapterTanks\\Mk3-Mk2.mu","fuel"]
    partdir['miniFuelTank']             = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankOscarB\\model.mu","fuel"]
    partdir['xenonTank']                = ["\\GameData\\Squad\\Parts\\FuelTank\\xenonTank\\model.mu","fuel"]
    partdir['xenonTankRadial']          = ["\\GameData\\Squad\\Parts\\FuelTank\\xenonTankRadial\\model.mu","fuel"]
    partdir['fuelTank3-2']              = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankJumbo-64\\model.mu","fuel"]
    partdir['fuelTank2-2']              = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankX200-16\\model.mu","fuel"]
    partdir['fuelTank1-2']              = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankX200-32\\model.mu","fuel"]
    partdir['fuelTank4-2']              = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankX200-8\\model.mu","fuel"]
    partdir['toroidalFuelTank']         = ["\\GameData\\Squad\\Parts\\FuelTank\\fuelTankToroidal\\model.mu","fuel"]
    partdir['rcsTankRadialLong']        = ["\\GameData\\Squad\\Parts\\FuelTank\\RCStankRadialLong\\model.mu","fuel"]
    partdir['radialRCSTank']            = ["\\GameData\\Squad\\Parts\\FuelTank\\RCSTankRadial\\model.mu","fuel"]
    
    # Engines
    partdir['JetEngine']                = ["\\GameData\\Squad\\Parts\\Engine\\jetEngineBasic\\model.mu","engine"]
    partdir['Size3AdvancedEngine']      = ["\\GameData\\NASAmission\\Parts\\Size3AdvancedEngine\\Size3AdvancedEngine.mu","engine"]
    partdir['Size2LFB']                 = ["\\GameData\\NASAmission\\Parts\\Size2LFB\\Size2LFB.mu","engine"]
    partdir['microEngine']              = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-1\\model.mu","engine"]
    partdir['radialEngineMini']         = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-1R\\model.mu","engine"]
    partdir['liquidEngine3']            = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-909\\model.mu","engine"]
    partdir['nuclearEngine']            = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-N\\model.mu","engine"]
    partdir['liquidEngine']             = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-T30\\model.mu","engine"]
    partdir['liquidEngine2']            = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineLV-T45\\model.mu","engine"]
    partdir['omsEngine']                = ["\\GameData\\Squad\\Parts\\Engine\\OMSEngine\\NewModel.mu","engine"]
    partdir['ionEngine']                = ["\\GameData\\Squad\\Parts\\Engine\\ionEngine\\model.mu","engine"]
    partdir['RAPIER']                   = ["\\GameData\\Squad\\Parts\\Engine\\rapierEngine\\rapier.mu","engine"]
    partdir['liquidEngine1-2']          = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineMainsail\\model.mu","engine"]
    partdir['liquidEngine2-2']          = ["\\GameData\\Squad\\Parts\\Engine\\liquidEnginePoodle\\model.mu","engine"]
    partdir['engineLargeSkipper']       = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineSkipper\\model.mu","engine"]
    partdir['smallRadialEngine']        = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngine24-77\\model.mu","engine"]
    partdir['liquidEngineMini']         = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngine48-7S\\model.mu","engine"]
    partdir['solidBooster1-1']          = ["\\GameData\\Squad\\Parts\\Engine\\solidBoosterBACC\\model.mu","engine"]
    partdir['radialLiquidEngine1-2']    = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineMk55\\model.mu","engine"]
    partdir['solidBooster']             = ["\\GameData\\Squad\\Parts\\Engine\\solidBoosterRT-10\\model.mu","engine"]
    partdir['MassiveBooster']           = ["\\GameData\\NASAmission\\Parts\\MassiveSRB\\MassiveSRB.mu","engine"]
    partdir['Size3EngineCluster']       = ["\\GameData\\NASAmission\\Parts\\Size3EngineCluster\\Size3EngineCluster.mu","engine"]
    partdir['sepMotor1']                = ["\\GameData\\Squad\\Parts\\Engine\\solidBoosterSep\\model.mu","engine"]
    partdir['toroidalAerospike']        = ["\\GameData\\Squad\\Parts\\Engine\\liquidEngineAerospike\\model.mu","engine"]
    partdir['turboFanEngine']           = ["\\GameData\\Squad\\Parts\\Engine\\jetEngineTurbo\\model.mu","engine"]
    
    # Command and Control
    partdir['advSasModule']             = ["\\GameData\\Squad\\Parts\\Command\\inlineAdvancedStabilizer\\model.mu","control"]
    partdir['asasmodule1-2']            = ["\\GameData\\Squad\\Parts\\Command\\advancedSasModuleLarge\\model.mu","control"]
    partdir['linearRcs']                = ["\\GameData\\Squad\\Parts\\Utility\\linearRCS\\model.mu","control"]
    partdir['RCSBlock']                 = ["\\GameData\\Squad\\Parts\\Utility\\rcsBlockRV-105\\model.mu","control"]
    partdir['sasModule']                = ["\\GameData\\Squad\\Parts\\Command\\inlineReactionWheel\\model.mu","control"]
    partdir['vernierEngine']            = ["\\GameData\\Squad\\Parts\\Engine\\vernorEngine\\NewModel.mu","control"]
    
    # Structural
    partdir['stackPoint1']              = ["\\GameData\\Squad\\Parts\\Utility\\radialAttachmentPoint\\model.mu","structural"]
    partdir['strutCube']                = ["\\GameData\\Squad\\Parts\\Structural\\strutCubicOcto\\model.mu","structural"]
    partdir['strutConnector']           = ["\\GameData\\Squad\\Parts\\CompoundParts\\strutConnector\\model.mu","structural"]
    partdir['adapterSmallMiniTall']     = ["\\GameData\\Squad\\Parts\\Structural\\adapterSmallMiniTall\\model.mu","structural"]
    partdir['adapterSmallMiniShort']    = ["\\GameData\\Squad\\Parts\\Structural\\adapterSmallMiniShort\\model.mu","structural"]
    partdir['radialDecoupler1-2']       = ["\\GameData\\Squad\\Parts\\Utility\\decouplerRadialHDM\\model.mu","structural"]
    partdir['Size3to2Adapter']          = ["\\GameData\\NASAmission\\Parts\\Size3To2Adapter\\Size3Adapter.mu","structural"]
    partdir['structuralPanel1']         = ["\\GameData\\Squad\\Parts\\Structural\\structuralPanel1x1\\model.mu","structural"]
    partdir['structuralPanel2']         = ["\\GameData\\Squad\\Parts\\Structural\\structuralPanel2x2\\model.mu","structural"]
    partdir['structuralIBeam2']         = ["\\GameData\\Squad\\Parts\\Structural\\structuralIBeam200\\model.mu","structural"]
    partdir['structuralIBeam3']         = ["\\GameData\\Squad\\Parts\\Structural\\structuralIBeam200Pocket\\model.mu","structural"]
    partdir['structuralIBeam1']         = ["\\GameData\\Squad\\Parts\\Structural\\structuralIBeam650\\model.mu","structural"]
    partdir['trussAdapter']             = ["\\GameData\\Squad\\Parts\\Structural\\trussGirderAdapter\\model.mu","structural"]
    partdir['trussPiece1x']             = ["\\GameData\\Squad\\Parts\\Structural\\trussGirderL\\model.mu","structural"]
    partdir['trussPiece3x']             = ["\\GameData\\Squad\\Parts\\Structural\\trussGirderXL\\model.mu","structural"]
    partdir['noseConeAdapter']          = ["\\GameData\\Squad\\Parts\\Aero\\noseConeAdapter\\model.mu","structural"]
    partdir['strutOcto']                = ["\\GameData\\Squad\\Parts\\Structural\\strutOcto\\model.mu","structural"]
    partdir['roverBody']                = ["\\GameData\\Squad\\Parts\\Utility\\roverBody\\model.mu","structural"]
    partdir['largeAdapter']             = ["\\GameData\\Squad\\Parts\\Utility\\largeAdapter\\model.mu","structural"]
    partdir['largeAdapter2']            = ["\\GameData\\Squad\\Parts\\Utility\\largeAdapterShort\\model.mu","structural"]
    partdir['decoupler1-2']             = ["\\GameData\\Squad\\Parts\\Utility\\decouplerStack2m\\model.mu","structural"]
    partdir['stationHub']               = ["\\GameData\\Squad\\Parts\\Structural\\stationHub\\model.mu","structural"]
    partdir['smallHardpoint']           = ["\\GameData\\Squad\\Parts\\Structural\\smallHardpoint\\model.mu","structural"]
    partdir['Mk1FuselageStructural']    = ["\\GameData\\Squad\\Parts\\Mk1\\mk1structural.mu","structural"]
    partdir['structuralPylon']          = ["\\GameData\\Squad\\Parts\\Structural\\structuralPylon\\model.mu","structural"]
    partdir['structuralMiniNode']       = ["\\GameData\\Squad\\Parts\\Structural\\structuralMicronode\\model.mu","structural"]
    partdir['stackDecoupler']           = ["\\GameData\\Squad\\Parts\\Utility\\decouplerStackTR-18A\\model.mu","structural"]
    partdir['stackSeparator']           = ["\\GameData\\Squad\\Parts\\Utility\\decouplerSeparatorTR-18D\\model.mu","structural"]
    partdir['stackSeparatorMini']       = ["\\GameData\\Squad\\Parts\\Utility\\decouplerSeparatorTR-2C\\model.mu","structural"]
    partdir['stackDecouplerMini']       = ["\\GameData\\Squad\\Parts\\Utility\\decouplerStackTR-2V\\model.mu","structural"]
    partdir['size3Decoupler']           = ["\\GameData\\NASAmission\\Parts\\Size3Decoupler\\Size3Decoupler.mu","structural"]
    partdir['stackSeparatorBig']        = ["\\GameData\\Squad\\Parts\\Utility\\decouplerSeparatorTR-XL\\model.mu","structural"]
    partdir['launchClamp1']             = ["\\GameData\\Squad\\Parts\\Utility\\launchClamp1\\model.mu","structural"]
    partdir['radialDecoupler']          = ["\\GameData\\Squad\\Parts\\Utility\\decouplerRadialTT-38K\\model.mu","structural"]
    partdir['radialDecoupler2']         = ["\\GameData\\Squad\\Parts\\Utility\\decouplerRadialTT-70\\model.mu","structural"]
    partdir['stackTriCoupler']          = ["\\GameData\\Squad\\Parts\\Utility\\stackTriCoupler\\model.mu","structural"]
    partdir['stackBiCoupler']           = ["\\GameData\\Squad\\Parts\\Utility\\stackBiCoupler\\model.mu","structural"]
    partdir['adapterLargeSmallBi']      = ["\\GameData\\Squad\\Parts\\Structural\\adapterLargeSmallBi\\model.mu","structural"]
    partdir['stackQuadCoupler']         = ["\\GameData\\Squad\\Parts\\Utility\\stackQuadCoupler\\model.mu","structural"]
    partdir['adapterLargeSmallTri']     = ["\\GameData\\Squad\\Parts\\Structural\\adapterLargeSmallTri\\model.mu","structural"]
    partdir['adapterLargeSmallQuad']    = ["\\GameData\\Squad\\Parts\\Structural\\adapterLargeSmallQuad\\model.mu","structural"]
    
    # Aerodynamics
    partdir['AdvancedCanard']           = ["\\GameData\\Squad\\Parts\\Aero\\advancedCanard\\model.mu","aero"]
    partdir['noseCone']                 = ["\\GameData\\Squad\\Parts\\Aero\\aerodynamicNoseCone\\model.mu","aero"]
    partdir['R8winglet']                = ["\\GameData\\Squad\\Parts\\Aero\\wingletAV-R8\\model.mu","aero"]
    partdir['winglet']                  = ["\\GameData\\Squad\\Parts\\Aero\\wingletAV-T1\\model.mu","aero"]
    partdir['CircularIntake']           = ["\\GameData\\Squad\\Parts\\Utility\\CircularIntake\\model.mu","aero"]
    partdir['deltaWing']                = ["\\GameData\\Squad\\SPP\\Wings\\delta.mu","aero"]
    partdir['winglet3']                 = ["\\GameData\\Squad\\Parts\\Aero\\wingletDeltaDeluxe\\model.mu","aero"]
    partdir['StandardCtrlSrf']          = ["\\GameData\\Squad\\SPP\\Wings\\elevon1.mu","aero"]
    partdir['elevon3']                  = ["\\GameData\\Squad\\SPP\\Wings\\elevon3.mu","aero"]
    partdir['smallCtrlSrf']             = ["\\GameData\\Squad\\SPP\\Wings\\elevon4.mu","aero"]
    partdir['elevon5']                  = ["\\GameData\\Squad\\SPP\\Wings\\elevon5.mu","aero"]
    partdir['elevon2']                  = ["\\GameData\\Squad\\SPP\\Wings\\elevon2.mu","aero"]
    partdir['nacelleBody']              = ["\\GameData\\Squad\\Parts\\Structural\\engineNacelle\\model.mu","aero"]
    partdir['MK1IntakeFuselage']        = ["\\GameData\\Squad\\Parts\\Mk1\\mk1fuselageIntake.mu","aero"]
    partdir['rocketNoseCone']           = ["\\GameData\\Squad\\Parts\\Aero\\protectiveRocketNoseMk7\\model.mu","aero"]
    partdir['radialEngineBody']         = ["\\GameData\\Squad\\Parts\\Structural\\engineBodyRadial\\model.mu","aero"]
    partdir['ramAirIntake']             = ["\\GameData\\Squad\\Parts\\Utility\\ramAirIntake\\model.mu","aero"]
    partdir['shockConeIntake']          = ["\\GameData\\Squad\\SPP\\ShockConeIntake\\model.mu","aero"]
    partdir['delta.small']              = ["\\GameData\\Squad\\SPP\\Wings\\delta_small.mu","aero"]
    partdir['CanardController']         = ["\\GameData\\Squad\\Parts\\Aero\\standardCanard\\model.mu","aero"]
    partdir['standardNoseCone']         = ["\\GameData\\Squad\\Parts\\Aero\\standardNoseCone\\model.mu","aero"]
    partdir['IntakeRadialLong']         = ["\\GameData\\Squad\\SPP\\IntakeRadialLong\\IntakeRadial.mu","aero"]
    partdir['structuralWing']           = ["\\GameData\\Squad\\SPP\\Wings\\structural1.mu","aero"]
    partdir['structuralWing2']          = ["\\GameData\\Squad\\SPP\\Wings\\structural2.mu","aero"]
    partdir['structuralWing3']          = ["\\GameData\\Squad\\SPP\\Wings\\structural3.mu","aero"]
    partdir['structuralWing4']          = ["\\GameData\\Squad\\SPP\\Wings\\structural4.mu","aero"]
    partdir['sweptWing1']               = ["\\GameData\\Squad\\SPP\\Wings\\swept1.mu","aero"]
    partdir['sweptWing2']               = ["\\GameData\\Squad\\SPP\\Wings\\swept2.mu","aero"]
    partdir['sweptWing']                = ["\\GameData\\Squad\\Parts\\Aero\\sweptWing\\model.mu","aero"]
    partdir['airplaneTail']             = ["\\GameData\\Squad\\Parts\\Aero\\tailConnector\\model.mu","aero"]
    partdir['tailfin']                  = ["\\GameData\\Squad\\Parts\\Aero\\tailfin\\model.mu","aero"]
    partdir['wingConnector']            = ["\\GameData\\Squad\\SPP\\Wings\\connector1.mu","aero"]
    partdir['wingConnector2']           = ["\\GameData\\Squad\\SPP\\Wings\\connector2.mu","aero"]
    partdir['wingConnector3']           = ["\\GameData\\Squad\\SPP\\Wings\\connector3.mu","aero"]
    partdir['wingConnector4']           = ["\\GameData\\Squad\\SPP\\Wings\\connector4.mu","aero"]
    partdir['wingConnector5']           = ["\\GameData\\Squad\\SPP\\Wings\\connector5.mu","aero"]
    partdir['wingStrake']               = ["\\GameData\\Squad\\SPP\\Wings\\strake.mu","aero"]
    partdir['airScoop']                 = ["\\GameData\\Squad\\Parts\\Utility\\airIntakeRadialXM-G50\\model.mu","aero"]
    
    # Utility
    partdir['GrapplingDevice']          = ["\\GameData\\NASAmission\\Parts\\GrapplingDevice\\GrapplingArm.mu","utility"]
    partdir['dockingPort2']             = ["\\GameData\\Squad\\Parts\\Utility\\dockingPort\\model.mu","utility"]
    partdir['dockingPort3']             = ["\\GameData\\Squad\\Parts\\Utility\\dockingPortJr\\model.mu","utility"]
    partdir['dockingPortLarge']         = ["\\GameData\\Squad\\Parts\\Utility\\dockingPortSr\\model.mu","utility"]
    partdir['dockingPort1']             = ["\\GameData\\Squad\\Parts\\Utility\\dockingPortShielded\\model.mu","utility"]
    partdir['largeSolarPanel']          = ["\\GameData\\Squad\\Parts\\Electrical\\gigantorXlSolarArray\\model.mu","utility"]
    partdir['spotLight1']               = ["\\GameData\\Squad\\Parts\\Utility\\spotLightMk1\\model.mu","utility"]
    partdir['spotLight2']               = ["\\GameData\\Squad\\Parts\\Utility\\spotLightMk2\\model.mu","utility"]
    partdir['dockingPortLateral']       = ["\\GameData\\Squad\\Parts\\Utility\\dockingPortInline\\model.mu","utility"]
    partdir['LaunchEscapeSystem']       = ["\\GameData\\NASAmission\\Parts\\LaunchEscapeSystem\\LaunchEscapeSystem.mu","utility"]
    partdir['landingLeg1']              = ["\\GameData\\Squad\\Parts\\Utility\\landingLegLT-1\\model.mu","utility"]
    partdir['landingLeg1-2']            = ["\\GameData\\Squad\\Parts\\Utility\\landingLegLT-2\\model.mu","utility"]
    partdir['miniLandingLeg']           = ["\\GameData\\Squad\\Parts\\Utility\\landingLegLT-5\\model.mu","utility"]
    partdir['parachuteSingle']          = ["\\GameData\\Squad\\Parts\\Utility\\parachuteMk1\\model.mu","utility"]
    partdir['parachuteLarge']           = ["\\GameData\\Squad\\Parts\\Utility\\parachuteMk16-XL\\model.mu","utility"]
    partdir['mk2CargoBayS']             = ["\\GameData\\Squad\\SPP\\Mk2CargoBay\\BaySmall.mu","utility"]
    partdir['mk2CargoBayL']             = ["\\GameData\\Squad\\SPP\\Mk2CargoBay\\BayLarge.mu","utility"]
    partdir['mk2DockingPort']           = ["\\GameData\\Squad\\SPP\\Mk2DockingPort\\model.mu","utility"]
    partdir['mk2CrewCabin']             = ["\\GameData\\Squad\\SPP\\Mk2CrewCabin\\model.mu","utility"]
    partdir['parachuteDrogue']          = ["\\GameData\\Squad\\Parts\\Utility\\parachuteMk25\\model.mu","utility"]
    partdir['parachuteRadial']          = ["\\GameData\\Squad\\Parts\\Utility\\parachuteMk2-R\\model.mu","utility"]
    partdir['mk3CargoBayL']             = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3CargoBay\\long.mu","utility"]
    partdir['mk3CargoBayS']             = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3CargoBay\\short.mu","utility"]
    partdir['mk3CargoBayM']             = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3CargoBay\\medium.mu","utility"]
    partdir['mk3CrewCabin']             = ["\\GameData\\Squad\\Parts\\Mk3\\Mk3Fuselage\\CREW.mu","utility"]
    partdir['solarPanels4']             = ["\\GameData\\Squad\\Parts\\Electrical\\1x6SolarPanels\\model.mu","utility"]
    partdir['solarPanels3']             = ["\\GameData\\Squad\\Parts\\Electrical\\2x3SolarPanels\\model.mu","utility"]
    partdir['solarPanels5']             = ["\\GameData\\Squad\\Parts\\Electrical\\radialFlatSolarPanel\\model.mu","utility"]
    partdir['rtg']                      = ["\\GameData\\Squad\\Parts\\Electrical\\RTG\\model.mu","utility"]
    partdir['ladder1']                  = ["\\GameData\\Squad\\Parts\\Utility\\ladderRadial\\model.mu","utility"]
    partdir['crewCabin']                = ["\\GameData\\Squad\\Parts\\Command\\hitchhikerStorageContainer\\model.mu","utility"]
    partdir['roverWheel1']              = ["\\GameData\\Squad\\Parts\\Wheel\\roverWheelM1\\model.mu","utility"]
    partdir['roverWheel2']              = ["\\GameData\\Squad\\Parts\\Wheel\\roverWheelS2\\model.mu","utility"]
    partdir['roverWheel3']              = ["\\GameData\\Squad\\Parts\\Wheel\\roverWheelXL3\\model.mu","utility"]
    partdir['SmallGearBay']             = ["\\GameData\\Squad\\Parts\\Wheel\\SmallGearBay\\model.mu","utility"]
    partdir['solarPanels2']             = ["\\GameData\\Squad\\Parts\\Electrical\\1x6ShroudSolarPanels\\model.mu","utility"]
    partdir['solarPanels1']             = ["\\GameData\\Squad\\Parts\\Electrical\\2x3ShroudSolarPanels\\model.mu","utility"]
    partdir['telescopicLadder']         = ["\\GameData\\Squad\\Parts\\Utility\\ladderTelescopic\\model.mu","utility"]
    partdir['telescopicLadderBay']      = ["\\GameData\\Squad\\Parts\\Utility\\ladderTelescopicBay\\model.mu","utility"]
    partdir['wheelMed']                 = ["\\GameData\\Squad\\Parts\\Wheel\\roverWheelTR-2L\\model.mu","utility"]
    partdir['batteryPack']              = ["\\GameData\\Squad\\Parts\\Electrical\\z-100Battery\\model.mu","utility"]
    partdir['batteryBank']              = ["\\GameData\\Squad\\Parts\\Electrical\\z-1kBattery\\model.mu","utility"]
    partdir['batteryBankMini']          = ["\\GameData\\Squad\\Parts\\Electrical\\z-200Battery\\model.mu","utility"]
    partdir['ksp.r.largeBatteryPack']   = ["\\GameData\\Squad\\Parts\\Electrical\\z-400Battery\\model.mu","utility"]
    partdir['batteryBankLarge']         = ["\\GameData\\Squad\\Parts\\Electrical\\z-4kBattery\\model.mu","utility"]
    
    # Science
    partdir['sensorThermometer']        = ["\\GameData\\Squad\\Parts\\Utility\\sensorThermometer\\model.mu","science"]
    partdir['mediumDishAntenna']        = ["\\GameData\\Squad\\Parts\\Utility\\commsAntennaDTS-M1\\mediumDishAntenna.mu","science"]
    partdir['longAntenna']              = ["\\GameData\\Squad\\Parts\\Utility\\commsDish16\\model.mu","science"]
    partdir['commDish']                 = ["\\GameData\\Squad\\Parts\\Utility\\commDish88-88\\model.mu","science"]
    partdir['sensorAccelerometer']      = ["\\GameData\\Squad\\Parts\\Utility\\sensorAccelerometer\\model.mu","science"]
    partdir['sensorGravimeter']         = ["\\GameData\\Squad\\Parts\\Utility\\sensorGravimeter\\model.mu","science"]
    partdir['Large.Crewed.Lab']         = ["\\GameData\\Squad\\Parts\\Science\\LargeCrewedLab\\large_crewed_lab.mu","science"]
    partdir['GooExperiment']            = ["\\GameData\\Squad\\Parts\\Science\\GooExperiment\\GooExperiment.mu","science"]
    partdir['sensorBarometer']          = ["\\GameData\\Squad\\Parts\\Utility\\sensorBarometer\\model.mu","science"]
    partdir['science.module']           = ["\\GameData\\Squad\\Parts\\Science\\MaterialBay\\science_module_small.mu","science"]
    partdir['avionicsNoseCone']         = ["\\GameData\\Squad\\Parts\\Science\\avionicsNoseCone\\model.mu","science"]

    return partdir

#############################
### PARSING STUFF
#############################

partdir = partdirectory()

def part_dir_part1(partslist):
    f = open('partdirpart1.txt','w')
    for part in partslist:
        f.write("partdir['"+part.partName+"'] = \n")
    f.close()

def zup_tuple(line):
    """changes from Unity Y-up world to Blender Z-up world"""
    zup = [float(i) for i in line.split(" ")[-1].split(",")]
    zup[1], zup[2] = zup[2], zup[1]
    return tuple(zup)

def zup_eul(line):
    """changes from Unity Y-up Left-Handed Quaternion to Blender Z-up Right-Handed Euler"""
    zup = [float(i) for i in line.split(" ")[-1].split(",")]
    zup = mathutils.Quaternion([0-zup[3], zup[0], zup[2], zup[1]])
    return (mathutils.Quaternion.to_euler(zup).x, mathutils.Quaternion.to_euler(zup).y, mathutils.Quaternion.to_euler(zup).z)

def zup_quat(line):
    """changes from Unity Y-up Left-Handed Quaternion to Blender Z-up Right-Handed Quaternion"""
    zup = [float(i) for i in line.split(" ")[-1].split(",")]
    zup = mathutils.Quaternion([0-zup[3], zup[0], zup[2], zup[1]])
    return (zup[0],zup[1],zup[2],zup[3])


class kspcraft:
    """A Kerbal Space Program craft lol"""
    def __init__(self,filename):
        self.filename = filename
        self.lines = None
        self.ship = None
        self.version = None
        self.description = None
        self.type = None
        self.size = None
        self.partslist = []

        self.parse_file()
        self.set_data(self.lines[0:5])
        self.set_partslist(self.lines)

    def num_parts(self):
        """method to count the number of parts in the ship, as a sanity check"""
        try:
            return len(self.partslist)
        except TypeError:
            return 0
    
    def parse_file(self):
        """read in the plaintext .craft file"""
        fileobj = open(self.filename)
        text = fileobj.read()
        fileobj.close()
        self.lines = text.splitlines()

    def set_data(self,lines):
        """read over the first 5 lines to set ship data"""
        self.ship = " ".join(lines[0].split(" ")[2:])
        self.version = lines[1].split(" ")[2]
        self.description = " ".join(lines[2].split(" ")[2:])
        self.type = lines[3].split(" ")[2]
        self.size = zup_tuple(lines[4])

    def set_partslist(self,lines):
        """find parts data by looking between each unindented { and the following \tEVENTS (\t is indentation)"""
        startindices = []
        endindices = []
        for i in range(len(self.lines)):
            if self.lines[i]=="{":
                startindices.append(i)
            if self.lines[i]=="\tEVENTS":
                endindices.append(i)

        for i in range(len(startindices)):
            self.partslist.append(part(self.lines[startindices[i]:endindices[i]]))



class part:
    """A part for a ship lol"""
    def __init__(self,lines):
        self.lines = lines
        self.part = None
        self.partNumber = None
        self.partName = None
        self.partClass = None
        self.pos = None
        self.attPos = None
        self.attPos0 = None
        self.rot = None
        self.attRot = None
        self.attRot0 = None
        self.rotQ = None
        self.mir = None
        self.symMethod = None
        self.istg = None
        self.dstg = None
        self.sidx = None
        self.sqor = None
        self.attm = None
        self.modCost = None
        self.modMass = None
        self.modSize = None
        self.linklist = []
        self.attNlist = []
        self.symlist = []
        self.srfNlist = []

        self.set_data(self.lines)

    def set_data(self,lines):
        """set part data based on first word of each line"""
        for line in lines:
            if line.split()[0] == "part":
                self.part = line.split(" ")[2]                                  #"part = Mark1-2Pod_4293084140" -> "Mark1-2Pod_4293084140" for object name
                self.partNumber = int(line.split("_")[1])                       #"part = Mark1-2Pod_4293084140" -> 4293084140 higher = higher in hierarchy (and to distinguish objects)
                self.partName = "".join(line.split("_")[0:-1]).split()[-1]      #"part = Mark1-2Pod_4293084140" -> "Mark1-2Pod" for mesh name
            #if line.split()[0] == "partName":
                #self.partName = " ".join(line.split()[2:])                     #"partName = Part" -> seems to always be Part, so kinda useless
            if line.split()[0] == "pos":
                self.pos = zup_tuple(line)                                      #"pos = 0.003080267,7.645381,0.02017996" -> (0.003080267, 0.02017996, 7.645381)
            if line.split()[0] == "attPos":
                self.attPos = zup_tuple(line)                                   #"attPos = 0,0,0" -> (0,0,0) y<>z, attachment position? always seems to be (0,0,0)
            if line.split()[0] == "attPos0":
                self.attPos0 = zup_tuple(line)                                  #"attPos0 = 0,0,0" -> (0,0,0) y<>z, seems to always be (0,0,0) also
            if line.split()[0] == "rot":
                self.rot = zup_eul(line)                                        #"rot = 0,0,0,1" -> (-1,0,0,0) w to beginning, y<>z, made right-handed, converted to Euler angles
                self.rotQ = zup_quat(line)                                      #"rot = 0,0,0,1" -> (-1,0,0,0) w to beginning, y<>z, made right-handed
            if line.split()[0] == "attRot":
                self.attRot = zup_eul(line)                                     #"attRot = 0,0,0,1" -> (-1,0,0,0) w to beginning, y<>z, made right-handed
            if line.split()[0] == "attRot0":
                self.attRot0 = zup_eul(line)                                    #"attRot0 = 0,0,0,1" -> (-1,0,0,0) w to beginning, y<>z, made right-handed
            if line.split()[0] == "mir":
                self.mir = zup_tuple(line)                                      #"mir = 1,1,1" -> (1,1,1) not really sure what this is for
            if line.split()[0] == "symMethod":
                self.symMethod = line.split(" ")[2]                             #"symMethod = Radial" -> "Radial" would be different in SPH
            if line.split()[0] == "istg":
                self.istg = int(line.split()[2])                                #"istg = 0" -> 0 _______________?
            if line.split()[0] == "dstg":
                self.dstg = int(line.split()[2])                                #"dstg = 0" -> 0 ________________?
            if line.split()[0] == "sidx":
                self.sidx = int(line.split()[2])                                #"sidx = -1" -> -1 ______________?
            if line.split()[0] == "sqor":
                self.sqor = int(line.split()[2])                                #"sqor = -1" -> -1 _____________?
            if line.split()[0] == "attm":
                self.attm = int(line.split()[2])                                #"attm = 0" -> 0 boolean for "is attachment?" thing that can be attached onto surface rather than connection node
            if line.split()[0] == "modCost":
                self.modCost = float(line.split()[2])                           #"modCost = 0" -> 0 ____________? (always 0)
            if line.split()[0] == "modMass":
                self.modMass = float(line.split()[2])                           #"modMass = 0" -> _______________? (always 0)
            if line.split()[0] == "modSize":                                    #(line below this one) "modSize = (0.0, 0.0, 0.0)" -> (0.0, 0.0, 0.0), y<>z
                self.modSize = tuple([float(" ".join(line.split()[2:]).split(", ")[0][1:]), float(" ".join(line.split()[2:]).split(", ")[2][0:-1]), float(" ".join(line.split()[2:]).split(", ")[1])])
            if line.split()[0] == "link":
                self.linklist.append(link(line))                                #new entry in list of links with new link instance
            if line.split()[0] == "attN":
                self.attNlist.append(attN(line))                                #new entry in list of attachments with new attN instance
            if line.split()[0] == "sym":
                self.symlist.append(sym(line))                                  #new entry in symmetrical parts list with new sym instance
            if line.split()[0] == "srfN":
                self.srfNlist.append(srfN(line))                                #"srfN = srfAttach,RCSTank1-2_4293083910" -> new entry in surface-attached-to list with new srfN instance


class link:
    """A link for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.part = line.split(" ")[2]                                          #"link = parachuteLarge_4293084050" -> "parachuteLarge_4293084050"
        self.partNumber = int(line.split("_")[1])                               #"link = parachuteLarge_4293084050" -> 4293084050 use this number to figure out parenting hierarchy (link and higher -> set as parent) need to set as a property


class attN:
    """An attN for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.loc = None
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.loc = line.split(" ")[2].split(",")[0]                             #"attN = bottom,decoupler1-2_4293084002" -> "bottom" may need this info at some point
        self.part = line.split(" ")[2].split(",")[1]                            #"attN = bottom,decoupler1-2_4293084002" -> "decoupler1-2_4293084002" 
        self.partNumber = int(line.split("_")[1])                               #"attN = bottom,decoupler1-2_4293084002" -> 4293084002


class sym:
    """A sym for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.part = line.split(" ")[2]                                          #"sym = RCSBlock_4293083644" -> "RCSBlock_4293083644"
        self.partNumber = int(line.split("_")[1])                               #"sym = RCSBlock_4293083644" -> 4293083644 also move/rotate/scale symmetrical parts maybe?
        

class srfN:
    """A srfN for a part for a ship lol"""
    def __init__(self,line):
        self.line = line
        self.type = None
        self.part = None
        self.partNumber = None

        self.set_data(self.line)

    def set_data(self,line):
        self.type = line.split(" ")[2].split(",")[0]                            #"srfN = srfAttach,RCSTank1-2_4293083910" -> "srfAttach"
        self.part = line.split(" ")[2].split(",")[1]                            #"srfN = srfAttach,RCSTank1-2_4293083910" -> "RCSTank1-4293083910"
        self.partNumber = int(line.split("_")[1])                               #"srfN = srfAttach,RCSTank1-2_4293083910" -> 4293083910


#############################
### BLENDER STUFF
#############################

def addcubes_dumb(partslist):
    """adds a cube in a dumb way with the rotation and location of each part"""
    for part in partslist:
        bpy.ops.mesh.primitive_cube_add(radius = 1, location = part.pos, rotation = (mathutils.Quaternion.to_euler(part.rot).x, mathutils.Quaternion.to_euler(part.rot).y, mathutils.Quaternion.to_euler(part.rot).z))

def addcubes(partslist):
    """adds a cube in an intelligent way with the rotation and location of each part"""
    for part in partslist:
        me = bpy.data.meshes.get('Cube')
        ob = bpy.data.objects.new(part.part, me)
        ob.location = part.pos
        ob.rotation_euler = part.rot
        
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True
        
        tex = bpy.ops.object.text_add()
        tex = bpy.context.object
        tex.data.body = "".join(["    -",part.part])
        tex.scale = (.001,.001,.001)
        tex.rotation_euler = (math.pi/2,0,0)
        tex.location = part.pos
#        scn.objects.link(tex)
#        scn.objects.active = tex

def add_parts(partslist):
    """adds parts, given that the meshes exist"""
    for part in partslist:
        me = bpy.data.meshes.get(part.partName)
        ob = bpy.data.objects.new(part.part, me)
        ob.location = part.pos
        #ob.rotation_quaternion = part.rotQ
        ob.rotation_euler = part.rot
        
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True
        
def import_parts_old(partslist,ksp):
    """Imports parts from the ksp directory"""
    for part in partslist:
        if os.path.isfile(ksp+partdir[part.partName]):
            print("Importing "+part.partName)
            bpy.ops.import_object.ksp_mu(filepath=ksp+partdir[part.partName])
            newpart = bpy.context.active_object
            newpart.name = part.part
            newpart.name = part.part
            newpart.location = part.pos
            newpart.rotation_quaternion = part.rotQ
        else:
            print("Failed to load "+part.partName+"... gotta fix that")
    for object in bpy.data.objects:
        if object.type == 'MESH' and "KSP" not in object.name:
            while len(object.data.materials) > 0:
                object.data.materials.pop(0, update_data=True)
                bpy.ops.object.material_slot_remove()
            if "coll" in object.name or "COL" in object.name or "fair" in object.name:
                object.hide = True
                object.hide_render = True
                #object.select = True
                #bpy.ops.object.delete()
                print(object.name + " Hidden")


def import_parts(partslist,ksp):
    """Imports parts from the ksp directory"""
    
    doneparts = {}                                                                                          # keep track of parts that have already been imported so I can save time
    doneobj = set(bpy.data.objects)                                                                         # know which objects have gone through the cleaning process
    scn = bpy.context.scene                                                                                 # the active scene
    
    for part in partslist:
        if os.path.isfile(ksp+partdir[part.partName][0]):                                                      # make sure the part file exists so nothing crashes
            print("\n----------------------------------------------------\n")                               # to make console output easier to look at
            if part.partName not in doneparts:                                                              # if part has not been imported...
                print("Importing "+part.partName+" as "+part.part)                                                               # ...say so on the console
                print("\n")
                bpy.ops.import_object.ksp_mu(filepath=ksp+partdir[part.partName][0])                               # call the importer
                newpart = bpy.context.active_object                                                             # set the imported part object to active. from here on, part refers to the part data structure and object to the blender object
                newpart.name = part.part                                                                        # rename the object according to the part name (including the number)
                newpart.location = part.pos                                                                     # move the object
                newpart.rotation_quaternion = part.rotQ                                                         # rotate the object
                
                # Set a bunch of properties
                newpart["partName"] = part.partName
                newpart["partClass"] = partdir[part.partName][1]
                newpart["mir"] = part.mir
                newpart["symMethod"] = part.symMethod
                newpart["istg"] = part.istg
                newpart["dstg"] = part.dstg
                newpart["sidx"] = part.sidx
                newpart["sqor"] = part.sqor
                newpart["attm"] = part.attm
                newpart["modCost"] = part.modCost
                newpart["modMass"] = part.modMass
                newpart["modSize"] = part.modSize
                #newpart["linklist"] = part.linklist
                #newpart["attNlist"] = part.attNlist
                #newpart["symlist"] = part.symlist
                #newpart["srfNlist"] = part.srfNlist ### FIX THESE
                
                
            else:                                                                                           # but if part has been imported...
                hiddenlist = []                                                                                 # clunky workaround
                for obj in bpy.data.objects:                                                                    # hidden objects cannot be modified (duplication is what I want to do)
                    if not obj.is_visible(scn):                                                                     # find all hidden objects
                        hiddenlist.append(obj)                                                                      # create a big stupid list
                        scn.objects.active = obj                                                                    # always need to do this to get things to actually happen to objects
                        obj.hide = False                                                                            # unhide each one
                bpy.ops.object.select_all(action = 'DESELECT')                                                  # deselect everything
                print("Duplicating "+part.partName+" as "+part.part+"\n")                                                        # let me know if the part is just being duplicated
                oldpart = bpy.data.objects[doneparts[part.partName]]                                            # have to select the object (2 step process)
                oldpart.select = True
                bpy.context.scene.objects.active = oldpart
                print(oldpart)
                bpy.ops.object.select_grouped(type = 'CHILDREN_RECURSIVE')                                      # select all children of the parent object (the empty), which deselects the parent
                bpy.data.objects[doneparts[part.partName]].select = True                                        # so reselect the parent
                
                bpy.ops.object.duplicate_move_linked()                                                          # duplicate the whole family
                copiedpart = oldpart.name + ".001"                                                             # the duplicate will be called something.001 always
                bpy.ops.object.select_all(action = 'DESELECT')                                                  # deselect everything
                newpart = bpy.data.objects[copiedpart]                                                          # and select just the parent (again, multi-step process)
                newpart.select = True
                bpy.context.scene.objects.active = newpart
                print(bpy.context.active_object)
                newpart.name = part.part                                                                        # rename it
                newpart.location = part.pos                                                                     # move it
                newpart.rotation_quaternion = part.rotQ                                                         # rotate it
                for obj in hiddenlist:                                                                          # hide all that annoying stuff again
                    obj.hide = True
        
        else:
            print("Failed to load "+part.partName+"... gotta fix that\n")                                   # if the part doesn't exist, let me know
        
        objlist = set([obj for obj in bpy.data.objects if obj not in doneobj])                              # find all the newly added objects
        doneobj = set(bpy.data.objects)                                                                     # done dealing with all the objects that are now in the scene (except for the ones I'm about to work with in objlist)
        
        if part.partName not in doneparts:                                                                  # if the part hasn't been imported before...
            doneparts[part.partName] = part.part                                                            # ...it has now
            
        for obj in objlist:                                                                                 # for all the unprocesses objects
            print(obj.name)                                                                                     # let me know which one we're on
            if obj.type == 'EMPTY':                                                                             # if it's an Empty object
                if obj.parent != None:                                                                              # if the Empty is not top-level
                    obj.hide = True                                                                                     # hide that shyet
                    print(obj.name + " Hidden\n")                                                                       # and tell me that they're gone
                else:                                                                                               # but if it is top level
                    obj.empty_draw_type = 'SPHERE'                                                                      # make that shyet a sphere
                    obj.empty_draw_size = 0                                                                             # a hella tiny sphere
            if obj.type == 'MESH':                                                                              # if it's a Mesh object
                scn.objects.active = obj                                                                            # make it active
                if "KSP" not in obj.name:
                    while len(obj.data.materials) > 0:
                        obj.data.materials.pop(0, update_data=True)
                        bpy.ops.object.material_slot_remove()
                bpy.ops.object.mode_set(mode='EDIT')                                                                # go into edit mode
                bpy.ops.mesh.remove_doubles(threshold = 0.0001)                                                     # remove double vertices
                bpy.ops.mesh.normals_make_consistent(inside = False)                                                # fix normals
                bpy.ops.object.mode_set(mode='OBJECT')                                                              # leave edit mode
                if len(obj.data.polygons) == 0:                                                                     # and if it's one of them stupid fake meshes with no faces
                    obj.hide = True                                                                                 # gtfo
                    
                maxrad = math.sqrt((obj.dimensions[0]/2)**2 + (obj.dimensions[1]/2)**2 + (obj.dimensions[2]/2)**2)  # find the radius of the parent Empty such that it encloses the object
                root = obj
                while root.parent != None:                                                                          # need to navigate to the uppermost parent
                    root = root.parent                                                                                  # and I can do it by jumping from child to parent until there is no parent
                if root.empty_draw_size < maxrad:                                                                   # make the empty big enough to enclose the biggest mesh found
                    root.empty_draw_size = maxrad                                                                       # and only update it if it's increasing in size (starts at 0, so it definitely should)
                
            if "coll" in obj.name or "COL" in obj.name or "fair" in obj.name and 'KSP' not in obj.name:         # if it is named anything to do with collider, I'll have none of it
                obj.hide = True                                                                                     # gtfo
                obj.hide_render = True                                                                              # really gtfo (don't even render)
                #object.select = True                                                                               # and if I'm really mad
                #bpy.ops.object.delete()                                                                            # I could just delete it
                if obj.type != 'EMPTY':                                                                             # and if it is a mesh (the empties have already been hidden, so this is a double-tap on them)...
                    print(obj.name + " Hidden\n")                                                                       # ...let me know

    bpy.ops.object.select_all(action = 'DESELECT')
    print("\n----------------------------------------------------\n") 

        
def fairing_fixer(partslist):
    """Unhides fairings if there is a part connected to the bottom of the engine"""
    for part in partslist:
        if partdir[part.partName][1] == "engine":
            for attN in part.attNlist:
                if attN.loc == "bottom":
                    root = bpy.data.objects[part.part]
                    queue = [child for child in root.children]
                    while len(queue) > 0:
                        current = queue.pop(0)
                        if "fair" in current.name:
                            current.hide = False
                            current.hide_render = False
                        for child in current.children:
                            queue.append(child)
                    
                    
    
def run():
    """runs"""
    mycraft = kspcraft('Kerbal 2X.craft')
    print("\n")
    print("         A          ")
    print("        / \\        ")
    print("       | 0 |        ")
    print("       |___|        ")
    print("       |___|        ")
    print("       |KSP|        ")
    print("      /|   |\\      ")
    print("     /| \\_/ |\\    ")
    print("    /_|  W  |_\\    ")
    print("       @WWW@        ")
    print("     @@WWWWW@@      ")
    print("    @ @@@@ @@@ @    ")
    print("  @   @  @@  @   @  ")
    print("\n")
    
    print(mycraft.ship + ' ready for takeoff\n')
    print(str(mycraft.num_parts()) + ' parts found...')
    
    import_parts(mycraft.partslist,kspexedirectory)
    fairing_fixer(mycraft.partslist)
    return mycraft

mycraft = run()