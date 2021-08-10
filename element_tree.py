import _io
import re
import xml.etree.ElementTree as ET
import tree_attributes

from markers import link_segment_to_marker

def print_tree(root: ET.Element):
    for child in root.iter("Segment"):
        print(f'{child.get("NAME")}\t{child.get("body")}\t{child.get("joint_frame")}\t{child.get("markers")}')


# the simplest, lambda-based implementation
def multiple_replace(adict: {}, text: str):
    # Create a regular expression from all of the dictionary keys
    regex = re.compile("|".join(map(re.escape, adict.keys(  ))))

    # For each match, look up the corresponding value in the dictionary
    return regex.sub(lambda match: adict[match.group(0)], text)


def regex_format(filename: str):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = multiple_replace({'[': '{', ']': '}', ':': ' =', '\'': ''}, filedata)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)


def write_segment(file, test_child: ET.Element):
    
    keys = ['name', 'parent', 'joint_frame', 'body', 'markers', 'joint']
    values = [f'"{test_child.get("NAME")}"', f'"{tree_attributes.get_parent(test_child).get("NAME")}"',
              test_child.get('joint_frame'), test_child.get('body'),
              dict.__repr__(test_child.get('markers')), test_child.get('joint')]
    formatted_dict = dict(zip(keys, values))
    for key, value in formatted_dict.items():
        file.write('%s : %s,\n' % (key, value))


tree = ET.parse('data/mIOR.vsk')
root = tree.getroot()
# Link segment's parent and marker position info to each node
tree_attributes.add_parent_info(root)
segment_marker_data = link_segment_to_marker(root)
tree_attributes.add_position_info(root, segment_marker_data)

print_tree(root)
# 
# test_child = root.findall('.//Segment')[1]
with open('test.lua', 'w') as file:
    file.write('return\n')
    for child in root.iter('Segment'):
        file.write('{\n')
        write_segment(file, child)
        file.write('},\n')
    file.write('}')
regex_format('test.lua')

