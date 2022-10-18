from UI import name_view
from UI import surname_view
from UI import telephone_num_view
from UI import descrition_view

def create():
    xml = '<xml>\n'
    xml += '    <name>{}</name>\n'\
        .format(name_view())
    xml += '    <surname>{}</surname>\n'\
        .format(surname_view())
    xml += '    <telephone>{}</telephone>\n'\
        .format(telephone_num_view())
    xml += ' <description>{}</description>\n'\
        .format(descrition_view())
    xml += '</xml>'

    with open ('manual.xml', 'w') as page:
        page.write(xml)

    return xml