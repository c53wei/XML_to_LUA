# Credit: https://stackoverflow.com/questions/24239435/get-parent-element-after-using-find-method-xml-etree-elementtree

def addParentInfo(et):
    for child in et:
        child.attrib['__my_parent__'] = et
        addParentInfo(child)

def stripParentInfo(et):
    for child in et:
        child.attrib.pop('__my_parent__', 'None')
        stripParentInfo(child)

def getParent(et):
    if '__my_parent__' in et.attrib:
        return et.attrib['__my_parent__']
    else:
        return None

# tree = ...
# addParentInfo(tree.getroot())
# el = tree.findall(...)[0]
# parent = getParent(el)
# while parent:
#     ...
#     parent = getParent(parent)
# ...
# stripParentInfo(tree.getroot())