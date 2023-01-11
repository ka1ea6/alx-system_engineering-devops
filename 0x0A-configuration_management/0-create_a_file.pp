file { 'create file in tmp':
  path    => '/tmp',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
}
