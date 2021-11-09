import xml.etree.ElementTree as ET
import tree_attributes
import subject_attributes


from markers import link_segment_to_marker
from write import write_lua


tree = ET.parse('../data/mIOR.vsk')
root = tree.getroot()

attribute_tree = ET.parse('../data/mIOR.XMP')
attribute_root = attribute_tree.getroot()
# Parse metadata such as age, mass, height, etc.
subject_values = subject_attributes.get_subject_traits(root)
subject_values.update(subject_attributes.get_subject_measurements(attribute_root))
# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(root)
segment_marker_data = link_segment_to_marker(root)
tree_attributes.add_position_info(root, segment_marker_data, subject_values)


# Write LUA
write_lua('../data/mIOR.lua', root, subject_values)

for parent in root.iter('Segment'):
    print(f"Parent: {parent.get('NAME')}")
    if parent.get('child'):
        print(f"Child: {parent.get('child').get('NAME')}")