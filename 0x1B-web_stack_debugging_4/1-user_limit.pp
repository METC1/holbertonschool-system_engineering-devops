# Puppet script to fix user limits
exec { 'fix_user_hard':
    command  => 'sed -i "s/holberton hard nofile.*/holberton hard nofile 5000/g" /etc/security/limits.conf',
    provider => shell,
}
exec { 'fix_user_soft':
    command  => 'sed -i "s/holberton soft nofile.*/holberton soft nofile 5000/g" /etc/security/limits.conf',
    provider => shell,
}

