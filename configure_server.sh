#!/bin/bash -ex
mydir=$(cd "$(dirname "$0")"; pwd)

export ANSIBLE_CONFIG=${mydir}/ansible.cfg
export ANSIBLE_REMOTE_USER=root
export ANSIBLE_ROLES_PATH=${mydir}/roles
hosts=${mydir}/server_inventory.yml
playbook=${mydir}/playbooks/server.yml
ansible-playbook -i "${hosts}" "${playbook}"
