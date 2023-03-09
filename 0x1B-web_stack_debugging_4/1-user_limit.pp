# Change OS open file hard and soft limit

exec { 'replace-hard':
  provider => shell,
  command  => 'sed -i +hard nofile 5+hard nofile 50000+ /etc/security/limits.conf'
  before   => Exec['replace-02']
}

exec { 'replace-soft':
  provider => shell,
  command  => 'sed -i +soft nofile 4+soft nofile 40000+ /etc/security/limits.conf'
}
