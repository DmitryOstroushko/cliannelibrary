import cliannelibrary

print('--------------------------------------------')
print(dir(cliannelibrary.XMLLibrary))
print('--------------------------------------------')
print(dir(cliannelibrary.exceptions))
print('--------------------------------------------')
print(cliannelibrary.exceptions.files_exception.FileAlreadyExistsException)
print('--------------------------------------------')

a = cliannelibrary.XMLLibrary('entrypoints_links.xml')
a.set_xml_node_to_modify('entrypoint_links')

#a.do_modify_xml(1, "test_1", {"test_attrib_1": 1, "test_attrib_2": 2}, 'text_1', 2)
#a.do_modify_xml(1, "test_1", {"test_attrib_1": 1, "test_attrib_2": 2}, 'text_1', 3)
a.do_modify_xml(1, "test_1", {"test_attrib_1": '1', "test_attrib_2": '2'}, 'testing')
a.do_save_xml_tree('entrypoints_links_modified.xml')