%include	/usr/lib/rpm/macros.perl
Summary:	PGP-Sign perl module
Summary(pl):	Modu� perla PGP-Sign
Name:		perl-PGP-Sign
Version:	0.16
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PGP/PGP-Sign-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	gnupg
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGP-Sign - generates detached PGP signatures for data.

This package was built for using with GnuPG. If you want to use it
with PGP, you need to modify 'Global variables' section in the
PGP/Sign.pm file.

%description -l pl
PGP-Sign - generuje oddzielne sygnatury PGP dla danych.

Ten pakiet zosta� zbudowany do u�ycia z GnuPG. Je�li chcesz u�ywa� go
z PGP, musisz zmodyfikowa� sekcj� 'Global variables' w pliku
PGP/Sign.pm.

%prep
%setup -q -n PGP-Sign-%{version}

%build
perl Makefile.PL \
	PGP=/usr/bin/gpg \
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
%doc {ChangeLog,README,TODO}.gz

%{perl_sitelib}/PGP/Sign.pm
%{perl_sitearch}/auto/PGP/Sign

%{_mandir}/man3/*
