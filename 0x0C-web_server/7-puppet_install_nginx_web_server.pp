# Installs and initializes an Nginx server

exec { 'install':
  provider => shell,
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; echo "Hello World!" | sudo tee /var/www/html/index.html; sudo sed -i "s+server_name _;+server_name _;\n\tlocation /redirect_me{\n\t\trewrite ^ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n\t}" /etc/nginx/sites-available/default; sudo service nginx start;',
}
