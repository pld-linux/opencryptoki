Summary:	An Implementation of PKCS#11 (Cryptoki) v2.11
Summary(pl.UTF-8):	Implementacja PKCS#11 (Cryptoki) v2.11
Name:		opencryptoki
Version:	2.3.2
Release:	1
License:	CPL v0.5
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/opencryptoki/%{name}-%{version}.tar.bz2
# Source0-md5:	eada4c72c2563f2c9a1b44fc6d1856db
Patch0:		%{name}-ica.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-bcom.patch
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	aep1000-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	bcm5820-devel
%ifarch s390 s390x
BuildRequires:	libica-devel >= 2.0
%endif
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	trousers-devel >= 0.2.9
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
Summary(pl.UTF-8):	Biblioteka openCryptoki
Group:		Libraries

%description libs
The openCryptoki library implements the PKCS#11 version 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%description libs -l pl.UTF-8
Biblioteka openCryptoki implementuje standard PKCS#11 w wersji 2.11:
Cryptographic Token Interface Standard (Cryptoki).

%package devel
Summary:	Header files for openCryptoki library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openCryptoki
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	opencryptoki-static

%description devel
Header files for openCryptoki library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openCryptoki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-crtok \
%ifarch s390 s390x
	--enable-ccatok \
	--enable-icatok \
%else
	--disable-ccatok \
	--disable-icatok \
%endif
	--enable-tpmtok
# icctok (PCICC) not supported on Linux (only AIX, Windows, z/OS, OS/390)
# crtok requires some weird library (libsocketarmor + typhoon.h) - not found
# pkcscca_migrate requires xcryptolinz (IBM proprietary, zSeries only)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	initdir=/etc/rc.d/init.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/opencryptoki/stdll/*.la

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
%{_mandir}/man1/pkcs11_startup.1*
%{_mandir}/man1/pkcsconf.1*
%{_mandir}/man5/pk_config_data.5*
%{_mandir}/man7/opencryptoki.7*
%{_mandir}/man8/pkcsslotd.8*
# swtok
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_sw.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_SW.so
# aep
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_aep.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_AEP.so
# bc
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_bc.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_BC.so
%ifarch s390 s390x
# cca
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_cca.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
# ica
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_ica.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
%endif
# tpm
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_tpm.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_TPM.so

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
