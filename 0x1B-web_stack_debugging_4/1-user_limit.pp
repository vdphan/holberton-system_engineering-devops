# login with the holberton user and open a file without any error message
exec { 'delete holberton user':
    command => "sed -i '/holberton hard nofile 5/d' /etc/security/limits.conf",
    path    => '/bin/',
}

exec { 'delete holberton user soft':
    command => "sed -i '/holberton soft nofile 4/d' /etc/security/limits.conf",
    path    => '/bin/',
}
