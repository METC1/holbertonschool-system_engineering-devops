# Puppet script to fix Wordpress settings
exec { 'fix_wordpresss':
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
    provider => shell,
}
