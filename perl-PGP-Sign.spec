%define	pdir	PGP
%define	pnam	Sign
%include	/usr/lib/rpm/macros.perl
Summary:	PGP-Sign perl module
Summary(pl):	Modu³ perla PGP-Sign
Name:		perl-PGP-Sign
Version:	0.16
Release:	6

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	gnupg
Requires:	gnupg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP-Sign - generates detached PGP signatures for data.

This package was built for using with GnuPG. If you want to use it
with PGP, you need to modify 'Global variables' section in the
PGP/Sign.pm file.

%description -l pl
PGP-Sign - generuje oddzielne sygnatury PGP dla danych.

Ten pakiet zosta³ zbudowany do u¿ycia z GnuPG. Je¶li chcesz u¿ywaæ go
z PGP, musisz zmodyfikowaæ sekcjê 'Global variables' w pliku
PGP/Sign.pm.

%prep
%setup -q -n PGP-Sign-%{version}

%build
perl Makefile.PL \
	PGP=%{_bindir}/gpg \
	PGPSTYLE=GPG
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/PGP/Sign.pm
%{_mandir}/man3/*
