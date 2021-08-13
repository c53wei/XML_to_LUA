# based on ModelFactory by Manish Sreenivasa
import re
import numpy as np
import xml.etree.ElementTree as ET

import tree_attributes


from visuals import visuals_dict

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

def writeMesh(file, segment: ET.Element):
    '''Write Visual Data'''

    segment_name = segment.get('NAME')
    segment_length = segment.get('length')
    segment_visual_dict = visuals_dict.get(segment_name)
    # TODO
    temp_asis_dist = 5.0
    temp_foot_width = 5.0
    temp_shoulder_width = 5.0

    # Work around as we are still missing some data for Shoulder & Hip segments
    if segment_visual_dict is not None:
        colour = np.array(segment_visual_dict.get('colour', [0.2, 0.7, 0.3]))
        dimension = segment_visual_dict.get('size') * segment_length
        meshcenter = segment_visual_dict.get('center') * segment_length
        mesh = segment_visual_dict.get('mesh')
        # Special considerations for certain body parts
        if segment_name in ('Pelvis', 'MiddleTrunk'):
            dimension = np.multiply(segment_visual_dict.get('size'), [temp_asis_dist, temp_asis_dist, segment_length ])
        elif segment_name.__contains__('Foot'):
            dimension = np.multiply(segment_visual_dict.get('size'), [segment_length, temp_foot_width, segment_length])
            meshcenter = np.multiply(segment_visual_dict.get('center'), [segment_length/2, segment_length, segment_length])
        elif segment_name in ('UpperTrunk'):
            dimension = np.multiply(segment_visual_dict.get('size'), [temp_asis_dist, temp_shoulder_width, segment_length])
    else:
        dimension = np.zeros(3)
        meshcenter = np.zeros(3)
        colour = np.zeros(3)
        mesh = 'dummy.obj'

    file.write('\n  visuals = {{')
    file.write('\n    src  = "meshes/' + mesh + '",')
    file.write('\n    dimensions  = ')
    writeLuaMatrix(file, np.reshape(dimension, (1, 3)), 1)
    file.write('\n    mesh_center = ')
    writeLuaMatrix(file, np.reshape(meshcenter, (1, 3)), 1)
    file.write('\n    color       = ')
    writeLuaMatrix(file, np.reshape(colour, (1, 3)), 1)
    file.write('\n    },},')


def writeLuaMatrix(file,matrix, tabnumber):
    N, M = matrix.shape
    if M > 0:
        for k in range(0,N):
            for n in range(0,tabnumber):
                file.write('  ')
            if k == 0 and N > 1:
                file.write('{{')
            else:
                file.write(' {')
            for j in range (0,M):
                file.write(' ' + str(matrix[k,j]) + ',')
            if k == N-1:
                if N > 1:
                    file.write('},},')
                else:
                    file.write('},')
            else:
                file.write('},\n')


def writeMarkers(self, file, segment_name):
    '''Write Marker Data to Segment'''
    parse_num = lambda n: float(n.astype('U').replace(',', ''))
    pos = np.zeros(3)
    file.write('\n  markers = {')
    for marker in self.Markers:
        if marker['Body'].astype('U') == segment_name:
            name = marker['Name'].astype('U')
            file.write('\n    {} = '.format(name))
            pos[:] = (parse_num(marker['marker_x']),
                      parse_num(marker['marker_y']),
                      parse_num(marker['marker_z']))

            writeLuaMatrix(file, np.reshape(pos, (1, 3)), 0)

    file.write('\n  },')





def writeJointFrame(self, file, segment_name, parent_name):
    '''write Joint Frame'''
    file.write('\n  joint_frame = {')
    file.write('\n    r = ')
    writeLuaMatrix(file, self.getJointR(segment_name, parent_name), 1)
    file.write('\n    E = \n')
    writeLuaMatrix(file, np.eye(3, 3), 3)
    file.write('\n  },')


def writeBodyInfo(self, file, segment_name):
    file.write('\n  body = {')
    file.write('\n    mass = {},'.format(self.Segment_Mass[segment_name]))
    file.write('\n    com = ')
    writeLuaMatrix(file, self.Segment_com_ratio[segment_name], 1)
    file.write('\n    inertia = \n')
    writeLuaMatrix(file, self.Segment_Inertia[segment_name], 3)
    file.write('\n  },')


def writeJointInfo(self, file, joint_type):
    file.write('\n  joint  =\n')
    joint = joint_dict[joint_type]
    if np.shape(joint)[0] == 1:
        file.write('    {')
        writeLuaMatrix(file, joint, 0)
        file.write('}')
    else:
        writeLuaMatrix(file, joint, 2)


def writeFrame(file, segment):
    '''Write one entire frame'''
    segment_name = segment.get("NAME")
    parent_name = tree_attributes.get_parent(segment).get("NAME")
    joint_type = segment['Joint'].astype('U')  # TODO
    file.write('\n  {')
    file.write('\n  name   = "' + segment_name + '",')
    file.write('\n  parent = "' + parent_name + '",')
    writeMesh(file, segment)
    self.writeJointFrame(file, segment_name, parent_name)
    self.writeBodyInfo(file, segment_name)
    self.writeMarkers(file, segment_name)
    self.writeJointInfo(file, joint_type)
    file.write('\n  },')


def writeFrames(file, root: ET.Element):
    '''write all Frames'''
    file.write('\n')
    file.write('frames = {')
    for segment in root.iter('Segment'):
        writeFrame(file, segment)
    file.write('\n},')


def write_lua(filepath: str, root : ET.Element):
    file = open(filepath, 'w')
    file.write('return {')
    write_metadata(file)
    write_global_information(file)
    write_animation_settings(file)
    write_points(file)
    writeFrames(file, root)
    file.write('\n}')
    file.close()


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