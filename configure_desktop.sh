#!/bin/bash -ex
mydir=$(cd "$(dirname "$0")"; pwd)
local_user=$(id -un)
sudo nice -n 0 "${mydir}/run_ansible.sh" "${local_user}"
