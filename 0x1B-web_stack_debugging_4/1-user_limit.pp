# This manifest increases the file descriptor limits for users.

# Increase soft file limit for user
exec { 'increase soft file limit':
  command => 'sed -i "/^holberton soft nofile/s/[0-9]\\+/65536/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/usr/sbin'],
}

# Increase hard file limit for user
exec { 'increase hard file limit':
  command => 'sed -i "/^holberton hard nofile/s/[0-9]\\+/65536/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/usr/sbin'],
}
