# Using Puppet, create a manifest that kills a process named killmenow
exec { 'killmenow':
    cwd => '/home/vagrant/holberton-system_engineering-devops/0x0A-configuration_management',
    command => 'pkill -f ./killmenow',
    path => '/usr/bin',
}
