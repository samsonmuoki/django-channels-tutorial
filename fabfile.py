from fabric.api import *


def ping():
    local('ansible all -m ping -i ansible_playbooks/hosts.yml')

def deploy():
    local('ansible-playbook ansible_playbooks/initialization_playbook.yml -i ansible_playbooks/hosts.yml')
    local('ansible-playbook ansible_playbooks/nginx_playbook.yml -i ansible_playbooks/hosts.yml')
    local('ansible-playbook ansible_playbooks/gunicorn_playbook.yml -i ansible_playbooks/hosts.yml')
    local('ansible-playbook ansible_playbooks/letsencrypt_playbook.yml -i ansible_playbooks/hosts.yml')
