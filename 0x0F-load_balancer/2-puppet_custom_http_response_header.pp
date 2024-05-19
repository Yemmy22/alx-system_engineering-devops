# This manifest installs and configures nginx on a new ubuntu machine to listen on port 80, with a redirection and custom 404 page.

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

file {'/var/www/html/index.html':
  content => 'Hello World!'
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

exec {'HTTP header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
