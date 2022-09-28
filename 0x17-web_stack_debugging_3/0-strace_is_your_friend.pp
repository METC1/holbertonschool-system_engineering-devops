# Puppet script to fix Wordpress settings
exec { 'Fix_wordpresss':
	command	=>	"sed '/sphpp/php/g'/var/www/html/wp-settings.php";
	provider=>	shell,
	}
