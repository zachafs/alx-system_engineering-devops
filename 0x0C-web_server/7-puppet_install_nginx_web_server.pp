# puppet

package { 'nginx':
 ensure => installed,
}

file_line { 'install':
 ensure => 'present',
 path	=> 'etc/nginx/sites-enabled/default',
 after	=> 'lesten 80 default_server;',
 line	=>'rewrite ^/redirect-me https://www.github.com/zachafs permanent;',
}

file { '/var/www/html/index.html':
 content => 'hello world!',
}

service { 'nginx':
 ensure => running,
 require => Package ['nginx'],
}
 
