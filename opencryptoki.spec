Summary:	An Implementation of PKCS#11 (Cryptoki) v2.11
Summary(pl.UTF-8):	Implementacja PKCS#11 (Cryptoki) v2.11
Name:		opencryptoki
Version:	2.2.4.1
Release:	1
License:	CPL v0.5
Group:		Applications/System
Source0:	http://dl.sourceforge.net/opencryptoki/%{name}-%{version}.tar.bz2
# Source0-md5:	d26093eb733ed9052b16dc33b445778a
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	aep1000-devel
BuildRequires:	bcm5820-devel
BuildRequires:	libica-devel
BuildRequires:	openssl-devel
BuildRequires:	trousers-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The openCryptoki package implements the PKCS#11 version 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%description -l pl.UTF-8
Pakiet openCryptoki implementuje standard PKCS#11 w wersji 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%package libs
Summary:	openCryptoki library
Summary(pl.UTF_8):	Biblioteka openCryptoki
Group:		Libraries

%description libs
The openCryptoki library implements the PKCS#11 version 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%description -l pl.UTF-8
Biblioteka openCryptoki implementuje standard PKCS#11 w wersji 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%package devel
Summary:	Header files for openCryptoki library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openCryptoki
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for openCryptoki library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openCryptoki.

%package static
Summary:	Static openCryptoki library
Summary(pl.UTF-8):	Statyczna biblioteka openCryptoki
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static openCryptoki library.

%description static -l pl.UTF-8
Statyczna biblioteka openCryptoki.

%prep
%setup -q

%build
%configure \
	--enable-static \
	--disable-crtok \
	--enable-icatok \
	--enable-tpmtok
# icctok (PCICC) not supported on Linux (only AIX, Windows, z/OS, OS/390)
# crtok requires some weird library (libsocketarmor + typhoon.h) - not found

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	initdir=/etc/rc.d/init.d

rm -f $RPM_BUILD_ROOT%{_libdir}/opencryptoki/stdll/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHTS FAQ LICENSE README TODO doc/*
%attr(755,root,root) %{_sbindir}/pkcs11_startup
%attr(755,root,root) %{_sbindir}/pkcsconf
%attr(755,root,root) %{_sbindir}/pkcs_slot
%attr(755,root,root) %{_sbindir}/pkcsslotd
%attr(754,root,root) /etc/rc.d/init.d/pkcsslotd
%dir /var/lib/opencryptoki
%{_libdir}/opencryptoki/methods
%{_libdir}/pkcs11/methods
%ifnarch s390 s390x
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_sw.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_SW.so
%endif
# aep
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_aep.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_AEP.so
# bc
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_bc.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_BC.so
# ica
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_ica.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
# tpm
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_tpm.so*

%files libs
%defattr(644,root,root,755)
/etc/ld.so.conf.d/opencryptoki-*.conf
%dir %{_libdir}/opencryptoki
%attr(755,root,root) %{_libdir}/opencryptoki/libopencryptoki.so*
%attr(755,root,root) %{_libdir}/opencryptoki/PKCS11_API.so
%dir %{_libdir}/opencryptoki/stdll
%dir %{_libdir}/pkcs11
%attr(755,root,root) %{_libdir}/pkcs11/libopencryptoki.so
%attr(755,root,root) %{_libdir}/pkcs11/PKCS11_API.so
%{_libdir}/pkcs11/stdll

%files devel
%defattr(644,root,root,755)
%{_libdir}/opencryptoki/libopencryptoki.la
%{_includedir}/opencryptoki

%files static
%defattr(644,root,root,755)
%{_libdir}/opencryptoki/libopencryptoki.a
