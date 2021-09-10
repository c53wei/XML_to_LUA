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


def add_position_info(root: ET.Element, segment_data: {}, subject_data):
    """
    Sets marker and joint frame position vector relative to parent segment
    :param root: Starting point in tree from which marker data exists in
    :param segment_data: Nested dictionary in form {segment_name: {marker_name: [x, y, z]...}
    """
    for child in root.iter('Segment'):
        body_part = child.get('NAME')
        # Convert joint position co-ordinates to float
        joint_coord = [float(i) for i in str.split(child[0].get('PRE-POSITION'), ' ')]
        try:
            parent_joint_coord = [float(i) for i in str.split(get_parent(child)[0].get('PRE-POSITION'), ' ')]
        except TypeError:
            print(f'{body_part} does not have a parent segment')
            parent_joint_coord = [0.0]*3
        # Anthropometric info
        segment_length = np.linalg.norm(np.array(joint_coord)-np.array(parent_joint_coord))
        child.attrib['length'] = segment_length
        mass = subject_data.get('weight')
        child.attrib['body'] = dict(zip(['mass', 'com', 'inertia'],
                                        calc_anthro(body_part=body_part,
                                                    segment_length=segment_length,
                                                    female=bool(subject_data.get('gender_m0_f1')),
                                                    body_mass=float(mass) if mass else 65
                                                    )))
        # Position info
        child.attrib['joint_frame'] = {}
        child.attrib['joint_frame']['r'] = np.array([joint_coord])
        child.attrib['joint_frame']['E'] = np.identity(3)
        # Marker info
        child.attrib['markers'] = segment_data[body_part]
        # Joint type
        child.attrib['joint'] = joint_dict.get(child[0].tag)


def get_markers(et):
    """Gets markers and their positions of a segment"""
    if 'markers' in et.attrib:
        return et.attrib['markers']
    else:
        return None

