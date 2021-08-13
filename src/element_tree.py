import xml.etree.ElementTree as ET
import tree_attributes

from markers import link_segment_to_marker
from write_lua import print_tree, write_segment, regex_format


def write_metadata(file):
        '''write Meta Data'''

        temp_data = 0.0
        file.write('\n')
        file.write('metadata = {')
        file.write('\n  {scaling = "deLeva",')
        file.write('\n  subject_age = {},'.format(1337))
        file.write('\n  subject_height = {},'.format(temp_data))
        file.write('\n  subject_gender = {},'.format(temp_data))
        file.write('\n  subject_weight = {},'.format(temp_data))
        file.write('\n  subject_ankleHeight = {},'.format(temp_data))
        file.write('\n  subject_shoulderWidth = {},'.format(temp_data))
        file.write('\n  subject_hipCenterWidth = {},'.format(temp_data))
        file.write('\n  subject_AsisDist = {} }},'.format(temp_data))
        file.write('\n},')


def write_global_information(file):
    '''Write global frame information'''
    file.write('\n')
    file.write('gravity = { 0, 0, -9.81,},\n')
    file.write('configuration = {')
    file.write('\n  axis_right = { 0, 1, 0,},')
    file.write('\n     axis_up = { 0, 0, 1,},')
    file.write('\n  axis_front = { 1, 0, 0,},')


def write_animation_settings(file):
    file.write('\n')
    file.write('animation_settings = {')
    file.write('  force_scale = 0.002,\n')
    file.write('  torque_scale = 0.002,\n')
    file.write('  force_color = {1., 1., 0.},\n')
    file.write('  torque_color = {0., 1., 0.},\n')
    file.write('  force_transparency = 0.0,\n')
    file.write('  torque_transparency = 0.0,')
    file.write('\n},')


def write_points(file):
    '''write Contact Points'''
    file.write('\n')
    file.write('points = {')
    file.write('\n},')


tree = ET.parse('../data/mIOR.vsk')
root = tree.getroot()
# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(root)
segment_marker_data = link_segment_to_marker(root)
tree_attributes.add_position_info(root, segment_marker_data)

# print_tree(root)
# 
# test_child = root.findall('.//Segment')[1]
# with open('../data/test.lua', 'w') as file:
#     file.write('return\n')
#     for child in root.iter('Segment'):
#         file.write('{\n')
#         write_segment(file, child)
#         file.write('},\n')
#     file.write('}')
# regex_format('../data/test.lua')

file = open('../data/test_2.lua', 'w')
file.write('return {')
write_metadata(file)
write_global_information(file)
write_animation_settings(file)
write_points(file)
# self.writeFrames(file)
file.write('\n}')
file.close()