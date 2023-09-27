# Using Puppet

package { 'nginx':
  ensure => installed,
}

file_line { 'install':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'rewrite ^/redirect_me https://www.github.com/zachafs permanent;',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello world!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

