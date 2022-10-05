# Fix Open files at Nginx level using ulimit
exec { 'config':
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
  provider => shell,
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['config'],
}
