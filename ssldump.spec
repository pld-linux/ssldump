Summary:	SSLv3/TLS network protocol analyzer
Summary(pl.UTF-8):	Analizator protokołu sieciowego SSLv3/TLS
Name:		ssldump
Version:	1.4
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	https://github.com/adulau/ssldump/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	20323bf4b4758f2be4412fa79e6013ab
URL:		https://github.com/adulau/ssldump/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	json-c-devel
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel >= 2:0.8.3
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When it identifies SSLv3/TLS traffic, it
decodes the records and displays them in a textual form to stdout. If
provided with the appropriate keying material, it will also decrypt
the connections and display the application data traffic.

%description -l pl.UTF-8
ssldump to analizator protokołu sieciowego SSLv3/TLS. Identyfikuje
połączenia TCP na wybranym interfejsie sieciowym i próbuje
interpretować je jako ruch SSLv3/TLS. Po zidentyfikowaniu ruchu
SSLv3/TLS dekoduje rekordy i wyświetla je w postaci tekstowej na
standardowym wyjściu. W przypadku wyposarzenia we właściwe klucze
będzie także dekodował połączenia i wyświetlał ruch danych aplikacji.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.* .
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_sbindir}/ssldump
%{_mandir}/man1/*
