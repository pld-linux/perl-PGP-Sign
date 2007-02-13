#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PGP
%define		pnam	Sign
Summary:	PGP::Sign Perl module
Summary(cs.UTF-8):	Modul PGP::Sign pro Perl
Summary(da.UTF-8):	Perlmodul PGP::Sign
Summary(de.UTF-8):	PGP::Sign Perl Modul
Summary(es.UTF-8):	Módulo de Perl PGP::Sign
Summary(fr.UTF-8):	Module Perl PGP::Sign
Summary(it.UTF-8):	Modulo di Perl PGP::Sign
Summary(ja.UTF-8):	PGP::Sign Perl モジュール
Summary(ko.UTF-8):	PGP::Sign 펄 모줄
Summary(nb.UTF-8):	Perlmodul PGP::Sign
Summary(pl.UTF-8):	Moduł Perla PGP::Sign
Summary(pt.UTF-8):	Módulo de Perl PGP::Sign
Summary(pt_BR.UTF-8):	Módulo Perl PGP::Sign
Summary(ru.UTF-8):	Модуль для Perl PGP::Sign
Summary(sv.UTF-8):	PGP::Sign Perlmodul
Summary(uk.UTF-8):	Модуль для Perl PGP::Sign
Summary(zh_CN.UTF-8):	PGP::Sign Perl 模块
Name:		perl-PGP-Sign
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d7a461db926dd3d826591562135926df
URL:		http://search.cpan.org/dist/PGP-Sign/
BuildRequires:	gnupg
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gnupg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP::Sign - generates detached PGP signatures for data.

This package was built for using with GnuPG. If you want to use it
with PGP, you need to modify 'Global variables' section in the
PGP/Sign.pm file.

%description -l pl.UTF-8
PGP::Sign - generuje oddzielne sygnatury PGP dla danych.

Ten pakiet został zbudowany do użycia z GnuPG. Jeśli chcesz używać go
z PGP, musisz zmodyfikować sekcję 'Global variables' w pliku
PGP/Sign.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor  \
	PGP=%{_bindir}/gpg \
	PGPSTYLE=GPG

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/PGP
%{_mandir}/man3/*
