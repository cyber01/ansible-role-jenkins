# Ansible Role: Jenkins

Installs and configures Jenkins

## Requirements

    Java (dependency)

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    ansible_jenkins_port: "8080"

Needs for firewalld

    ansible_jenkins_open_port: true

Allow remote connections to jenkins. Work only if `ansible_jenkins_open_port` and `firewalld` is installed.

## Dependencies


## Example Playbook

    - hosts: servers
      roles:
        - cyber01.ansible-role-jenkins


## License

MIT / BSD

## Author Information

This role was created in 2019 by [Sergey Brovko](http://cyber01.ru/).
