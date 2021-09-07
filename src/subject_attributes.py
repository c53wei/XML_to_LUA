import xml.etree.ElementTree as ET


def get_subject_attributes(root: ET.Element) -> dict:

    # Initialize attribute dictionary to be returned
    subject_attributes_dict = {}
    for child in root.iter('StaticParameter'):

        subject_attributes_dict[child.get('NAME')] = child.get('VALUE')

    subject_attributes_dict['sex'] = _m0_f1(subject_attributes_dict.get('gender_m0_f1'))

    return subject_attributes_dict


def _m0_f1(value: str):
    if value is '0':
        return 'male'
    elif value is '1':
        return 'female'
    else:
        return None