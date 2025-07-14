Summary:	An Implementation of PKCS#11 (Cryptoki) v2.11
Summary(pl.UTF-8):	Implementacja PKCS#11 (Cryptoki) v2.11
Name:		opencryptoki
Version:	3.10.0
Release:	1
License:	CPL v0.5
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/opencryptoki/%{name}-%{version}.tar.gz
# Source0-md5:	7e857a57a7082e7c1728e7acb9fe8c79
Patch0:		%{name}-sh.patch
Patch1:		%{name}-noroot.patch
Patch2:		%{name}-notonlysystemd.patch
URL:		https://opencryptoki.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
%ifarch s390 s390x
BuildRequires:	libica-devel >= 2.0
%endif
BuildRequires:	libtool >= 2:2
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	trousers-devel >= 0.2.9
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires(postun):	/usr/sbin/groupdel
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts
Requires:	systemd-units >= 38
Provides:	group(pkcs11)
Obsoletes:	opencrytoki-module-aeptok < 3.4
Obsoletes:	opencrytoki-module-crtok < 3.4
Obsoletes:	opencrytoki-module-bcomtok < 3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	.*%{_libdir}/opencryptoki/stdll/libpkcs11_.*\.so.*

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
Requires:	filesystem >= 4.0-28

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
Obsoletes:	opencryptoki-static < 2.3

%description devel
Header files for openCryptoki library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openCryptoki.

%package module-ccatok
Summary:	CCA cryptographics devices (secure-key) support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzeń kryptograficznych ICA (z bezpiecznym kluczem) dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-ccatok
This package brings the necessary libraries and files to support CCA
devices in the openCryptoki stack. CCA is an interface to IBM
cryptographic hardware such as IBM 4764 or 4765 that uses the
"co-processor" or "secure-key" path.

%description module-ccatok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi urządzeń
kryptograficznych CCA w stosie openCryptoki. CCA to interfejs do
sprzętu kryptograficznego firmy IBM, takiego jak IBM 4764 lub 4765,
wykorzystującego "koprocesor" lub ścieżkę "bezpiecznego klucza".

%package module-icatok
Summary:	ICA cryptographics devices (clear-key) support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzeń kryptograficznych ICA (z jawnym kluczem) dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-icatok
This package brings the necessary libraries and files to support ICA
devices in the openCryptoki stack. ICA is an interface to IBM
cryptographic hardware such as IBM 4764 or 4765 that uses the
"accelerator" or "clear-key" path.

%description module-icatok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi urządzeń
kryptograficznych ICA w stosie openCryptoki. ICA to interfejs do
sprzętu kryptograficznego firmy IBM, takiego jak IBM 4764 lub 4765,
wykorzystującego "akcelerator" lub ścieżkę "jawnego klucza".

%package module-icsftok
Summary:	ICSF (Integrated Cryptographic Service Facility) token support for openCryptoki
Summary(pl.UTF-8):	Obsługa tokenów ICSF (Integrated Cryptographic Service Facility) dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-icsftok
This package brings the necessary libraries and files to support ICSF
(Integrated Cryptographic Service Facility) remote tokens in the
openCryptoki stack.

%description module-icsftok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi zdalnych
tokenów ICSF (Integrated Cryptographic Service Facility) w stosie
openCryptoki.

%package module-swtok
Summary:	The software token implementation for openCryptoki
Summary(pl.UTF-8):	Programowa implementacja tokenu dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-swtok
This package brings the software token implementation to use
openCryptoki without any specific cryptographic hardware.

%description module-swtok -l pl.UTF-8
Ten pakiet dostarcza programową implementację tokenu, pozwalającą
używać openCryptoki bez żadnego specjalnego sprzętu kryptograficznego.

%package module-tpmtok
Summary:	TPM (Trusted Platform Module) device support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzenia TPM (Trusted Platform Module) dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-tpmtok
This package brings the necessary libraries and files to support TPM
(Trusted Platform Module) devices in the openCryptoki stack.

%description module-tpmtok -l pl.UTF-8
Ten pakiet dostarcza biblioteki oraz pliki potrzebne do obsługi
urządzeń TPM (Trusted Platform Module) w stosie openCryptoki.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%ifarch s390 s390x
	--enable-ccatok \
	--enable-ep11tok \
	--enable-icatok \
%else
	--disable-ccatok \
	--disable-ep11tok \
	--disable-icatok \
%endif
	--enable-tpmtok \
	--with-systemd=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	initdir=/etc/rc.d/init.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/opencryptoki/stdll/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 110 pkcs11

%post
/sbin/chkconfig --add pkcsslotd
%service pkcsslotd restart
%systemd_post pkcsslotd.service

%preun
%systemd_preun pkcsslotd.service
if [ "$1" = "0" ]; then
	%service -q pkcsslotd stop
	/sbin/chkconfig --del pkcsslotd
fi

%postun
%systemd_reload
if [ "$1" = "0" ]; then
	%groupremove pkcs11
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHTS ChangeLog FAQ LICENSE README.md doc/{README.token_data,opencryptoki-howto.md}
%attr(755,root,root) %{_sbindir}/pkcsconf
%attr(755,root,root) %{_sbindir}/pkcsicsf
%attr(755,root,root) %{_sbindir}/pkcsslotd
%{_libdir}/opencryptoki/methods
%{_libdir}/pkcs11/methods
%dir %{_sysconfdir}/opencryptoki
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opencryptoki/opencryptoki.conf
%attr(754,root,root) /etc/rc.d/init.d/pkcsslotd
%{systemdunitdir}/pkcsslotd.service
%dir /var/lib/opencryptoki
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki
%{systemdtmpfilesdir}/opencryptoki.conf
%{_mandir}/man1/pkcsconf.1*
%{_mandir}/man1/pkcsicsf.1*
%{_mandir}/man5/opencryptoki.conf.5*
%{_mandir}/man7/opencryptoki.7*
%{_mandir}/man8/pkcsslotd.8*

%files libs
%defattr(644,root,root,755)
/etc/ld.so.conf.d/opencryptoki-*.conf
%dir %{_libdir}/opencryptoki
%attr(755,root,root) %{_libdir}/opencryptoki/libopencryptoki.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/opencryptoki/libopencryptoki.so.0
# symlinked as pkcs11 module, so it's here not in -devel
%attr(755,root,root) %{_libdir}/opencryptoki/libopencryptoki.so
%attr(755,root,root) %{_libdir}/opencryptoki/PKCS11_API.so
%dir %{_libdir}/opencryptoki/stdll
%attr(755,root,root) %{_libdir}/pkcs11/libopencryptoki.so
%attr(755,root,root) %{_libdir}/pkcs11/PKCS11_API.so
%{_libdir}/pkcs11/stdll

%files devel
%defattr(644,root,root,755)
%{_libdir}/opencryptoki/libopencryptoki.la
%{_includedir}/opencryptoki

%ifarch s390 s390x
%files module-ccatok
%defattr(644,root,root,755)
%doc doc/{README-IBM_CCA_users,README.cca_stdll,README.pkcscca_migrate}
%attr(755,root,root) %{_sbindir}/pkcscca_migrate
%attr(755,root,root) %{_sbindir}/pkcscca_migrate.sh
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_cca.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/ccatok
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/ccatok/TOK_OBJ
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/ccatok
%{_mandir}/man1/pkcscca.1*
%endif

%ifarch s390 s390x
%files module-ep11tok
%defattr(644,root,root,755)
%doc doc/README.ep11_stdll
%attr(755,root,root) %{_sbindir}/pkcsep11_migrate
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_ep11.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_EP11.so
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opencryptoki/ep11tok.conf
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/ep11tok
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/ep11tok/TOK_OBJ
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/ep11tok
%{_mandir}/man1/pkcsep11_migrate.1*
%endif

%ifarch s390 s390x
%files module-icatok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_ica.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/lite
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/lite/TOK_OBJ
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/lite
%endif

%files module-icsftok
%defattr(644,root,root,755)
%doc doc/README.icsf_stdll
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_icsf.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_ICSF.so
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/icsf
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/icsf

%files module-swtok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_sw.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_SW.so
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/swtok
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/swtok/TOK_OBJ
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/swtok

%files module-tpmtok
%defattr(644,root,root,755)
%doc doc/README.tpm_stdll
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_tpm.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_TPM.so
%attr(770,root,pkcs11) %dir /var/lib/opencryptoki/tpm
%attr(770,root,pkcs11) %dir /var/lock/opencryptoki/tpm
