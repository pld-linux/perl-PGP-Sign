#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
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
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/R/RR/RRA/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94427ecdc22d2137654318331622d0bc
URL:		https://metacpan.org/dist/PGP-Sign
BuildRequires:	gnupg
BuildRequires:	perl-Module-Build >= 0.28
BuildRequires:	perl-devel >= 1:5.20
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run
%endif
Requires:	gnupg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP::Sign - generates detached PGP signatures for data.

This module works with GnuPG only.

%description -l pl.UTF-8
PGP::Sign - generuje oddzielne sygnatury PGP dla danych.

Ten moduł działa wyłącznie z GnuPG.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor \
	--destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/PGP
%{_mandir}/man3/*
