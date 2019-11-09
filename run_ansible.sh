#!/bin/bash
mydir=$(cd "$(dirname "$0")"; pwd)
hosts=${mydir}/desktop_inventory.yml
playbook=${mydir}/playbooks/desktop.yml
export ANSIBLE_ROLES_PATH="${mydir}/roles" 
export ANSIBLE_CONFIG="${mydir}/ansible.cfg"
ansible-playbook -i "${hosts}" "${playbook}" --extra-vars "local_user=$1" -v
