# changing phpp to php in /var/html/wp-settings.php using regex

exec { 'change name':
  command  => 'sed s+phpp+php+g /var/html/wp-settings.php',
  provider =>  shell,
}
