# This manifest changes the values of identity file and password authentication in the /etc/ssh/ssh_config'

$config_file = file('/etc/ssh/ssh_config')
$mod_config = regsubst($config_file, '^#.*IdentityFile ~/.ssh/id_rsa$', '    IdentityFile ~/.ssh/school', 'G')
$mod_config1 = regsubst($mod_config, '^#.*PasswordAuthentication yes$', '    PasswordAuthentication no', 'G')

file {  'modify config_file' :
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => $mod_config1,
}
