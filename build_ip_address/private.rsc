/log info "Loading private ipv4 address list"
/ip firewall address-list
:do { add address=0.0.0.0/8 list=Private } on-error={}
:do { add address=10.0.0.0/8 list=Private } on-error={}
:do { add address=100.64.0.0/10 list=Private } on-error={}
:do { add address=127.0.0.0/8 list=Private } on-error={}
:do { add address=169.254.0.0/16 list=Private } on-error={}
:do { add address=172.16.0.0/12 list=Private } on-error={}
:do { add address=192.0.0.0/24 list=Private } on-error={}
:do { add address=192.0.2.0/24 list=Private } on-error={}
:do { add address=192.88.99.0/24 list=Private } on-error={}
:do { add address=192.168.0.0/16 list=Private } on-error={}
:do { add address=198.18.0.0/15 list=Private } on-error={}
:do { add address=198.51.100.0/24 list=Private } on-error={}
:do { add address=203.0.113.0/24 list=Private } on-error={}
:do { add address=224.0.0.0/3 list=Private } on-error={}
