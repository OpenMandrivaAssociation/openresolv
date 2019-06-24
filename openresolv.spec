Name:		openresolv
Version:	3.5.6
Release:	1
Summary:	A framework for managing DNS information 
License:	BSD
Group:		System/Base
URL:		http://roy.marples.name/projects/%name
Source0:	http://roy.marples.name/downloads/openresolv/%{name}-%{version}.tar.xz
Patch0:		fs33801.patch
BuildArch:	noarch

Requires:	filesystem

%description
resolvconf is the middleman between the network
configuration services and /etc/resolv.conf.
resolvconf itself is just a script that stores,
removes and lists a full resolv.conf generated
for the interface. It then calls all the helper
scripts it knows about so it can configure the real
/etc/resolv.conf and optionally any local nameservers
other can libc.

%package	bind
Summary:	Bind subscriber for openresolv
Group:		System/Base
Requires:	%name = %version-%release
Requires:	bind

%description	bind
bind subscriber for openresolv

%package	dnsmasq
Summary:	Dnsmasq subscriber for openresolv
Group:		System/Base
Requires:	%name = %version-%release
Requires:	dnsmasq

%description	dnsmasq
dnsmasq subscriber for openresolv

%package	unbound
Summary:	Unbound subscriber for openresolv
Group:		System/Base
Requires:	%name = %version-%release
Requires:	unbound

%description	unbound
unbound subscriber for openresolv

%package pdnsd
Summary:	Pdnsd subscriber for openresolv
Group:		System/Base
Requires:	%name = %version-%release
Requires:	pdnsd

%description pdnsd
pdnsd subscriber for openresolv

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --sbindir=/sbin --libexecdir=/lib/resolvconf \
           --localstatedir=%_var \
           --rundir=%_var/run \
           --os=linux
%make

%install
%makeinstall_std

%files
/sbin/resolvconf
%config(noreplace) %{_sysconfdir}/resolvconf.conf
/lib/resolvconf/libc
%{_mandir}/man5/*
%{_mandir}/man8/*

%files bind
/lib/resolvconf/named

%files dnsmasq
/lib/resolvconf/dnsmasq

%files unbound
/lib/resolvconf/unbound

%files pdnsd
/lib/resolvconf/pdnsd

