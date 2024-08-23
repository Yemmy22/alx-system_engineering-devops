# Modifies the User Rate Limit (ULIMIT)

exec { 'Increase ULIMIT' :
  command => 'sed -i "/^ULIMIT=\"-n [0-9]\+\"/s/[0-9]\+/4096/" txt',
  path    => ['/usr/bin', '/usr/sbin'],
}
