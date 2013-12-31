#
# Conditional build:
%bcond_without	aep	# AEP Crypto Accelerator support
%bcond_without	bcom	# Broadcom Crypto Accelerator support
%bcond_with	corrent	# Corrent Crypto Accelerator support [BR: libsocketarmor + typhoon.h]
#
Summary:	An Implementation of PKCS#11 (Cryptoki) v2.11
Summary(pl.UTF-8):	Implementacja PKCS#11 (Cryptoki) v2.11
Name:		opencryptoki
Version:	3.0
Release:	1
License:	CPL v0.5
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/opencryptoki/%{name}-v%{version}.tar.gz
# Source0-md5:	ec4e2a196c8a336d400d3b17288260af
Patch0:		%{name}-ica.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-bcom.patch
Patch3:		%{name}-aep.patch
Patch4:		%{name}-format.patch
Patch5:		%{name}-noroot.patch
Patch6:		%{name}-notonlysystemd.patch
URL:		http://opencryptoki.sourceforge.net/
%{?with_aep:BuildRequires:	aep1000-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
%{?with_bcom:BuildRequires:	bcm5820-devel}
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
Obsoletes:	opencryptoki-static

%description devel
Header files for openCryptoki library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openCryptoki.

%package module-aeptok
Summary:	AEP Crypto Accelerator support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzeń AEP Crypto Accelerator dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-aeptok
This package brings the necessary libraries and files to support AEP
Crypto Accelerator devices in the openCryptoki stack.

%description module-aeptok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi urządzeń
kryptograficznych AEP Crypto Accelerator w stosie openCryptoki.

%package module-bcomtok
Summary:	Broadcom Crypto Accelerator support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzeń Broadcom Crypto Accelerator dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-bcomtok
This package brings the necessary libraries and files to support
Broadcom Crypto Accelerator devices in the openCryptoki stack.

%description module-bcomtok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi urządzeń
kryptograficznych Broadcom Crypto Accelerator w stosie openCryptoki.

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

%package module-crtok
Summary:	Corrent Crypto Accelerator support for openCryptoki
Summary(pl.UTF-8):	Obsługa urządzeń Corrent Crypto Accelerator dla openCryptoki
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description module-crtok
This package brings the necessary libraries and files to support
Corrent Crypto Accelerator devices in the openCryptoki stack.

%description module-crtok -l pl.UTF-8
Ten pakiet dostarcza biblioteki i pliki potrzebne do obsługi urządzeń
kryptograficznych Corrent Crypto Accelerator w stosie openCryptoki.

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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_aep:--disable-aeptok} \
	%{!?with_bcom:--disable-bcomtok} \
	%{!?with_corrent:--disable-crtok} \
%ifarch s390 s390x
	--enable-ccatok \
	--enable-icatok \
%else
	--disable-ccatok \
	--disable-icatok \
%endif
	--enable-tpmtok \
	--with-systemd=%{systemdunitdir}
# icctok (PCICC) not supported on Linux (only AIX, Windows, z/OS, OS/390)
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
%doc AUTHORS COPYRIGHTS ChangeLog FAQ LICENSE README TODO doc/{README.token_data,openCryptoki-HOWTO.pdf}
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

%if %{with aep}
%files module-aeptok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_aep.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_AEP.so
%endif

%if %{with bcom}
%files module-bcomtok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_bc.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_BC.so
%endif

%ifarch s390 s390x
%files module-ccatok
%defattr(644,root,root,755)
%doc doc/{README-IBM_CCA_users,README.cca_stdll}
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_cca.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_CCA.so
%endif

%if %{with corrent}
%files module-crtok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_cr.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_CR.so
%endif

%ifarch s390 s390x
%files module-icatok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/libpkcs11_ica.so*
%attr(755,root,root) %{_libdir}/opencryptoki/stdll/PKCS11_ICA.so
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
