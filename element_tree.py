import xml.etree.ElementTree as ET
import tree_attributes

from markers import link_segment_to_marker

tree = ET.parse('data/mIOR.vsk')

# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(tree.getroot())
segment_marker_data = link_segment_to_marker(tree.getroot())
tree_attributes.add_position_info(tree.getroot(), segment_marker_data)

for child in tree.getroot().find('.//Segment'):
    print(f'{child.get("NAME")}\t{child.get("body")}\t{child.get("joint_frame")}\t{child.get("markers")}')


