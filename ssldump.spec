#
Summary:	SSLv3/TLS network protocol analyzer
Name:		ssldump
Version:	0.9b3
Release:	1
Epoch:		0
License:	BSD
Group:		Applications/Networking
Source0:	http://www.rtfm.com/ssldump/%{name}-%{version}.tar.gz
# Source0-md5:	ac8c28fe87508d6bfb06344ec496b1dd
URL:		http://www.rtfm.com/ssldump/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libpcap-devel >= 2:0.8.3
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When it identifies SSLv3/TLS traffic, it
decodes the records and displays them in a textual form to stdout. If
provided with the appropriate keying material, it will also decrypt
the connections and display the application data traffic.


%prep
%setup -q
sed -i -e 's#libpcap.a#libpcap.so#g' configure*
sed -i -e 's#net/bpf.h#pcap-bpf.h#g' base/pcap-snoop.c

%build
cp -f %{_datadir}/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--with-pcap-inc=%{_includedir} \
	--with-pcap-lib=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_sbindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_sbindir}/ssldump
%{_mandir}/man1/*
