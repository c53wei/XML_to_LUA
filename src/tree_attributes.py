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
        if 'child' not in et.attrib and child.tag == 'Segment':
            et.attrib['child'] = child
        add_parent_info(child)
     
        
def add_pelvis_info(pelvis: ET.Element):
    """Middle trunk is a fake segment. Pelvis' 'real' child is uppertrunk"""
    middle_trunk = pelvis.attrib['child'] 
    pelvis.attrib['child'] = middle_trunk.attrib['child']
    


def strip_parent_info(et: ET.Element):
    for child in et:
        child.attrib.pop('parent', 'None')
        strip_parent_info(child)


def get_parent(et: ET.Element):
    return et.attrib.get('parent', None)


def get_child(et: ET.Element):
    return et.attrib.get('child', None)


def add_position_info(root: ET.Element, segment_data: {}, subject_data):
    """
    Sets marker and joint frame position vector relative to parent segment
    :param root: Starting point in tree from which marker data exists in
    :param segment_data: Nested dictionary in form {segment_name: {marker_name: [x, y, z]...}
    """
    for parent in root.iter('Segment'):
        body_part = parent.get('NAME')
        if body_part == 'Pelvis':
            add_pelvis_info(parent)
        # Convert joint position co-ordinates to float
        joint_coord = [float(i)/1000 for i in str.split(parent[0].get('PRE-POSITION'), ' ')]
        child = get_child(parent)
        try:
            child_joint_coord = [float(i)/1000 for i in str.split(child[0].get('PRE-POSITION'), ' ')]
        except TypeError:
            print(f'{body_part} does not have a child segment')
            child_joint_coord = [0.0]*3
        # Anthropometric info
        segment_length = np.linalg.norm(np.array(joint_coord)-np.array(child_joint_coord))
        parent.attrib['length'] = segment_length
        mass = subject_data.get('weight')
        parent.attrib['body'] = dict(zip(['mass', 'com', 'inertia'],
                                        calc_anthro(body_part=body_part,
                                                    segment_length=segment_length,
                                                    female=bool(subject_data.get('gender_m0_f1')),
                                                    body_mass=float(mass) if mass else 65
                                                    )))
        # Position info
        parent.attrib['joint_frame'] = {}
        parent.attrib['joint_frame']['r'] = np.array([joint_coord])
        parent.attrib['joint_frame']['E'] = np.identity(3)
        # Marker info
        parent.attrib['markers'] = segment_data[body_part]
        # Joint type
        parent.attrib['joint'] = joint_dict.get(parent[0].tag)


def get_markers(et):
    """Gets markers and their positions of a segment"""
    if 'markers' in et.attrib:
        return et.attrib['markers']
    else:
        return None

