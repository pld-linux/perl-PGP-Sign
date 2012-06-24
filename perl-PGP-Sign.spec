#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PGP
%define		pnam	Sign
Summary:	PGP::Sign Perl module
Summary(cs):	Modul PGP::Sign pro Perl
Summary(da):	Perlmodul PGP::Sign
Summary(de):	PGP::Sign Perl Modul
Summary(es):	M�dulo de Perl PGP::Sign
Summary(fr):	Module Perl PGP::Sign
Summary(it):	Modulo di Perl PGP::Sign
Summary(ja):	PGP::Sign Perl �⥸�塼��
Summary(ko):	PGP::Sign �� ����
Summary(nb):	Perlmodul PGP::Sign
Summary(pl):	Modu� Perla PGP::Sign
Summary(pt):	M�dulo de Perl PGP::Sign
Summary(pt_BR):	M�dulo Perl PGP::Sign
Summary(ru):	������ ��� Perl PGP::Sign
Summary(sv):	PGP::Sign Perlmodul
Summary(uk):	������ ��� Perl PGP::Sign
Summary(zh_CN):	PGP::Sign Perl ģ��
Name:		perl-PGP-Sign
Version:	0.17
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	caab81561eeae34735d20dc308ea6428
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	gnupg
Requires:	gnupg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP::Sign - generates detached PGP signatures for data.

This package was built for using with GnuPG. If you want to use it
with PGP, you need to modify 'Global variables' section in the
PGP/Sign.pm file.

%description -l pl
PGP::Sign - generuje oddzielne sygnatury PGP dla danych.

Ten pakiet zosta� zbudowany do u�ycia z GnuPG. Je�li chcesz u�ywa� go
z PGP, musisz zmodyfikowa� sekcj� 'Global variables' w pliku
PGP/Sign.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor  \
	PGP=%{_bindir}/gpg \
	PGPSTYLE=GPG
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/PGP
%{_mandir}/man3/*
