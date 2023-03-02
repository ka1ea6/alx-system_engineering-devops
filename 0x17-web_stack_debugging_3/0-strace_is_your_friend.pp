# changing phpp to php in /var/html/wp-settings.php using regex

exec { 'change name':
  command  => 'sed -i s+phpp+php+g /var/html/wp-settings.php',
  provider =>  shell,
}

