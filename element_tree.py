import json

import xml.etree.ElementTree as ET
import tree_attributes

from markers import link_segment_to_marker

tree = ET.parse('data/mIOR.vsk')

def print_tree(root: ET.Element):
    for child in root.iter("Segment"):
        print(f'{child.get("NAME")}\t{child.get("body")}\t{child.get("joint_frame")}\t{child.get("markers")}')

# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(tree.getroot())
segment_marker_data = link_segment_to_marker(tree.getroot())
tree_attributes.add_position_info(tree.getroot(), segment_marker_data)

print_tree(tree.getroot())

test_child = tree.getroot().findall('.//Segment')[1]
with open('test.lua', 'w') as file:
    keys = ['name', 'parent', 'joint_frame', 'body', 'markers',  ]
    for key, value in test_child.attrib.items():
        file.write('%s = %s\n' % (key, value))



