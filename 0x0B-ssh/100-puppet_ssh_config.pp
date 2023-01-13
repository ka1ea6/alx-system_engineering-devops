# Change SSH config file
exec {'echo':
  path    => ['/usr/bin', 'usr/local/bin', '/bin'],
  command => 'echo "	IdentityFile ~/.ssh/school\n	PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
