import numpy as np
import xml.etree.ElementTree as ET

from anthropometrics.getJointAxis import joint_dict
from anthropometrics.getDeLevaModel import calc_anthro

def add_parent_info(et: ET.Element):
    """
    Sets 'reference' to parent node for all children
    :param et: Starting point of tree, can be root or any node
    """
    for child in et:
        child.attrib['parent'] = et
        add_parent_info(child)


def strip_parent_info(et: ET.Element):
    for child in et:
        child.attrib.pop('parent', 'None')
        strip_parent_info(child)


def get_parent(et: ET.Element):
    if 'parent' in et.attrib:
        return et.attrib['parent']
    else:
        return None


def add_position_info(root: ET.Element, segment_data: {}):
    """
    Sets marker and joint frame position vector relative to parent segment
    :param root: Starting point in tree from which marker data exists in
    :param segment_data: Nested dictionary in form {segment_name: {marker_name: [x, y, z]...}
    """
    for child in root.findall('.//Segment'):
        body_part = child.get('NAME')
        # Convert joint position co-ordinates to float
        joint_coord = np.asfarray(str.split(child[0].get('PRE-POSITION'), ' '), float)
        try:
            parent_joint_coord = np.asfarray(str.split(get_parent(child)[0].get('PRE-POSITION'), ' '))
        except TypeError:
            print(f'{body_part} does not have a parent segment')
            parent_joint_coord = np.zeros(3)
            continue
        # Anthropometric info
        segment_length = np.linalg.norm(joint_coord-parent_joint_coord)
        child.attrib['body'] = dict(zip(['mass', 'com', 'inertia'],
                                        calc_anthro(body_part=body_part,
                                                    segment_length=segment_length)))
        # Position info
        child.attrib['joint_frame'] = {}
        child.attrib['joint_frame']['r'] = joint_coord
        child.attrib['joint_frame']['E'] = joint_dict.get(child[0].tag)
        # Marker info
        child.attrib['markers'] = segment_data[body_part]
        add_position_info(child, segment_data)


def get_markers(et):
    "Gets markers and their positions of a segment"
    if 'markers' in et.attrib:
        return et.attrib['markers']
    else:
        return None


def get_r(et):
    "Gets position relative to parent segment"
    if 'r' in et.attrib['joint_frame']:
        return et.attrib['joint_frame']['r']
    else:
        return None