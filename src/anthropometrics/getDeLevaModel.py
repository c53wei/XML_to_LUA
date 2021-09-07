# based on ModelFactory by Manish Sreenivasa

import numpy as np

mass_dict_m = {"Pelvis": 0.1117,
               "R_Thigh": 0.1416,
               "L_Thigh": 0.1416,
               "R_Shank": 0.0433,
               "L_Shank": 0.0433,
               "R_Foot": 0.0137,
               "L_Foot": 0.0137,
               "MiddleTrunk": 0.1633,
               "UpperTrunk": 0.1596,
               "R_UpperArm": 0.0271,
               "L_UpperArm": 0.0271,
               "R_Forearm": 0.0162,
               "L_Forearm": 0.0162,
               "R_Hand": 0.0061,
               "L_Hand": 0.0061,
               "Head": 0.0694,
               }

mass_dict_f = {"Pelvis": 0.1247,
               "R_Thigh": 0.1478,
               "L_Thigh": 0.1478,
               "R_Shank": 0.0481,
               "L_Shank": 0.0481,
               "R_Foot": 0.0129,
               "L_Foot": 0.0129,
               "MiddleTrunk": 0.1465,
               "UpperTrunk": 0.1545,
               "R_UpperArm": 0.0255,
               "L_UpperArm": 0.0255,
               "R_Forearm": 0.0138,
               "L_Forearm": 0.0138,
               "R_Hand": 0.0056,
               "L_Hand": 0.0056,
               "Head": 0.0669,
               }

length_dict_m = {"Pelvis": 0.1457 / 1.741,
                 "R_Thigh": 0.4222 / 1.741,
                 "L_Thigh": 0.4222 / 1.741,
                 "R_Shank": 0.4403 / 1.741,
                 "L_Shank": 0.4403 / 1.741,
                 "R_Foot": 0.2581 / 1.741,
                 "L_Foot": 0.2581 / 1.741,
                 "MiddleTrunk": 0.2155 / 1.741,
                 "UpperTrunk": 0.2421 / 1.741,
                 "R_UpperArm": 0.2817 / 1.741,
                 "L_UpperArm": 0.2817 / 1.741,
                 "R_Forearm": 0.2689 / 1.741,
                 "L_Forearm": 0.2689 / 1.741,
                 "R_Hand": 0.1879 / 1.741,
                 "L_Hand": 0.1879 / 1.741,
                 "Head": 0.2429 / 1.741,
                 }

length_dict_f = {"Pelvis": 0.1815 / 1.735,
                 "R_Thigh": 0.3685 / 1.735,
                 "L_Thigh": 0.3685 / 1.735,
                 "R_Shank": 0.4386 / 1.735,
                 "L_Shank": 0.4386 / 1.735,
                 "R_Foot": 0.2283 / 1.735,
                 "L_Foot": 0.2283 / 1.735,
                 "MiddleTrunk": 0.2053 / 1.735,
                 "UpperTrunk": 0.2280 / 1.735,
                 "R_UpperArm": 0.2751 / 1.735,
                 "L_UpperArm": 0.2751 / 1.735,
                 "R_Forearm": 0.2643 / 1.735,
                 "L_Forearm": 0.2643 / 1.735,
                 "R_Hand": 0.1701 / 1.735,
                 "L_Hand": 0.1701 / 1.735,
                 "Head": 0.2437 / 1.735,
                 }

com_ratios_dict_f = {'Pelvis': np.array([[0., 0., 1 - 0.4920]]),
                     'R_Thigh': np.array([[0., 0., -0.3612]]),
                     'L_Thigh': np.array([[0., 0., -0.3612]]),
                     'R_Shank': np.array([[0., 0., -0.4352]]),
                     'L_Shank': np.array([[0., 0., -0.4352]]),
                     'R_Foot': np.array([[0.4014, 0., 0.]]),
                     'L_Foot': np.array([[0.4014, 0., 0.]]),
                     'MiddleTrunk': np.array([[0., 0., 1 - 0.4512]]),
                     'UpperTrunk': np.array([[0., 0., 1 - 0.5050]]),
                     'R_UpperArm': np.array([[0., 0., -0.5754]]),
                     'L_UpperArm': np.array([[0., 0., -0.5754]]),
                     'R_Forearm': np.array([[0., 0., -0.4559]]),
                     'L_Forearm': np.array([[0., 0., -0.4559]]),
                     'R_Hand': np.array([[0., 0., -0.3427]]),
                     'L_Hand': np.array([[0., 0., -0.3427]]),
                     'Head': np.array([[0., 0., 1 - 0.4841]]),
                     }

com_ratios_dict_m = {'Pelvis': np.array([[0., 0., 1 - 0.6115]]),
                     'R_Thigh': np.array([[0., 0., -0.4095]]),
                     'L_Thigh': np.array([[0., 0., -0.4095]]),
                     'R_Shank': np.array([[0., 0., -0.4395]]),
                     'L_Shank': np.array([[0., 0., -0.4395]]),
                     'R_Foot': np.array([[0.4415, 0., 0.]]),
                     'L_Foot': np.array([[0.4415, 0., 0.]]),
                     'MiddleTrunk': np.array([[0., 0., 1 - 0.4502]]),
                     'UpperTrunk': np.array([[0., 0., 1 - 0.5066]]),
                     'R_UpperArm': np.array([[0., 0., -0.5772]]),
                     'L_UpperArm': np.array([[0., 0., -0.5772]]),
                     'R_Forearm': np.array([[0., 0., -0.4574]]),
                     'L_Forearm': np.array([[0., 0., -0.4574]]),
                     'R_Hand': np.array([[0., 0., -0.3624]]),
                     'L_Hand': np.array([[0., 0., -0.3624]]),
                     'Head': np.array([[0., 0., 1 - 0.5002]]),
                     }

rGyration_ratios_dict_f = {'Pelvis': np.array([[0.433, 0.402, 0.444]]),
                           'R_Thigh': np.array([[0.369, 0.364, 0.162]]),
                           'L_Thigh': np.array([[0.369, 0.364, 0.162]]),
                           'R_Shank': np.array([[0.267, 0.263, 0.092]]),
                           'L_Shank': np.array([[0.267, 0.263, 0.092]]),
                           'R_Foot': np.array([[0.299, 0.279, 0.139]]),
                           'L_Foot': np.array([[0.299, 0.279, 0.139]]),
                           'MiddleTrunk': np.array([[0.433, 0.354, 0.415]]),
                           'UpperTrunk': np.array([[0.466, 0.314, 0.449]]),
                           'R_UpperArm': np.array([[0.278, 0.260, 0.148]]),
                           'L_UpperArm': np.array([[0.278, 0.260, 0.148]]),
                           'R_Forearm': np.array([[0.261, 0.257, 0.094]]),
                           'L_Forearm': np.array([[0.261, 0.257, 0.094]]),
                           'R_Hand': np.array([[0.244, 0.208, 0.154]]),
                           'L_Hand': np.array([[0.244, 0.208, 0.154]]),
                           'Head': np.array([[0.271, 0.295, 0.261]]),
                           }

rGyration_ratios_dict_m = {'Pelvis': np.array([[0.615, 0.551, 0.587]]),
                           'R_Thigh': np.array([[0.329, 0.329, 0.149]]),
                           'L_Thigh': np.array([[0.329, 0.329, 0.149]]),
                           'R_Shank': np.array([[0.251, 0.246, 0.102]]),
                           'L_Shank': np.array([[0.251, 0.246, 0.102]]),
                           'R_Foot': np.array([[0.257, 0.245, 0.124]]),
                           'L_Foot': np.array([[0.257, 0.245, 0.124]]),
                           'MiddleTrunk': np.array([[0.482, 0.383, 0.468]]),
                           'UpperTrunk': np.array([[0.505, 0.320, 0.465]]),
                           'R_UpperArm': np.array([[0.285, 0.269, 0.158]]),
                           'L_UpperArm': np.array([[0.285, 0.269, 0.158]]),
                           'R_Forearm': np.array([[0.276, 0.265, 0.121]]),
                           'L_Forearm': np.array([[0.276, 0.265, 0.121]]),
                           'R_Hand': np.array([[0.288, 0.235, 0.184]]),
                           'L_Hand': np.array([[0.288, 0.235, 0.184]]),
                           'Head': np.array([[0.303, 0.315, 0.261]]),
                           }


def calc_inertia(radii, length, mass):
    I = np.array([[np.power(radii[0] * length, 2) * mass, 0., 0.],
                  [0., np.power(radii[1] * length, 2) * mass, 0.],
                  [0., 0., np.power(radii[2] * length, 2) * mass]])
    return I


def calc_anthro(body_part: str, segment_length: float, female: bool = False, body_mass: float = 65) -> ():
    body_part = body_part.lower()
    # Normalize mass coefficient (male 73 kg, female 61.9 kg)
    if female:
        mass_dict = dict((k.lower(), v/61.9) for k, v in mass_dict_f.items())
        com_dict = dict((k.lower(), v) for k, v in com_ratios_dict_f.items())
        r_gyration_dict = dict((k.lower(), v) for k, v in rGyration_ratios_dict_f.items())
    else:
        mass_dict = dict((k.lower(), v/73.0) for k, v in mass_dict_m.items())
        com_dict = dict((k.lower(), v) for k, v in com_ratios_dict_m.items())
        r_gyration_dict = dict((k.lower(), v) for k, v in rGyration_ratios_dict_m.items())
    try:
        mass = mass_dict.get(body_part, 0) * body_mass
        com = com_dict.get(body_part, 0) * segment_length
        inertia = calc_inertia(r_gyration_dict.get(body_part)[0], segment_length, mass)
    except TypeError:
        mass = 0
        com = np.zeros([1, 3])
        inertia = np.zeros([3, 3])

    return mass, com, inertia
