#!/usr/bin/env bash
# using puppet for Client configuration file

file { '/etc/ssh/ssh_config':
    ensure  => present,
    content => "
        # SSH client configuration
        Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
}
