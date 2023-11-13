# change the file descriptor limit for the server

exec { 'change-limit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => '/bin',
}

# Restart nginx

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['change-limit'],
}
