# installs the flask package using pip3

package {'flase:
  provider => 'pip3',
  ensure   => '2.1.0',
}
