# Ping range
echo "fping -s -g 192.168.0.1 192.168.0.9 -r 1"

# Rsync folder from local to remote
echo "rsync -rtvz ~/local user@machine:~/target"

# Add proxy to apt
# Add to /etc/apt/apt.conf
Acquire::http::Proxy "http://pt02labproxy:3128";
