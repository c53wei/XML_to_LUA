import xml.etree.ElementTree as ET


def get_subject_measurements(root: ET.Element) -> {}:

    # Initialize attribute dictionary to be returned
    metadata_dict = {}
    for child in root.iter('XMPParameter'):

        metadata_dict[child.get('Label')] = child.get('Value')
    return metadata_dict


def get_subject_traits(root: ET.Element) -> {}:

    # Initialize attribute dictionary to be returned
    traits_dict = {}
    for child in root.iter('StaticParameter'):

        traits_dict[child.get('NAME')] = child.get('VALUE')
    traits_dict ['sex'] = _m0_f1(traits_dict.get('gender_m0_f1'))

    return traits_dict


def _m0_f1(value: str):

    if value == '0':
        return 'male'
    elif value == '1':
        return 'female'
    else:
        return None