import lxml
from lxml import etree
import xmltodict
xml_path = 'XML.xml'
result_xml_path = 'result.xml'
xml_schema_path = 'xml_schema.xsd'
dtd_path = 'DTD.dtd'

def validateSchema(XMLfile: str, XMLSchema: str) -> bool:

    xml_schema_doc = etree.parse(XMLSchema)
    xml_schema = etree.XMLSchema(xml_schema_doc)

    xml_doc = etree.parse(XMLfile)
    result = xml_schema.validate(xml_doc)

    if result:
        print("File Validated")
    else:
        print("Your XML file does not conform to its XML Schema")
        
def validateDTD(XMLfile: str, DTDSchema: str) -> bool:

    dtd_schema = etree.DTD(open(DTDSchema, 'rb'))

    xml_doc = etree.parse(XMLfile)
    result = dtd_schema.validate(xml_doc)

    if result:
        print("File Validated")
    else:
        print("Your XML file does not conform to its DTD Schema")

def validateXML(XMLfile: str, ValidationFile: str) -> bool:
    try:
        if ValidationFile[-4:] == '.dtd':
            validateDTD(XMLfile, ValidationFile)
        elif ValidationFile[-4:] == '.xsd':
            validateSchema(XMLfile, ValidationFile)
        else:
            raise Exception("Validation File is not correct")
    except:
        raise Exception("XML file is not correct")
        
        
def task_a(xml_path):
    validateSchema(xml_path, xml_schema_path)
    validateDTD(xml_path, dtd_path)
    
print("\nTask a\n")
task_a(xml_path)

def task_b(xml_path):
    validateXML(xml_path, xml_schema_path)
    validateXML(xml_path, dtd_path)
    
print("\n\nTask b\n")
task_b(xml_path)


def task_c(xml_path):
    with open(xml_path) as fd:
        data = xmltodict.parse(fd.read())
        data['record'].pop('contributor', None)

        data['record']['contributor'] = {}

        data['record']['contributor']['name'] = 'abhinav'
        data['record']['contributor']['gender'] = 'male'

    with open('result.xml', 'w') as result_file:
        result_file.write(xmltodict.unparse(data, pretty=True))
    print("Data saved into result.xml")    
    
print("\n\nTask c\n")
task_c(xml_path)

def task_d(result_xml_path):
    print("Validation result with new schema\n")
    validateXML(result_xml_path, xml_schema_path)
    validateXML(result_xml_path, dtd_path)

    with open(result_xml_path) as fd:
        data = xmltodict.parse(fd.read())
        
    data['record'].pop('contributor', None)
    data['record']['contributor'] = 'text'
    
    with open(result_xml_path, 'w') as result_file:
        result_file.write(xmltodict.unparse(data, pretty=True))
    
    print("\n\nValidation result after reverting new schema")
    validateXML(result_xml_path, xml_schema_path)
    validateXML(result_xml_path, dtd_path)
    
print("\n\nTask d\n")
task_d(result_xml_path)