import json
import re
import xml.etree.ElementTree as ET
import tree_attributes

from markers import link_segment_to_marker

tree = ET.parse('data/mIOR.vsk')


def print_tree(root: ET.Element):
    for child in root.iter("Segment"):
        print(f'{child.get("NAME")}\t{child.get("body")}\t{child.get("joint_frame")}\t{child.get("markers")}')


# the simplest, lambda-based implementation
def multiple_replace(adict, text):
    # Create a regular expression from all of the dictionary keys
    regex = re.compile("|".join(map(re.escape, adict.keys(  ))))

    # For each match, look up the corresponding value in the dictionary
    return regex.sub(lambda match: adict[match.group(0)], text)


def replace_square_brackets(filename):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = multiple_replace({'[': '{', ']': '}', ':': '=', '\'': ''}, filedata)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(tree.getroot())
segment_marker_data = link_segment_to_marker(tree.getroot())
tree_attributes.add_position_info(tree.getroot(), segment_marker_data)

print_tree(tree.getroot())

test_child = tree.getroot().findall('.//Segment')[1]
with open('test.lua', 'w') as file:
    keys = ['name', 'parent', 'joint_frame', 'body', 'markers', 'joint']
    values = [test_child.get('NAME'), tree_attributes.get_parent(test_child),
              ]

    for key, value in test_child.attrib.items():
        file.write('%s : %s\n' % (key, value))

replace_square_brackets('test.lua')

