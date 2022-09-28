# Puppet 
exec { 'Fix_wordpresss':
	command	=>	"sed '/s.phpp/.php'/var/www/html/wp-settings.php";
	provider=>	shell,
	}
