import xml.etree.ElementTree as ET

from collections import defaultdict

from add_parent import addParentInfo, getParent

tree = ET.parse('mIOR.vsk')
root = tree.getroot()
addParentInfo(tree.getroot())

# <Parameter> section contains xyz components of marker information
marker_xyz = {}
for marker_coord in root.findall('.//Parameter'):
        marker_xyz[marker_coord.get('NAME')] = marker_coord.get('VALUE')

# <TargetLocalPointToWorldPoint> contains segment and marker data
segment_marker_data = defaultdict(lambda: defaultdict(dict))
for marker in root.findall('.//TargetLocalPointToWorldPoint'):
    segment_name = marker.get('SEGMENT')
    marker_name = marker.get('MARKER')

    location_xyz_names = str.split(marker.get('POSITION'), ' ')
    location_xyz_values = [marker_xyz.get(location_name.strip('\''), location_name) \
                           for location_name in location_xyz_names]
    segment_marker_data[segment_name][marker_name] = location_xyz_values





