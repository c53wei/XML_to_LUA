import xml.etree.ElementTree as ET
import tree_attributes
import subject_attributes


from markers import link_segment_to_marker
from write import write_lua


tree = ET.parse('../data/mIOR.vsk')
root = tree.getroot()
# Parse metadata such as age, mass, height, etc.
subject_attributes = subject_attributes.get_subject_attributes(root)
# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(root)
segment_marker_data = link_segment_to_marker(root)
tree_attributes.add_position_info(root, segment_marker_data)


# Write LUA
write_lua('../data/test.lua', root, subject_attributes)
