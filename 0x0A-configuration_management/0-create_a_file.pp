# Create a file 'school' in dir /tmp

file { 'first':
  path    => '/tmp',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
}
