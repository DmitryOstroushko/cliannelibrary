# clianne library - useful python methods

![PyPI](https://img.shields.io/pypi/v/cliannelibrary?color=orange) ![Python 3.6, 3.7, 3.8](https://img.shields.io/pypi/pyversions/cliannelibrary?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/DmitryOstroushko/cliannelibrary?color=blueviolet) ![License](https://img.shields.io/pypi/l/cliannelibrary?color=blueviolet) ![Forks](https://img.shields.io/github/forks/DmitryOstroushko/cliannelibrary?style=social)

**Clianne Library** - this project is a Python client library which includes useful methods on different topics:  

- processing XML resources  

- custom functions for working with files  


## Installation

Install the current version with [PyPI](https://pypi.org/project/cliannelibrary/):

```bash
pip install cliannelibrary
```

Or from Github:
```bash
pip install https://github.com/DmitryOstroushko/cliannelibrary/archive/main.zip
```

## Usage

1) XML processing  
You can create XMLLibrary instance based on XML file, and then use it to modify XML structure with operarions ADD, MODIFY and DELETE

```python
xml_structure = XMLLibrary('file.xml')

xml_structure.set_xml_node_to_modify(tag='xml_tag',
                                     attrib_dict={'attr_1': 'test_1',
                                                  'attr_2': 'test_2'}
                                     node_value='text'
                                    )
xml_structure.do_modify_xml(3)
```

2) You can rename files to digital-names with mask-smaple

```python
mask: str ='*'
start_number: int = 20210300
FileLibrary().rename_file_by_mask(False, mask, start_number)
```

## Example

Create a new Story in the first Project that is returned from the API in the all projects list.

*If you installed a module from PyPi, you should to import it like this: ``` from clubhouse_api import ClubHouse ```*

*If from GitHub or source: ``` from club_house_api import ClubHouse ```*

```python
from club_house_api import ClubHouse
import asyncio
import os

TOKEN = os.getenv('API_TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()

async def main():

    all_projects = await club_house.projects()
    first_project_id = all_projects[0]['id']

    new_story = {'name': 'My new story', 'project_id': first_project_id}
    story = await club_house.stories.create(**new_story)
    print(story)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


## Contributing

Bug reports and/or pull requests are welcome


## License

The module is available as open source under the terms of the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0)
