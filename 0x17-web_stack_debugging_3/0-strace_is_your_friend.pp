# This manuscript renames wp-setting file in apache root directory

exec { 'rename' :
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
}
