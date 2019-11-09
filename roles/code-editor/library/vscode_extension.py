#!/usr/bin/python
import subprocess
from ansible.module_utils.basic import *

DOCUMENTATION = '''
module: is_running
short_description: "Installs vscode extensions"
author:
  - Matthew Urry
requirements:
  - only standard library needed
options:
  name:
    description:
      - the name of the extension
      required: true
      default: null
  state:
    description:
        - What state this extension should be in one of [present, absent]
'''

def check_for_extension(name, data_dir):
    output = subprocess.check_output(["code", '--list-extensions', '--user-data-dir', data_dir])
    installed_extensions = [line.strip() for line in output.splitlines()]
    return name in installed_extensions

def install_extension(name, data_dir):
    if check_for_extension(name, data_dir):
        return False
    subprocess.check_call(["code", '--install-extension', name, '--user-data-dir', data_dir])
    return True

def uninstall_extension(name, data_dir):
    if not check_for_extension(name, data_dir):
        return False
    subprocess.check_call(["code", '--uninstall-extension', name, '--user-data-dir', data_dir])
    return True

def main():
    # The AnsibleModule provides lots of common code for handling returns, parses your arguments for you, and allows you to check inputs
    module = AnsibleModule(
        argument_spec={
            "name": {
                "required": True,
                "type": 'str'
            },
            "state": {
                "default": "present",
                "choices": ['present', 'absent'],
                "type": 'str'
            },
            "user_data_dir": {
                'type': 'str'
            }
        },
    )

    name = module.params['name']
    state = module.params['state']
    data_dir = module.params.get('user_data_dir', None)

    if state == 'present':
        module.exit_json(changed=install_extension(name, data_dir))
    else:
        assert state == 'absent'
        module.exit_json(changed=uninstall_extension(name, data_dir))


if __name__ == '__main__':
  main()