%include	/usr/lib/rpm/macros.perl
Summary:	PGP-Sign perl module
Summary(pl):	Modu³ perla PGP-Sign
Name:		perl-PGP-Sign
Version:	0.16
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/PGP/PGP-Sign-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	gnupg
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	gnupg
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PGP-Sign - generates detached PGP signatures for data.

This package was built for using with GnuPG. If you want to use it with
PGP, you need to modify 'Global variables' section in the PGP/Sign.pm file.

%description -l pl
PGP-Sign - generuje oddzielne sygnatury PGP dla danych.

Ten pakiet zosta³ zbudowany do u¿ycia z GnuPG. Je¶li chcesz u¿ywaæ go
z PGP, musisz zmodyfikowaæ sekcjê 'Global variables' w pliku PGP/Sign.pm.

%prep
%setup -q -n PGP-Sign-%{version}

%build
perl Makefile.PL \
	PGP=/usr/bin/gpg \
	PGPSTYLE=GPG
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PGP/Sign
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz

%{perl_sitelib}/PGP/Sign.pm
%{perl_sitearch}/auto/PGP/Sign

%{_mandir}/man3/*
