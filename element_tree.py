import xml.etree.ElementTree as ET

tree = ET.parse('../jan.vsk')
root = tree.getroot()

# <Parameter> contains values corresponding to marker locations
parameters = root[0]
marker_xyz = {}
for x in parameters:
    if x.tag == 'Parameter':
        marker_xyz[x.attrib['NAME']] = x.attrib['VALUE']

# Skeleton contains segment and corresponding joint in tree format
skeleton = root[1]
segment_root = skeleton[0]
# Target set contains objects that reference location of markers in <Parameters>
target_set = root[3][0]
markers = {}
for x in target_set:
    location_xyz_names = str.split(x.attrib['POSITION'], ' ')
    location_xyz_values = [marker_xyz.get(location_name.strip('\''), location_name) for location_name in location_xyz_names]
    markers[x.attrib['MARKER']] = location_xyz_values





