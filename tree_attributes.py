import numpy as np
import xml.etree.ElementTree as ET

from anthropometrics import calc_anthro


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
    if '__parent__' in et.attrib:
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
        # Anthropometric info, stub
        child.attrib['body'] = dict(zip(['mass', 'com', 'inertia'], calc_anthro()))

        # Position info
        child.attrib['joint_frame'] = {}
        child.attrib['joint_frame']['r'] = child[0].get('PRE-POSITION')
        child.attrib['joint_frame']['E'] = np.identity(3)  # ToDo: Stub until rotation matrix is verified

        # Marker info
        child.attrib['markers'] = segment_data[child.get('NAME')]
        add_position_info(child, segment_data)
        # print(f'{child.get("NAME")}\t{child.get("__r__")}\t{child.get("__markers__")}')


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