#!/usr/bin/python

from kpart import *

# These will probably need to live in a central file of their own & be imported into these parts files
BDB              = KMod("Bluedog DB")
ChakaMonkey      = KMod("Chaka Monkey")
FASA             = KMod("FASA")
KWRocketry       = KMod("KW Rocketry")
RealEngines      = KMod("RealEngines")
RNUSRockets      = KMod("RN US Rockets")
RO_Extended      = KMod("RO-Extended")
RSB              = KMod("Real Scale Boosters")
StockRO          = KMod("Stock (RO Config)")
SSTU             = KMod("SSTU")
SSTU_RO_Addition = KMod("SSTU (RO Addition)")
SXT              = KMod("SXT")
Taerobee         = KMod("Taerobee")
VSR              = KMod("Ven Stock Revamp")

# The same might go for these tags
LqdTurbo = KTag("ModuleTagEngineLiquidTurbo")
LqdPF    = KTag("ModuleTagEngineLiquidPF")
Toxic    = KTag("ModuleTagToxic")

### Category "Orbital Rocketry"

Orbital = KCat("Orbital Rocketry")

## Declare techs for category
# These four are also used for category RCS, so we'll want to share them
rocketryTesting     = KTech("rocketryTesting",      1945) # Post War
Orbital.add_tech(rocketryTesting)
earlyRocketry       = KTech("earlyRocketry",        1950)
Orbital.add_tech(earlyRocketry)
basicRocketryRP0    = KTech("basicRocketryRP0",     1952)
Orbital.add_tech(basicRocketryRP0)
orbitalRocketry1956 = KTech("orbitalRocketry1956",  1956)
Orbital.add_tech(orbitalRocketry1956)

for year in [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1970, 1972, 1976, 1981, 1986, 1992, 1998, 2004, 2009, 2014]:
    Orbital.add_tech(KTech("orbitalRocketry%d" % (year,), year))
Orbital.add_tech(KTech("orbitalRocketryNF",         2019))
Orbital.add_tech(KTech("colonization2051Orbital",   2051))
Orbital.add_tech(KTech("colonization2100Orbital",   2100))
Orbital.add_tech(KTech("colonization2150Orbital",   2150))

## Parts for category "Orbital Rocketry" begin here

# A-4
A4Config = EngineConfig("A-4", 0, 1, year=0, category=Orbital)
A9Config = EngineConfig("A-9", 550, (20000, 'HydyneFuel'), year=1945, category=Orbital, description="Derivate of the A-4/V-2 engine for use with the A-9 upper stage / spaceplane. Fuel mixture is speculative.")
Bumper_Engine = KPart("Bumper_Engine", "A-4", "Thiel Lox/Alcohol rocket engine. Used on V-2 missile. Work began June 1936. Interim design, but went into production. Used 18 x 1.5 tonne thrust chambers, feeding common mixing chamber. Tested from 1939, mass production 1943-1945. Diameter: [0.76 m]. Plume configured by RealPlume.",
                150, 1,
                mod=Taerobee, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[A4Config, A9Config],
                ecms=['A-4'], tags=[LqdTurbo])
Bumper_Engine_Unclad = Bumper_Engine.clone("Bumper_Engine_Unclad")

# A-6/Redstone
A6Config = EngineConfig("A-6", 0, (3000, 'Navaho-PhaseIII-TP'), year=1952, category=Orbital, description="The production version of the NAA75-110 engine as used on Redstone and the Mercury-Redstone Launch Vehicle.")
A7Config = EngineConfig("A-7", 200, (5000, 'HydyneFuel'), year=1956, category=Orbital, description="NAA75-110 using Hydyne fuel for increased thrust and specific impulse. Used on the Redstone-derivative Jupiter-C sounding rocket and Juno I launch vehicle.")
bluedog_redstone = KPart("bluedog_redstone", "NAA-75-110 A-Series", "Used on the Redstone missile.  Designed for Ethanol/LOx (A-6) (1.5 O/F Ratio), it was later adapted to burn Hydyne/LOx (A-7) (1.73 O/F Ratio)(higher performance (12%) yet more toxic) for use in Jupiter C / Juno I.  When Redstone MRLV was adapted from Jupiter C for manned use the A7 was switched back to Ethanol, accepting slightly lower performance for lack of toxicity. Thrust Vector Control was provided by carbon thrust vanes (add the Redstone Fin / Thrust vane part in 4x symmetry), and additional attitude control was provided by actuating fins. Mass includes thrust frame. Diameter: [1.77 m]. Plume configured by RealPlume.",
                400, 16000,
                mod=BDB, year=1952, category=Orbital,
                is_conf=RP0Conf, engine_configs=[A6Config, A7Config],
                ecms=['A-6'], tags=[LqdTurbo])
FASA_Mercury_Redstone_Eng = bluedog_redstone.clone("FASA_Mercury_Redstone_Eng", mod=FASA, year=1955)
# not an engine, but still in class Orbital for some reason
FASAMercuryRedstoneFin = KPart("FASAMercuryRedstoneFin", "A-7 Fin / Thrust Vane", "The Redstone / Jupiter-C / Juno engine could not gimbal.  Instead TVC was obtained by use of carbon thrust vanes. Apply in 4x symmetry to A7 engine unit.",
                5, 100,
                mod=FASA, year=1955, category=Orbital, is_conf=RP0Conf)

# Aerobee
WAC_Corporal = EngineConfig("WAC-Corporal", 0, 1, year=0, category=Orbital)
XASR1        = EngineConfig("XASR-1", 10, 1000, year=1945, category=Orbital)
AJ10_27      = EngineConfig("AJ10-27", 15, (2000, 'XASR-1'), year=1952, category=Orbital)
ROAerobeeSustainer = KPart("ROAerobeeSustainer", "Aerobee", "Small sustainer for WAC Corporal, Aerobee sounding rockets. Pressure-fed. Used after a small solid booster. Diameter: [0.3 m]. Plume configured by RealPlume.",
                30, 1,
                mod=StockRO, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[WAC_Corporal, XASR1, AJ10_27],
                ecms=['WAC-Corporal'], tags=[LqdPF])
taerobee_aerobee = ROAerobeeSustainer.clone("taerobee_aerobee",
                mod=Taerobee, year=1951)

# AJ10_Early
AJ10_37 = EngineConfig("AJ10-37", 0, (8000, 'AJ10-27'), year=1956, category=Orbital, description="Used on Vanguard second stage.")
AJ10_42 = EngineConfig("AJ10-42", -15, (2000, 'AJ10-37'), year=1958, category=Orbital, description="Used on Able I")
AJ10_101A = EngineConfig("AJ10-101A", 1, (1000, 'AJ10-42'), year=1959, category=Orbital, description="Used on Able II on Thor and Atlas.")
AJ10_142 = EngineConfig("AJ10-142", 1, (1500, 'AJ10-42'), year=1960, category=Orbital, description="Used on Thor-Delta")
AJ10_118 = EngineConfig("AJ10-118", -30, (1000, 'AJ10-142'), year=1962, category=Orbital, description="Used on Delta A")
AJ10_118D = EngineConfig("AJ10-118D", 10, (5000, 'AJ10-118'), year=1962, category=Orbital, description="Used on Delta B-D")
SXTAJ10 = KPart("SXTAJ10", "AJ10 Series (Early)", "Small pressure-fed hypergolic upper stage engine. Derivative of the first US liquid rocket engine, the AJ10 series is perhaps the longest-lived of any engine series, a part of the US's first satellite launch vehicle, Vanguard, the Apollo CSM, and even one projected Orion service module. This is the original Vanguard second stage / Able / Delta configuration, without restart capability. Plume configured by RealPlume.",
                150, 3000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_37, AJ10_42, AJ10_101A, AJ10_142, AJ10_118, AJ10_118D],
                ecms=['AJ10-37'], tags=[LqdPF, Toxic])
bluedog_ableEngine = SXTAJ10.clone("bluedog_ableEngine", mod=BDB)
SSTU_AJ10_CustomEarly = SXTAJ10.clone("SSTU-AJ10-CustomEarly", mod=SSTU_RO_Addition)
rn_aj10_37 = SXTAJ10.clone("rn_aj10_37", mod=RNUSRockets)
REP_AJ10_37 = SXTAJ10.clone("AJ10_37", mod=RealEngines)

SHIP_AJ_10_101_104 = KPart("SHIP_AJ_10_101_104", "AJ-10 101/104", "Flown on the Able, and AbleStar upper stages. Use the 10-101 with the Able upper stage, and the 10-104 with the AbleStar upper stage.",
                None, None,
                mod=RO_Extended, year=1959, category=Orbital,
                is_conf=ROConf, tags=[LqdPF, Toxic])

# AJ10_Mid
AJ10_104 = EngineConfig("AJ10-104", 0, (25000, 'AJ10-101A'), year=1960, category=Orbital, description="Used on Ablestar")
AJ10_118E = EngineConfig("AJ10-118E", -25, (5000, 'AJ10-104', 'AJ10-118D'), year=1965, category=Orbital, description="Used on Delta E-N")
SXTAJ10Mid = KPart("SXTAJ10Mid", "AJ10 Series (Mid)", "Small pressure-fed hypergolic upper stage engine. Derivative of the first US liquid rocket engine, the AJ10 series is perhaps the longest-lived of any engine series, a part of the US's first satellite launch vehicle, Vanguard, the Apollo CSM, and even one projected Orion service module. This represents mid-period AJ10s with a nozzle extension and restart capability. Used on Thor-Ablestar and Delta E through Delta N. Plume configured by RealPlume.",
                250, 5000,
                mod=SXT, year=1961, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_104, AJ10_118E],
                ecms=['AJ10-104'], tags=[LqdPF, Toxic])
bluedog_ablestarEngine = SXTAJ10Mid.clone("bluedog_ablestarEngine", mod=BDB)
SSTU_AJ10_CustomMid = SXTAJ10Mid.clone("SSTU-AJ10-CustomMid", mod=SSTU_RO_Addition)
rn_aj10_104 = SXTAJ10Mid.clone("rn_aj10_104", mod=RNUSRockets)
REP_AJ10_104 = SXTAJ10Mid.clone("AJ10_104", mod=RealEngines)

# AJ10_Adv
AJ10_138 = EngineConfig("AJ10-138", 0, 0, year=1964, category=Orbital, description="Used on Transtage")
AJ10_118F = EngineConfig("AJ10-118F", 50, 5000, year=1972, category=Orbital, description="Used on Delta 1000")
AJ10_118K = EngineConfig("AJ10-118K", 100, 15000, year=1989, category=Orbital, description="Used on Delta II")
SXTAJ10Adv = KPart("SXTAJ10Adv", "AJ10 Series (Advanced)", "Small pressure-fed hypergolic upper stage engine. Derivative of the first US liquid rocket engine, the AJ10 series is perhaps the longest-lived of any engine series, a part of the US's first satellite launch vehicle, Vanguard, the Apollo CSM, and even one projected Orion service module. This represents advanced era AJ10s with a nozzle extension and restart capability. Used on Transtage as AJ10-138; similar models but back with the -118 designation were used on the Delta F and Delta K upper stages. Plume configured by RealPlume.",
                300, 6000,
                mod=SXT, year=1964, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_104, AJ10_118E],
                ecms=['AJ10-118F'], tags=[LqdPF, Toxic])
bluedog_DeltaK_AJ10 = SXTAJ10Adv.clone("bluedog_DeltaK_AJ10", mod=BDB)
SSTU_AJ10_CustomAdvanced = SXTAJ10Adv.clone("SSTU-AJ10-CustomAdvanced", mod=SSTU_RO_Addition)

KW1mengineVestaVR1 = SXTAJ10Adv.clone("KW1mengineVestaVR1", mod=KWRocketry)
bluedog_Titan_TranstageEngine = SXTAJ10Adv.clone("bluedog_Titan_TranstageEngine", title="AJ10-138 (x2)", description="Originally developed for Vanguard and Able. Two used, thrust uprated from 3540 kgf to 3628 kgf, with higher specific impulse, in Transtage. Diameter: [1.53 m].",
                cost=600, mod=BDB,
                engine_configs=[AJ10_138], ecms=['AJ10-138'])

FASAGeminiLFECentarTwin = KPart("FASAGeminiLFECentarTwin", "AJ10-138", "This can be an upper stage / orbital taxi for various Titan III configurations. Uses 2x AJ10-138. Plume configured by RealPlume.",
                4300, 86000,
                mod=FASA, year=1964, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_138],
                ecms=['AJ10-138'], tags=[LqdPF, Toxic])

# AJ10-137
AJ10_137 = EngineConfig("AJ10-137", 0, 0, year=1968, category=Orbital, description="Used on the Apollo Service Module as the Service Propulsion System.")
ROAJ10_137 = KPart("ROAJ10-137", "AJ10-137 (Service Propulsion System)", "The Aerojet AJ10-137 rocket engine used on the Apollo Service Module as the Service Propulsion System. Diameter: [3.9 m]. Plume configured by RealPlume.",
                700, 24500,
                mod=StockRO, year=1968, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_137],
                ecms=['AJ10-137'], tags=[LqdPF, Toxic])
bluedog_Apollo_Block2_ServiceEngine = ROAJ10_137.clone("bluedog_Apollo_Block2_ServiceEngine", mod=BDB)
FASAApollo_SM_Engine = ROAJ10_137.clone("FASAApollo_SM_Engine", mod=FASA)
SSTU_SC_ENG_AJ10_137 = ROAJ10_137.clone("SSTU-SC-ENG-AJ10-137", mod=SSTU)
KW2mengineSPS = ROAJ10_137.clone("KW2mengineSPS", mod=KWRocketry)
REP_AJ10_137 = ROAJ10_137.clone("AJ10_137", mod=RealEngines)

'''
category Command is not defined - we should move this config to the Capsules
config file

SSTU_SC_B_SM = KPart("SSTU-SC-B-SM", "Apollo Service Module", "The Apollo Service Module. Contains fuel, RCS, ECS, fuel cell, and batteries. This has RCS pods built in.",
                10000, 350000,
                mod=SSTU, year=1968, category=Command,
                is_conf=RP0Conf, engine_configs=[AJ10_137],
                ecms=['AJ10-137'], tags=[LqdPF, Toxic])
'''

# AJ10-190
AJ10_190_OMS = EngineConfig("AJ10-190-OMS", 0, 0, year=1981, category=Orbital, description="Used as the Space Shuttle OMS")
AJ10_190_Orion = EngineConfig("AJ10-190-Orion", 0, 0, year=2023, category=Orbital, description="Used as the Orion SPS")
omsEngine = KPart("omsEngine", "AJ10-190", "Low thrust pressure-fed hypergolic engine. It was used on the Space Shuttle for orbital insertion, maneuvering and deorbiting. Currently used by the Orion MPCV. Diameter: [1.17 m]. Plume configured by RealPlume.",
                400, 8000,
                mod=StockRO, year=1981, category=Orbital,
                is_conf=RP0Conf, engine_configs=[AJ10_190_OMS, AJ10_190_Orion],
                ecms=['AJ10-190'], tags=[LqdPF, Toxic])
REP_AJ10_190 = omsEngine.clone("AJ10_190", mod=RealEngines)
SSTU_SC_ENG_AJ10_190 = omsEngine.clone("SSTU-SC-ENG-AJ10-190", mod=SSTU)
CHAKAOME2 = omsEngine.clone("CHAKAOME2", mod=ChakaMonkey)

# Gamma family (British HTP/kero, Black Arrow)
Gamma2Config = EngineConfig("Gamma-2", 0, (4000, 'GammaTP'), year=1956, category=Orbital)
SXTBlackAdder2 = KPart("SXTBlackAdder2", "Gamma 2", "A two chamber version of Gamma, used for the second stage of the Black Arrow satellite launch vehicle. As the only Gamma not required to operate at sea level, the nozzles were extended to allow better expansion. Diameter: [1.37 m]. Plume configured by RealPlume.",
                250, 4000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[Gamma2Config],
                ecms=['Gamma-2'], tags=[LqdTurbo])
Gamma8Config = EngineConfig("Gamma-8", 0, (5000, 'GammaTP'), year=1956, category=Orbital)
SXTBlackAdder = KPart("SXTBlackAdder", "Gamma 8", "This was an 8 chamber development of Gamma, used for the first stage of the Black Arrow satellite launch vehicle. Gamma thrust chambers were mounted in pairs radially, each pair on a one-axis tangential gimbal. Collective movement gave roll control, differential movement pitch. Diameter: [1.98 m]. Plume configured by RealPlume.",
                300, 10000,
                mod=SXT, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[Gamma8Config],
                ecms=['Gamma-8'], tags=[LqdTurbo])

# LR79 (Thor)
S3Config  = EngineConfig("S-3",         0, (10000, 'Navaho-TP'), year=1956, category=Orbital, description="Development version of the LR79 engine. Used on Thor R&D missiles.")
S3DConfig = EngineConfig("S-3D",        1, (2000, 'Navaho-TP-1958', 'S-3'),  year=1958, category=Orbital, description="Production version of the LR79 engine, used on Thor and Jupiter.")
LR79NA9   = EngineConfig("LR79-NA-9",  30, (2000, 'Navaho-TP-1959', 'S-3D'), year=1959, category=Orbital, description="MB-3-1 on Thor.")
LR79NA11  = EngineConfig("LR79-NA-11", 40, (2000, 'Navaho-TP-1960', 'LR79-NA-9'),  year=1960, category=Orbital, description="MB-3-2 on Thor.")
LR79NA13  = EngineConfig("LR79-NA-13", 50, (2000, 'Navaho-TP-1962', 'LR79-NA-11'), year=1963, category=Orbital, description="MB-3-3 on Thor.")
FASADeltaMB3LFE = KPart("FASADeltaMB3LFE", "LR79 Series", "Long-lasting US Kerolox gas-generator booster engine. The same components and broadly the same performance as the LR89, the LR79 (also known as S-3D in Jupiter / Juno II) powered Jupiter, Thor, and Thor-Delta (Delta) rockets. Diameter: [1.53 m]. Plume configured by RealPlume.",
                300, 13000,
                mod=FASA, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[S3Config, S3DConfig, LR79NA9, LR79NA11, LR79NA13],
                ecms=['S-3'], tags=[LqdTurbo])
liquidEngine1_2 = FASADeltaMB3LFE.clone("liquidEngine1-2", mod=StockRO)
bluedog_Juno_EngineS3D = FASADeltaMB3LFE.clone("bluedog_Juno_EngineS3D", title="S-3D Liquid Engine", mod=BDB)
bluedog_thorEngine = FASADeltaMB3LFE.clone("bluedog_thorEngine", title="Thor/Delta LR-79", mod=BDB)
SHIP_LR_71 = FASADeltaMB3LFE.clone("SHIP_LR_71", title="LR-79 Series", description="Engine used in a variety of launch vehicles, most notibly the Thor/Delta", mod=RO_Extended, year=1957)
rn_lr79 = FASADeltaMB3LFE.clone("rn_lr79", title="LR79/MB-3 Rocket Engine", description="A Lox/Kerosene rocket engine used on Thor-Able and early Delta launch vehicles. Plume configured by RealPlume.", mod=RNUSRockets, year=1958, engine_configs=[], ecms=['S-3D'])
rn_s3 = rn_lr79.clone("rn_s3", title="S-3", description="A Lox/Kerosene rocket engine used on Juno II and Saturn A-2. Plume configured by RealPlume.", ecms=[], not_identical=True) # XXX should this have S-3 ecm?

## LR79 Turbopump Exhaust.
rn_lr79_tp = KPart("rn_lr79_tp", "LR79/MB-3 Turbopump Exhaust Nozzle", "Turbopump exhaust for the Thor-Able/Delta launch vehicles. Plume configured by RealPlume.",
                5, 1000,
                mod=RNUSRockets, year=1958, category=Orbital,
                is_conf=RP0Conf,
                ecms=['S-3D'], tags=[LqdTurbo])
rn_s3_vernier = rn_lr79_tp.clone("rn_s3_vernier", title="S-3 Turbopump Exhaust Nozzle", description="A Lox/Kerosene vernier rocket engine used on the S-3 engine for Juno II and Saturn A-2. Plume configured by RealPlume.", cost=50, ecms=[], not_identical=True) # XXX should this have S-3 ecm?

# LR89 (Atlas booster)
LR43NA3  = EngineConfig("LR43-NA-3",    0, (12000, 'Navaho-TP'), year=1956, category=Orbital, description="First version of the LR89 booster for Atlas.")
LR89NA3  = EngineConfig("LR89-NA-3",    1, (2500, 'Navaho-TP-1958', 'LR43-NA-3'), year=1958, category=Orbital)
LR89NA5  = EngineConfig("LR89-NA-5",   15, (2500, 'Navaho-TP-1960', 'LR89-NA-3'), year=1960, category=Orbital)
LR89NA6  = EngineConfig("LR89-NA-6",   25, (2500, 'Navaho-TP-1962', 'LR89-NA-5'), year=1962, category=Orbital)
LR89NA71 = EngineConfig("LR89-NA-7.1", 40, (1000, 'MA-5-System',    'LR89-NA-6'), year=1965, category=Orbital)
LR89NA72 = EngineConfig("LR89-NA-7.2", 50, (1000, 'MA-5-System-I',  'LR89-NA-7.1'), year=1967, category=Orbital)
RS56OBA  = EngineConfig("RS-56-OBA",    8, (5000, 'H1-TP',          'LR89-NA-7.2'), year=1990, category=Orbital, description="Upgraded using H-1/RS-27 components.")
bluedog_Atlas_LR89 = KPart("bluedog_Atlas_LR89", "LR89 Series", "Kerolox gas-generator engine that served as booster for Atlas. Late model LR89s were upgraded with RS-27 components for higher efficiency. Very similar to LR79 (this was the pure-booster variant). Diameter: [1.0 m]. Plume configured by RealPlume.",
                300, 6000,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR43NA3, LR89NA3, LR89NA5, LR89NA6, LR89NA71, LR89NA72, RS56OBA],
                ecms=['LR43-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasEngBooster = bluedog_Atlas_LR89.clone("FASAMercuryAtlasEngBooster", mod=FASA)
RO_LR_89 = bluedog_Atlas_LR89.clone("RO-LR-89", mod=StockRO)

# LR101 (Atlas/Thor vernier)
LR101NA3  = EngineConfig("LR101-NA-3",  0, (8000, 'Navaho-PhaseIII-TP'), year=1956, category=Orbital)
LR101NA11 = EngineConfig("LR101-NA-11", 1, (1000, 'Navaho-TP-1960', 'LR101-NA-3'), year=1962, category=Orbital)
LR101NA15 = EngineConfig("LR101-NA-15",-5, (1000, 'RS27-System',    'LR101-NA-3'), year=1990, category=Orbital)
bluedog_Atlas_LR101_Radial = KPart("bluedog_Atlas_LR101_Radial", "LR101 Series", "Pump or pressure-fed kerolox vernier engine. Used for attitude control and final velocity adjustment in the MA-x system (2x LR89 + LR105 + 2x LR101) on Atlas, and MB-x system (LR79 or RS-27 + 2xLR101) on Thor-Able / Thor-Agena / Thor-Delta / Delta. Plume configured by RealPlume.",
                15, 1000,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR101NA3, LR101NA11, LR101NA15],
                ecms=['LR101-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasVernierEngine = bluedog_Atlas_LR101_Radial.clone("FASAMercuryAtlasVernierEngine", mod=FASA)
RSBengineLR101 = bluedog_Atlas_LR101_Radial.clone("RSBengineLR101", mod=RSB)
radialEngineMini = bluedog_Atlas_LR101_Radial.clone("radialEngineMini", mod=StockRO)
rn_lr79_vernier = bluedog_Atlas_LR101_Radial.clone("rn_lr79_vernier", title="LR101 Thor Vernier", description="Pump or pressure-fed kerolox vernier engine. Used for attitude control and final velocity adjustment in the MB-x system (LR79 or RS-27 + 2xLR101) on Thor-Able / Thor-Agena / Thor-Delta / Delta. Plume configured by RealPlume.", mod=RNUSRockets, year=1958)

# LR105 (Atlas sustainer)
LR43NA5   = EngineConfig("LR43-NA-5",     0, (15000, 'Navaho-TP'), year=1956, category=Orbital, description="First version of the LR105 sustainer for Atlas.")
LR105NA3  = EngineConfig("LR105-NA-3",    1, (3000, 'Navaho-TP-1958', 'LR43-NA-5'),  year=1958, category=Orbital)
LR105NA5  = EngineConfig("LR105-NA-5",   20, (3000, 'Navaho-TP-1960', 'LR105-NA-3'), year=1960, category=Orbital)
LR105NA6  = EngineConfig("LR105-NA-6",   35, (3000, 'Navaho-TP-1962', 'LR105-NA-5'), year=1962, category=Orbital)
LR105NA71 = EngineConfig("LR105-NA-7.1", 60, (1200, 'MA-5-System',    'LR105-NA-6'), year=1965, category=Orbital)
LR105NA72 = EngineConfig("LR105-NA-7.2", 80, (1200, 'MA-5-System-I',  'LR105-NA-7.1'), year=1967, category=Orbital)
RS56OSA   = EngineConfig("RS-56-OSA",    10, (6000, 'H1-TP',          'LR105-NA-7.2'), year=1990, category=Orbital, description="Upgraded using H-1/RS-27 components.")
bluedog_Atlas_LR105 = KPart("bluedog_Atlas_LR105", "LR105 Series", "Kerolox gas-generator sustainer engine used in the Atlas launch vehicle. It, like the Atlas's booster engines (LR89s) are lit on the ground, but after a bit over 2 minutes' flight the boosters are dropped and the Atlas core continues to orbit under the power of the sustainer engine (and the verniers for roll control and final adjustment). The final configuration of the LR105 (like the LR89) uses RS-27 components for increased performance. As a sustainer engine, the LR105 has relatively poor sea level specific impulse compared to most boosters, but somewhat better vacuum specific impulse--though the difference in both is nowhere near as pronounced as when comparing a booster to an upper stage engine. Diameter: [1.5 m]. Plume configured by RealPlume.",
                275, 5500,
                mod=BDB, year=1956, category=Orbital,
                is_conf=RP0Conf, engine_configs=[LR43NA5, LR105NA3, LR105NA5, LR105NA6, LR105NA71, LR105NA72, RS56OSA],
                ecms=['LR43-NA-3'], tags=[LqdTurbo])
FASAMercuryAtlasEng = bluedog_Atlas_LR105.clone("FASAMercuryAtlasEng", mod=FASA)
liquidEngine = bluedog_Atlas_LR105.clone("liquidEngine", mod=StockRO)

# RD-100 series
RD100Config = EngineConfig("RD-100", 0, 0, year=0, category=Orbital)
RD102 = EngineConfig("RD-102", 120, (10000, 'RD102-TP'), year=1950, category=Orbital)
RD103 = EngineConfig("RD-103", 300, (7000, 'RD-102', 'RD-103TP'), year=1952, category=Orbital)
RD103M = EngineConfig("RD-103M", 350, (5000, 'RD-103'), year=1956, category=Orbital)
rd100 = KPart("rd100", "RD-100 Series (Early)", "The RD-100 engine series were the first large scale Ethalox Russian liquid propellant rocket engines ever developed and fired. The original RD-100 engine was a 1:1 copy of the German Model 39 engine (used on the A-4 ballistic missile), with later variants (RD-101 and RD-103/M) featuring ever increasing performance to satisfy the needs of the larger R-2 and R-5 IRBMs. Diameter: 1.65 m. Plume configured by RealPlume.",
                150, 1,
                mod=RealEngines, year=0, category=Orbital,
                is_conf=RP0Conf, engine_configs=[RD100Config, RD102, RD103, RD103M],
                ecms=['RD-100'], tags=[LqdTurbo])
LVT15 = rd100.clone("LVT15", mod=VSR)

# X-405
X_405 = EngineConfig("X-405", 0, (12000, 'Navaho-PhaseIII-TP'), year=1956, category=Orbital, description="Used on Vanguard first stage.")
X_405H = EngineConfig("X-405H", 100, (10000, 'PumpReignition', 'X-405'), year=1959, category=Orbital, description="Engine for proposed Vega stage for NASA Atlas-Vega LV. Superceded by Atlas-Agena once NASA became aware of the USAF's Agena stage.")
SXTX405 = KPart("SXTX405", "Vanguard X-405 (XLR50-GE-2)", "A very early kerolox gas generator booster engine used on the Vanguard launch vehicle. Diameter: 1.0 m. Plume configured by RealPlume.",
                400, 12000,
                mod=SXT, year=1957, category=Orbital,
                is_conf=RP0Conf, engine_configs=[X_405, X_405H],
                ecms=['X-405'], tags=[LqdTurbo])
bluedog_vanguardEngine = SXTX405.clone("bluedog_vanguardEngine", mod=BDB)
rn_x405 = SXTX405.clone("rn_x405", mod=RNUSRockets)

rn_x405_vernier = KPart("rn_x405_vernier", "Vanguard X-405 Turbopump Exhaust Jet", "First stage vernier engine used on the Vanguard launch vehicle. Plume configured by RealPlume.",
                25, 500,
                mod=RNUSRockets, year=1957, category=Orbital,
                is_conf=RP0Conf,
                ecms=['X-405'], tags=[LqdTurbo])

# Agena
XLR81_BA_5 = EngineConfig("XLR81-BA-5", 0, (12000, 'Navaho-PhaseIII-TP'), year=1959, category=Orbital, description="Agena A")
XLR81_BA_7 = EngineConfig("XLR81_BA_7", 100, (10000, 'PumpReignition', 'XLR81-BA-5'), year=1961, category=Orbital, description="Agena B")
XLR81_BA_11 = EngineConfig("XLR81-BA-11", 80, (20000, 'XLR81-BA-7'), year=1962, category=Orbital, description="Agena D")
XLR81_BA_13 = EngineConfig("XLR81-BA-13", 300, (50000, 'XLR11-BA-11'), year=1965, category=Orbital, description="Model 8247, Gemini ATV")
Model8096_39 = EngineConfig("Model8096-39", 300, 12000, year=1965, category=Orbital, description="Improved propellant (HDA)")
Model8096A = EngineConfig("Model8096A", 325, 25000, year=1967, category=Orbital, description="Higher expansion ratio nozzle")
Model8096L = EngineConfig("Model8096L", 350, 35000, year=1987, category=Orbital, description="Reusable Agena for STS")
RO_AgenaEngine = KPart("RO-AgenaEngine", "XLR81 (Agena) Vacuum Engine", "Gas-generator nitric acid/UDMH vacuum engine used on Agena. The XLR81 family was derived from the Bell Hustler Rocket Engine, which was developed for use on an air-to-surface missile. Early engines were nearly identical to the Hustler engine, while later variants offered new capabilities and improved performance. Engine restart was introduced on the Agena B's XLR81-BA-7 (Model 8081). The XLR81-BA-11 (Model 8096) used on Agena D used propellant sumps to eliminate the need for ullage thrust. The XLR81-BA-13 (Model 8247) powered the Gemini Agena Target Vehicle (a modified Agena D) and was rated for up to 14 restarts. Diameter: [0.9 m]. Plume configured by RealPlume.",
                200, 7000,
                mod=VSR, year=1959, category=Orbital,
                is_conf=RP0Conf, engine_configs=[XLR81_BA_5, XLR81_BA_7, XLR81_BA_11, XLR81_BA_13, Model8096_39, Model8096A, Model8096L],
                ecms=['XLR81-BA-5'], tags=[LqdTurbo, Toxic])
FASAAgena_Engine = RO_AgenaEngine.clone("FASAAgena_Engine", mod=FASA)
RSBengineXLR81 = RO_AgenaEngine.clone("RSBengineXLR81", mod=RSB)
SSTU_SC_ENG_LR81_8048 = RO_AgenaEngine.clone("SSTU-SC-ENG-LR81-8048", title="XLR81 Agena A/B Vacuum Engine", mod=SSTU, engine_configs=[XLR81_BA_5, XLR81_BA_7])
SSTU_SC_ENG_LR81_8096 = RO_AgenaEngine.clone("SSTU-SC-ENG-LR81-8096", title="XLR81 Agena D Vacuum Engine", mod=SSTU, engine_configs=[XLR81_BA_11, XLR81_BA_13, Model8096_39, Model8096A, Model8096L], not_identical=True)

'''
Agena SPS in unlocked in the RCS tech nodes so should be in the RCS config

AgenaSPS = EngineConfig("AgenaSPS", 0, 0, year=1959, category=Orbital, description="")
'''
