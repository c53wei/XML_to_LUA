# based on ModelFactory by Manish Sreenivasa

import numpy as np

mass_dict_m = {"Pelvis":  0.1117,
               "Thigh_R": 0.1416,
               "Thigh_L": 0.1416,
               "Shank_R": 0.0433,
               "Shank_L": 0.0433,
               "Foot_R":  0.0137,
               "Foot_L":  0.0137,
               "MiddleTorso": 0.1633,
               "UpperTorso": 0.1596,
               "UpperArm_R": 0.0271,
               "UpperArm_L": 0.0271,
               "LowerArm_R": 0.0162,
               "LowerArm_L": 0.0162,
               "Hand_R": 0.0061,
               "Hand_L": 0.0061,
               "Head": 0.0694,
}

mass_dict_f = {"Pelvis":  0.1247,
               "Thigh_R": 0.1478,
               "Thigh_L": 0.1478,
               "Shank_R": 0.0481,
               "Shank_L": 0.0481,
               "Foot_R":  0.0129,
               "Foot_L":  0.0129,
               "MiddleTorso": 0.1465,
               "UpperTorso": 0.1545,
               "UpperArm_R": 0.0255,
               "UpperArm_L": 0.0255,
               "LowerArm_R": 0.0138,
               "LowerArm_L": 0.0138,
               "Hand_R": 0.0056,
               "Hand_L": 0.0056,
               "Head": 0.0669,
}

length_dict_m = {"Pelvis":  0.1457 / 1.741,
               "Thigh_R": 0.4222 / 1.741,
               "Thigh_L": 0.4222 / 1.741,
               "Shank_R": 0.4403 / 1.741,
               "Shank_L": 0.4403 / 1.741,
               "Foot_R":  0.2581 / 1.741,
               "Foot_L":  0.2581 / 1.741,
               "MiddleTorso": 0.2155 / 1.741,
               "UpperTorso": 0.2421 / 1.741,
               "UpperArm_R": 0.2817 / 1.741,
               "UpperArm_L": 0.2817 / 1.741,
               "LowerArm_R": 0.2689 / 1.741,
               "LowerArm_L": 0.2689 / 1.741,
               "Hand_R": 0.1879 / 1.741,
               "Hand_L": 0.1879 / 1.741,
               "Head": 0.2429 / 1.741,
}

length_dict_f = {"Pelvis":  0.1815 / 1.735,
               "Thigh_R": 0.3685 / 1.735,
               "Thigh_L": 0.3685 / 1.735,
               "Shank_R": 0.4386 / 1.735,
               "Shank_L": 0.4386 / 1.735,
               "Foot_R":  0.2283 / 1.735,
               "Foot_L":  0.2283 / 1.735,
               "MiddleTorso": 0.2053 / 1.735,
               "UpperTorso": 0.2280 / 1.735,
               "UpperArm_R": 0.2751 / 1.735,
               "UpperArm_L": 0.2751 / 1.735,
               "LowerArm_R": 0.2643 / 1.735,
               "LowerArm_L": 0.2643 / 1.735,
               "Hand_R": 0.1701 / 1.735,
               "Hand_L": 0.1701 / 1.735,
               "Head": 0.2437 / 1.735,
}

com_ratios_dict_f = {'Pelvis': np.array([[0., 0.,  1-0.4920]]),    
                     'Thigh_R': np.array([[0., 0., -0.3612]]),     
                     'Thigh_L': np.array([[0., 0., -0.3612]]), 
                     'Shank_R': np.array([[0., 0., -0.4352]]),
                     'Shank_L': np.array([[0., 0., -0.4352]]),          
                     'Foot_R': np.array([[0.4014,  0., 0.]]),           
                     'Foot_L': np.array([[0.4014,  0., 0.]]), 
                     'MiddleTorso': np.array([[0., 0.,  1-0.4512]]),
                     'UpperTorso': np.array([[0., 0.,  1-0.5050]]),
                     'UpperArm_R': np.array([[0., 0., -0.5754]]), 
                     'UpperArm_L': np.array([[0., 0., -0.5754]]),
                     'LowerArm_R': np.array([[0., 0., -0.4559]]),
                     'LowerArm_L': np.array([[0., 0., -0.4559]]), 
                     'Hand_R': np.array([[0., 0., -0.3427]]),
                     'Hand_L': np.array([[0., 0., -0.3427]]),
                     'Head': np.array([[0., 0.,  1-0.4841]]),
}

com_ratios_dict_m = {'Pelvis': np.array([[0., 0.,  1-0.6115]]),    
                     'Thigh_R': np.array([[0., 0., -0.4095]]),     
                     'Thigh_L': np.array([[0., 0., -0.4095]]), 
                     'Shank_R': np.array([[0., 0., -0.4395]]),
                     'Shank_L': np.array([[0., 0., -0.4395]]),          
                     'Foot_R': np.array([[0.4415,  0., 0.]]),           
                     'Foot_L': np.array([[0.4415,  0., 0.]]), 
                     'MiddleTorso': np.array([[0., 0.,  1-0.4502]]),
                     'UpperTorso': np.array([[0., 0.,  1-0.5066]]),
                     'UpperArm_R': np.array([[0., 0., -0.5772]]), 
                     'UpperArm_L': np.array([[0., 0., -0.5772]]),
                     'LowerArm_R': np.array([[0., 0., -0.4574]]),
                     'LowerArm_L': np.array([[0., 0., -0.4574]]), 
                     'Hand_R': np.array([[0., 0., -0.3624]]),
                     'Hand_L': np.array([[0., 0., -0.3624]]),
                     'Head': np.array([[0., 0.,  1-0.5002]]),
}

rGyration_ratios_dict_f = {'Pelvis': np.array([[0.433, 0.402, 0.444]]),    
                     'Thigh_R': np.array([[0.369, 0.364, 0.162]]),     
                     'Thigh_L': np.array([[0.369, 0.364, 0.162]]), 
                     'Shank_R': np.array([[0.267, 0.263, 0.092]]),
                     'Shank_L': np.array([[0.267, 0.263, 0.092]]),          
                     'Foot_R': np.array([[0.299, 0.279, 0.139]]),           
                     'Foot_L': np.array([[0.299, 0.279, 0.139]]), 
                     'MiddleTorso': np.array([[0.433, 0.354, 0.415]]),
                     'UpperTorso': np.array([[0.466, 0.314, 0.449]]),
                     'UpperArm_R': np.array([[0.278, 0.260, 0.148]]), 
                     'UpperArm_L': np.array([[0.278, 0.260, 0.148]]),
                     'LowerArm_R': np.array([[0.261, 0.257, 0.094]]),
                     'LowerArm_L': np.array([[0.261, 0.257, 0.094]]), 
                     'Hand_R': np.array([[0.244, 0.208, 0.154]]),
                     'Hand_L': np.array([[0.244, 0.208, 0.154]]),
                     'Head': np.array([[0.271, 0.295, 0.261]]),
}

rGyration_ratios_dict_m = {'Pelvis': np.array([[0.615, 0.551, 0.587]]),    
                     'Thigh_R': np.array([[0.329, 0.329, 0.149]]),     
                     'Thigh_L': np.array([[0.329, 0.329, 0.149]]), 
                     'Shank_R': np.array([[0.251, 0.246, 0.102]]),
                     'Shank_L': np.array([[0.251, 0.246, 0.102]]),          
                     'Foot_R': np.array([[0.257, 0.245, 0.124]]),           
                     'Foot_L': np.array([[0.257, 0.245, 0.124]]), 
                     'MiddleTorso': np.array([[0.482, 0.383, 0.468]]),
                     'UpperTorso': np.array([[0.505, 0.320, 0.465]]),
                     'UpperArm_R': np.array([[0.285, 0.269, 0.158]]), 
                     'UpperArm_L': np.array([[0.285, 0.269, 0.158]]),
                     'LowerArm_R': np.array([[0.276, 0.265, 0.121]]),
                     'LowerArm_L': np.array([[0.276, 0.265, 0.121]]), 
                     'Hand_R': np.array([[0.288, 0.235, 0.184]]),
                     'Hand_L': np.array([[0.288, 0.235, 0.184]]),
                     'Head': np.array([[0.303, 0.315, 0.261]]),
}


def calc_inertia(radii, length, mass):
    I = np.array([[np.power(radii[0] * length, 2) * mass, 0., 0.],
                  [0., np.power(radii[1] * length, 2) * mass, 0.],
                  [0., 0., np.power(radii[2] * length, 2) * mass]])
    return I


def calc_anthro(body_part: str, segment_length: float, male: bool=True, body_mass: float=65) -> ():

    body_part = body_part.lower()
    if male:
        mass_dict = dict((k.lower(), v) for k, v in mass_dict_m .items())
        com_dict = dict((k.lower(), v) for k, v in com_ratios_dict_m .items())
        r_gyration_dict = dict((k.lower(), v) for k, v in rGyration_ratios_dict_m .items())
    else:
        mass_dict = dict((k.lower(), v) for k, v in mass_dict_f .items())
        com_dict = dict((k.lower(), v) for k, v in com_ratios_dict_f .items())
        r_gyration_dict = dict((k.lower(), v) for k, v in rGyration_ratios_dict_f .items())

    try:
        mass = mass_dict.get(body_part, 0) * body_mass
        com = com_dict.get(body_part, 0) * segment_length
        com = com.tolist()[0]
        inertia = calc_inertia(r_gyration_dict.get(body_part)[0], segment_length, mass).tolist()
    except TypeError:
        mass = 0
        com = 0
        inertia = 0

    return mass, com, inertia


