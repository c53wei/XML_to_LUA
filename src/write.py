# based on ModelFactory by Manish Sreenivasa
import numpy as np
import xml.etree.ElementTree as ET

import tree_attributes


from visuals import visuals_dict


def write_metadata(file, subject: {}):
    """
    Write metadata to output file
    """
    temp_data = 0.0
    file.write('\n')
    file.write('metadata = {')
    file.write('\n  {scaling = "deLeva",')
    file.write('\n  subject_age = {},'.format(subject.get('age')))
    file.write('\n  subject_height = {},'.format(subject.get('height')))
    file.write('\n  subject_sex = {},'.format(subject.get('sex')))
    file.write('\n  subject_mass = {},'.format(subject.get('weight')))
    file.write('\n  subject_shoulderWidth = {},'.format(subject.get('AC_Width_Average')))
    file.write('\n  subject_AsisDist = {} }},'.format(subject.get('ASIS_Width_Average')))
    file.write('\n},')


def write_global_information(file):
    """Write global frame information"""
    file.write('\n')
    file.write('gravity = { 0, 0, -9.81,},\n')
    file.write('configuration = {')
    file.write('\n  axis_right = { 0, 1, 0,},')
    file.write('\n  axis_up = { 0, 0, 1,},')
    file.write('\n  axis_front = { 1, 0, 0,},')


def write_lua_matrix(file, matrix, tabnumber):

    N, M = matrix.shape
    if M > 0:
        for k in range(0, N):
            for n in range(0, tabnumber):
                file.write('  ')
            if k == 0 and N > 1:
                file.write('{{')
            else:
                file.write(' {')
            for j in range(0, M):
                file.write(' ' + str(matrix[k, j]) + ',')
            if k == N-1:
                if N > 1:
                    file.write('},},')
                else:
                    file.write('},')
            else:
                file.write('},\n')
                

def write_mesh(file, segment: ET.Element, subject: {}):
    """Write Visual Data"""

    segment_name = segment.get('NAME')
    segment_length = segment.get('length')
    segment_visual_dict = visuals_dict.get(segment_name)
    # Convert mm to m
    asis_dist = float(subject.get('ASIS_Width_Average').split(' ')[0])/1000
    foot_width = float(subject.get('Foot_Width_Average').split(' ')[0])/1000
    shoulder_width = float(subject.get('AC_Width_Average').split(' ')[0])/1000

    # Work around as we are still missing some data for Shoulder & Hip segments
    if segment_visual_dict is not None:
        colour = np.array(segment_visual_dict.get('colour', [0.2, 0.7, 0.3]))
        dimension = segment_visual_dict.get('size') * segment_length
        meshcenter = segment_visual_dict.get('center') * segment_length
        mesh = segment_visual_dict.get('mesh')
        # Special considerations for certain body parts
        if segment_name in ('Pelvis', 'MiddleTrunk'):
            dimension = np.multiply(segment_visual_dict.get('size'),
                                    [asis_dist, asis_dist, segment_length])
        elif segment_name.__contains__('Foot'):
            dimension = np.multiply(segment_visual_dict.get('size'),
                                    [segment_length, foot_width, segment_length])
            meshcenter = np.multiply(segment_visual_dict.get('center'),
                                     [segment_length/2, segment_length, segment_length])
        elif segment_name == 'UpperTrunk':
            dimension = np.multiply(segment_visual_dict.get('size'),
                                    [asis_dist, shoulder_width, segment_length])
    else:
        dimension = np.zeros(3)
        meshcenter = np.zeros(3)
        colour = np.zeros(3)
        mesh = 'dummy.obj'

    file.write('\n  visuals = {{')
    file.write('\n    src  = "meshes/' + mesh + '",')
    file.write('\n    dimensions  = ')
    write_lua_matrix(file, np.reshape(dimension, (1, 3)), 1)
    file.write('\n    mesh_center = ')
    write_lua_matrix(file, np.reshape(meshcenter, (1, 3)), 1)
    file.write('\n    color       = ')
    write_lua_matrix(file, np.reshape(colour, (1, 3)), 1)
    file.write('\n    },},')


def write_joint_frame(file, segment: ET.Element):
    """Write Joint Frame"""
    file.write('\n  joint_frame = {')
    file.write('\n    r = ')
    write_lua_matrix(file, segment.get('joint_frame').get('r'), 1)
    file.write('\n    E = \n')
    write_lua_matrix(file, segment.get('joint_frame').get('E'), 3)
    file.write('\n  },')


def write_body_info(file, segment: ET.Element):
    file.write('\n  body = {')
    file.write('\n    mass = {},'.format(segment.attrib['body']['mass']))
    file.write('\n    com = ')
    write_lua_matrix(file, segment.attrib['body']['com'], 1)
    file.write('\n    inertia = \n')
    write_lua_matrix(file, segment.attrib['body']['inertia'], 3)
    file.write('\n  },')


def write_markers(file, segment: ET.Element):
    """Write marker data to segment"""
    file.write('\n  markers = {')
    segment_marker_dict = segment.attrib['markers']
    for marker_name, locations in segment_marker_dict.items():
        file.write('\n    {} = '.format(marker_name))
        pos = np.array([locations])
        write_lua_matrix(file, pos, 0)
    file.write('\n  },')


def write_joint_info(file, segment: ET.Element):
    file.write('\n  joint  =\n')
    joint = segment.get('joint')
    if np.shape(joint)[0] == 1:
        file.write('    {')
        write_lua_matrix(file, joint, 0)
        file.write('}')
    else:
        write_lua_matrix(file, joint, 2)


def write_frame(file, segment, subject):
    """Write an entire segment to file"""
    file.write('\n  {')
    file.write('\n  name   = "' + segment.get("NAME") + '",')
    file.write('\n  parent = "' + tree_attributes.get_parent(segment).get("NAME", 'ROOT') + '",')
    write_mesh(file, segment, subject)
    write_joint_frame(file, segment)
    write_body_info(file, segment)
    write_markers(file, segment)
    write_joint_info(file, segment)
    file.write('\n  },')


def write_frames(file, root: ET.Element, subject: {}):
    """Write all segments to frame"""
    file.write('\n')
    file.write('frames = {')
    for segment in root.iter('Segment'):
        write_frame(file, segment, subject)
    file.write('\n},')


def write_lua(filepath: str, root: ET.Element, subject: {}):
    file = open(filepath, 'w')
    file.write('return {')
    write_metadata(file, subject)
    write_global_information(file)
    write_frames(file, root, subject)
    file.write('\n}')
    file.close()
