# Change OS open file hard and soft limit

exec { 'replace-hard':
  provider => shell,
  command  => 'sudo sed -i "s+hard nofile 5+hard nofile 50000+" /etc/security/limits.conf',
  before   => Exec['replace-soft']
}

exec { 'replace-soft':
  provider => shell,
  command  => 'sudo sed -i "s+soft nofile 4+soft nofile 40000+" /etc/security/limits.conf',
}
