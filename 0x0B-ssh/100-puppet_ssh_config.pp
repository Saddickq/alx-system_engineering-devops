# SSH configuration file so that you can connect to a server without typing a password.

exec { 'append_to_file':
  path    => '/usr/bin',
  command => 'echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}

exec { 'append2_to_file':
  path    => '/usr/bin',
  command => 'echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
