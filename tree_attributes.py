import numpy as np
import xml.etree.ElementTree as ET


def add_parent_info(et: ET.Element):
    """
    Sets 'reference' to parent node for all children
    :param et: Starting point of tree, can be root or any node
    """
    for child in et:
        child.attrib['__parent__'] = et
        add_parent_info(child)


def strip_parent_info(et: ET.Element):
    for child in et:
        child.attrib.pop('__parent__', 'None')
        strip_parent_info(child)


def get_parent(et: ET.Element):
    if '__parent__' in et.attrib:
        return et.attrib['__parent__']
    else:
        return None


def add_position_info(root: ET.Element, segment_data: {}):
    """
    Sets marker and joint frame position vector relative to parent segment
    :param root: Starting point in tree from which marker data exists in
    :param segment_data: Nested dictionary in form {segment_name: {marker_name: [x, y, z]...}
    """
    for child in root.findall('.//Segment'):
        child.attrib['__markers__'] = segment_data[child.get('NAME')]
        child.attrib['__r__'] = child[0].get('PRE-POSITION')
        child.attrib['__E__'] = np.identity(3)  # Stub until rotation matrix is verified

        add_position_info(child, segment_data)
        # print(f'{child.get("NAME")}\t{child.get("__r__")}\t{child.get("__markers__")}')


def get_markers(et):
    "Gets markers and their positions of a segment"
    if '__markers__' in et.attrib:
        return et.attrib['__markers__']
    else:
        return None


def get_r(et):
    "Gets position relative to parent segment"
    if '__r__' in et.attrib:
        return et.attrib['__r__']
    else:
        return None