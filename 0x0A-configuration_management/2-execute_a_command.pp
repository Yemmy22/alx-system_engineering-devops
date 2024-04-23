# This script kills - gracefully end -  a running process.

exec { 'pkill':
  path    => '/usr/bin',
  command => 'pkill killmenow',
}
