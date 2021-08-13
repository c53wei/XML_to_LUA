# based on ModelFactory by Manish Sreenivasa
import re
import xml.etree.ElementTree as ET

import tree_attributes


# import numpy as np
# from .getJointAxis import *
# from .getDeLevaModel import *
# from .write import *
# import csv
#
#
# def inertia(radii, length, mass):
#     I = np.array([[np.power(radii[0] * length, 2) * mass, 0., 0.],
#                   [0., np.power(radii[1] * length, 2) * mass, 0.],
#                   [0., 0., np.power(radii[2] * length, 2) * mass]])
#     return I
#
#
# class LuaModelWriter:
#     '''Lua Model Class'''
#
#     def __init__(self, directory, conf_dir, name):
#         self.file_save_location = directory
#
#         '''Read Anthropometry'''
#         with open(directory + '/Anthropometry.txt') as f:
#             self.Anthropometry = dict(filter(None, csv.reader(f)))
#         self.shoulderWidth = float(self.Anthropometry['ShoulderWidth'])
#         self.shoulderNeckOffset = float(self.Anthropometry['ShoulderNeckOffset'])
#         self.hipCenterWidth = float(self.Anthropometry['HipCenterWidth'])
#         self.height = float(self.Anthropometry['Height'])
#         self.weight = float(self.Anthropometry['Weight'])
#         self.footWidth = float(self.Anthropometry['FootWidth'])
#         self.heelZOffset = float(self.Anthropometry['HeelZOffset'])
#         self.heelXOffset = float(self.Anthropometry['HeelXOffset'])
#         self.gender = self.Anthropometry['Gender']
#         self.AnkleHeight = self.Anthropometry['AnkleHeight']
#         self.KneeDist = float(self.Anthropometry['KneeDist'])
#         self.AnkleDist = float(self.Anthropometry['AnkleDist'])
#         self.ElbowDist = float(self.Anthropometry['ElbowDist'])
#         self.WristDist = float(self.Anthropometry['WristDist'])
#         self.AsisDist = float(self.Anthropometry['AsisDist'])
#         self.name = name
#         self.custom_segment = False
#
#         temp_dict = None
#         temp_dict_length = None
#         male = ("Male", "male", "0", "m", " Male", " male")
#
#         '''Read Model Joint Config'''
#         self.Segment_Prop = np.genfromtxt(conf_dir + '/modelDescription.txt',
#                                           names=True, delimiter=', ', dtype=None, usemask=True, encoding=None)
#
#         '''Read Mesh Visualization'''
#         self.Visuals = np.genfromtxt(conf_dir + '/Visuals.txt',
#                                      names=True, delimiter=', ', dtype=None, usemask=True, encoding=None)
#
#         '''Read Markers'''
#         self.Markers = np.genfromtxt(directory + 'Markers.txt',
#                                      names=True, delimiter=', ', dtype=None, usemask=True, encoding=None)
#
#         '''Read Segment Length if file exists, otherwise deLeva'''
#         self.Segment_Length = {}
#         try:
#             with open(directory + '/SegmentLengths.txt') as f:
#                 self.Segment_Length = {row[0]: float(row[1]) for row in csv.reader(f)}
#                 self.custom_segment = True
#         except FileNotFoundError:
#             self.custom_segment = False
#             if self.gender in ("Male", "male", "0", "m"):
#                 temp_dict = length_dict_m
#             else:
#                 temp_dict = length_dict_f
#             for k, v in temp_dict.items():
#                 self.Segment_Length[k] = v * self.height
#
#         '''Compute Segment masses'''
#         self.Segment_Mass = {}
#         new_mass = {}
#         total_mass = 0
#         test = 0
#         if self.gender in male:
#             temp_dict = mass_dict_m
#             temp_dict_length = length_dict_m
#         else:
#             temp_dict = mass_dict_f
#             temp_dict_length = length_dict_m
#
#         if self.custom_segment:
#             for k, v in temp_dict.items():
#                 new_mass[k] = v * self.weight / (temp_dict_length[k] * self.height) * self.Segment_Length[k]
#                 total_mass = total_mass + new_mass[k]
#             for k, v in new_mass.items():
#                 self.Segment_Mass[k] = v / total_mass * self.weight
#                 test = test + self.Segment_Mass[k]
#         else:
#             for k, v in temp_dict_mass.items():
#                 self.Segment_Mass[k] = v * self.weight
#
#         '''Compute Com Ratio'''
#         self.Segment_com_ratio = {}
#         if self.gender in male:
#             temp_dict = com_ratios_dict_m
#         else:
#             temp_dict = com_ratios_dict_f
#         for k, v in temp_dict.items():
#             self.Segment_com_ratio[k] = v * self.Segment_Length[k]
#
#         '''Compute Inertia'''
#         self.Segment_Inertia = {}
#         if self.gender in male:
#             temp_dict = rGyration_ratios_dict_m
#         else:
#             temp_dict = rGyration_ratios_dict_f
#         for k, v in temp_dict.items():
#             self.Segment_Inertia[k] = inertia(v[0], self.Segment_Length[k], self.Segment_Mass[k])
#
#         print("Model init done")
#
#     def getJointR(self, segment_name, parent_name):
#         j = np.zeros(3)
#         if segment_name in ('Pelvis'):
#             j[:] = (0, 0, 0)
#         elif segment_name in ('MiddleTrunk', 'UpperTrunk', 'Head'):
#             j[:] = (0, 0, float(self.Segment_Length[parent_name]))
#         elif segment_name in ('Shank_R', 'Shank_L', 'LowerArm_R', 'LowerArm_L',
#                               'Foot_R', 'Foot_L', 'Hand_R', 'Hand_L'):
#             j[:] = (0, 0, -self.Segment_Length[parent_name])
#         elif segment_name in ('Thigh_R'):
#             j[:] = (0, -0.5 * self.hipCenterWidth, 0)
#         elif segment_name in ('Thigh_L'):
#             j[:] = (0, 0.5 * self.hipCenterWidth, 0)
#         elif segment_name in ('UpperArm_R'):
#             j[:] = (0, -self.shoulderWidth / 2, self.Segment_Length[parent_name]
#                     - self.shoulderNeckOffset)
#         elif segment_name in ('UpperArm_L'):
#             j[:] = (0, self.shoulderWidth / 2, self.Segment_Length[parent_name]
#                     - self.shoulderNeckOffset)
#         else:
#             j[:] = (0, 0, 0)
#         return np.reshape(j, (1, 3))
#
#     def writeMetaData(self, file):
#         '''write Meta Data'''
#         file.write('\n')
#         file.write('metadata = {')
#         file.write('\n  {scaling = "deLeva",')
#         file.write('\n  subject_age = {},'.format(1337))
#         file.write('\n  subject_height = {},'.format(self.height))
#         file.write('\n  subject_gender = {},'.format(self.gender))
#         file.write('\n  subject_weight = {},'.format(self.weight))
#         file.write('\n  subject_ankleHeight = {},'.format(self.AnkleHeight))
#         file.write('\n  subject_shoulderWidth = {},'.format(self.shoulderWidth))
#         file.write('\n  subject_hipCenterWidth = {},'.format(self.hipCenterWidth))
#         file.write('\n  subject_AsisDist = {} }},'.format(self.AsisDist))
#         file.write('\n},')
#
#     def writeAnimationSettings(self, file):
#         file.write('\n')
#         file.write('animation_settings = {')
#         file.write('  force_scale = 0.002,\n')
#         file.write('  torque_scale = 0.002,\n')
#         file.write('  force_color = {1., 1., 0.},\n')
#         file.write('  torque_color = {0., 1., 0.},\n')
#         file.write('  force_transparency = 0.0,\n')
#         file.write('  torque_transparency = 0.0,')
#         file.write('\n},')
#
#     def writePoints(self, file):
#         '''write Contact Points'''
#         file.write('\n')
#         file.write('points = {')
#         file.write('\n},')
#
#     def writeGlobalInformation(self, file):
#         '''Write global frame information'''
#         file.write('\n')
#         file.write('gravity = { 0, 0, -9.81,},\n')
#         file.write('configuration = {')
#         file.write('\n  axis_right = { 0, 1, 0,},')
#         file.write('\n     axis_up = { 0, 0, 1,},')
#         file.write('\n  axis_front = { 1, 0, 0,},')
#
#     def writeConstraintSets(self, file):
#         '''Write Constraint Sets information'''
#         file.write('\n')
#         file.write('\npoints = {')
#         file.write('\n},')
#
#     def writeMarkers(self, file, segment_name):
#         '''Write Marker Data to Segment'''
#         parse_num = lambda n: float(n.astype('U').replace(',', ''))
#         pos = np.zeros(3)
#         file.write('\n  markers = {')
#         for marker in self.Markers:
#             if marker['Body'].astype('U') == segment_name:
#                 name = marker['Name'].astype('U')
#                 file.write('\n    {} = '.format(name))
#                 pos[:] = (parse_num(marker['marker_x']),
#                           parse_num(marker['marker_y']),
#                           parse_num(marker['marker_z']))
#
#                 writeLuaMatrix(file, np.reshape(pos, (1, 3)), 0)
#
#         file.write('\n  },')
#
#     def writeMesh(self, file, segment_name):
#         '''Write Visual Data'''
#         parse_num = lambda n: float(n.astype('U').replace(',', ''))
#         dimension = np.zeros(3)
#         meshcenter = np.zeros(3)
#         color = np.zeros(3)
#         mesh = 'dummy.obj'
#
#         for visual in self.Visuals:
#             if visual['Body'].astype('U') == segment_name:
#                 color[:] = (parse_num(visual['color_r']),
#                             parse_num(visual['color_g']),
#                             parse_num(visual['color_b']))
#                 meshcenter[:] = (parse_num(visual['center_x'])
#                                  * self.Segment_Length[segment_name],
#                                  parse_num(visual['center_y'])
#                                  * self.Segment_Length[segment_name],
#                                  parse_num(visual['center_z'])
#                                  * self.Segment_Length[segment_name])
#                 dimension[:] = (parse_num(visual['size_x'])
#                                 * self.Segment_Length[segment_name],
#                                 parse_num(visual['size_y'])
#                                 * self.Segment_Length[segment_name],
#                                 parse_num(visual['size_z'].astype('U'))
#                                 * self.Segment_Length[segment_name])
#                 mesh = visual['Mesh'].astype('U')
#                 if segment_name in ('Pelvis', 'MiddleTrunk'):
#                     dimension[:] = (parse_num(visual['size_x'])
#                                     * self.AsisDist,
#                                     parse_num(visual['size_y'])
#                                     * self.AsisDist,
#                                     parse_num(visual['size_z'])
#                                     * self.Segment_Length[segment_name])
#                 if segment_name in ('Foot_R', 'Foot_L'):
#                     dimension[:] = (parse_num(visual['size_x'])
#                                     * self.Segment_Length[segment_name],
#                                     parse_num(visual['size_y'])
#                                     * self.footWidth,
#                                     parse_num(visual['size_z'])
#                                     * self.Segment_Length[segment_name])
#                     meshcenter[:] = (parse_num(visual['center_x'])
#                                      * self.Segment_Length[segment_name] / 2,
#                                      parse_num(visual['center_y'])
#                                      * self.Segment_Length[segment_name],
#                                      parse_num(visual['center_z'])
#                                      * self.Segment_Length[segment_name])
#                 if segment_name in ('UpperTrunk'):
#                     dimension[:] = (parse_num(visual['size_x'])
#                                     * self.AsisDist,
#                                     parse_num(visual['size_y'])
#                                     * self.shoulderWidth,
#                                     parse_num(visual['size_z'])
#                                     * self.Segment_Length[segment_name])
#
#         file.write('\n  visuals = {{')
#         file.write('\n    src  = "meshes/' + mesh + '",')
#         file.write('\n    dimensions  = ')
#         writeLuaMatrix(file, np.reshape(dimension, (1, 3)), 1)
#         file.write('\n    mesh_center = ')
#         writeLuaMatrix(file, np.reshape(meshcenter, (1, 3)), 1)
#         file.write('\n    color       = ')
#         writeLuaMatrix(file, np.reshape(color, (1, 3)), 1)
#         file.write('\n    },},')
#
#     def writeJointFrame(self, file, segment_name, parent_name):
#         '''write Joint Frame'''
#         file.write('\n  joint_frame = {')
#         file.write('\n    r = ')
#         writeLuaMatrix(file, self.getJointR(segment_name, parent_name), 1)
#         file.write('\n    E = \n')
#         writeLuaMatrix(file, np.eye(3, 3), 3)
#         file.write('\n  },')
#
#     def writeBodyInfo(self, file, segment_name):
#         file.write('\n  body = {')
#         file.write('\n    mass = {},'.format(self.Segment_Mass[segment_name]))
#         file.write('\n    com = ')
#         writeLuaMatrix(file, self.Segment_com_ratio[segment_name], 1)
#         file.write('\n    inertia = \n')
#         writeLuaMatrix(file, self.Segment_Inertia[segment_name], 3)
#         file.write('\n  },')
#
#     def writeJointInfo(self, file, joint_type):
#         file.write('\n  joint  =\n')
#         joint = joint_dict[joint_type]
#         if np.shape(joint)[0] == 1:
#             file.write('    {')
#             writeLuaMatrix(file, joint, 0)
#             file.write('}')
#         else:
#             writeLuaMatrix(file, joint, 2)
#
#     def writeFrame(self, file, segment):
#         '''Write one entire frame'''
#         segment_name = segment['Body'].astype('U')
#         parent_name = segment['Parent'].astype('U')
#         joint_type = segment['Joint'].astype('U')
#         file.write('\n  {')
#         file.write('\n  name   = "' + segment_name + '",')
#         file.write('\n  parent = "' + parent_name + '",')
#         self.writeMesh(file, segment_name)
#         self.writeJointFrame(file, segment_name, parent_name)
#         self.writeBodyInfo(file, segment_name)
#         self.writeMarkers(file, segment_name)
#         self.writeJointInfo(file, joint_type)
#         file.write('\n  },')
#
#     def writeFrames(self, file):
#         '''wirte all Frames'''
#         file.write('\n')
#         file.write('frames = {')
#         for segment in self.Segment_Prop:
#             self.writeFrame(file, segment)
#         file.write('\n},')
#
#     def save(self):
#         file = open(self.file_save_location + '/' + self.name + '_deLeva_reduced.lua', 'w')
#         file.write('return {')
#         self.writeMetaData(file)
#         self.writeGlobalInformation(file)
#         self.writeAnimationSettings(file)
#         self.writePoints(file)
#         self.writeFrames(file)
#         file.write('\n}')
#         file.close()


#  Temporary write functions
def print_tree(root: ET.Element):
    for child in root.iter("Segment"):
        print(f'{child.get("NAME")}\t{child.get("body")}\t{child.get("joint_frame")}\t{child.get("markers")}')


# the simplest, lambda-based implementation
def multiple_replace(adict: {}, text: str):
    # Create a regular expression from all of the dictionary keys
    regex = re.compile("|".join(map(re.escape, adict.keys())))

    # For each match, look up the corresponding value in the dictionary
    return regex.sub(lambda match: adict[match.group(0)], text)


def regex_format(filename: str):
    # Read in the file
    with open(filename, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = multiple_replace({'[': '{', ']': '}', ':': ' =', '\'': ''}, filedata)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)


def write_segment(file, test_child: ET.Element):
    keys = ['name', 'parent', 'joint_frame', 'body', 'markers', 'joint']
    values = [f'"{test_child.get("NAME")}"', f'"{tree_attributes.get_parent(test_child).get("NAME")}"',
              test_child.get('joint_frame'), test_child.get('body'),
              dict.__repr__(test_child.get('markers')), test_child.get('joint')]
    formatted_dict = dict(zip(keys, values))
    for key, value in formatted_dict.items():
        file.write('%s : %s,\n' % (key, value))