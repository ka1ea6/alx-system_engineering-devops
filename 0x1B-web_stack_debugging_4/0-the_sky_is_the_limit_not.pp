# Fix failure on high requests.

exec {'replace':
  command  => 'sudo sed -i "s+ULIMIT=\"-n 15\"+ULIMIT=\"-n 4096\"+ /etc/default/nginx'
  provider => shell,
  before   => Exec['restart'],
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
