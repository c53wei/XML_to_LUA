import xml.etree.ElementTree as ET

from collections import defaultdict


def find_marker_name_position(root: ET.Element) -> {}:
    "Creates dictionary of form {marker_name, [x, y, z]}"
    # <Parameter> section contains xyz components of marker information
    marker_xyz = {}
    for marker_coord in root.iter('Parameter'):
        marker_xyz[marker_coord.get('NAME')] = marker_coord.get('VALUE')
    return marker_xyz


def link_segment_to_marker(root: ET.Element) -> defaultdict:
    marker_xyz = find_marker_name_position(root)
    # <TargetLocalPointToWorldPoint> contains segment and marker data
    segment_marker_data = defaultdict(lambda: defaultdict(dict))
    for marker in root.iter('TargetLocalPointToWorldPoint'):
        segment_name = marker.get('SEGMENT')
        marker_name = marker.get('MARKER')

        location_xyz_names = str.split(marker.get('POSITION'), ' ')
        location_xyz_values = [marker_xyz.get(location_name.strip('\''), location_name) \
                               for location_name in location_xyz_names]
        segment_marker_data[segment_name][marker_name] = location_xyz_values

    return segment_marker_data
