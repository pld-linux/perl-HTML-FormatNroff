%include	/usr/lib/rpm/macros.perl
Summary:	FormatNroff perl module
Summary(pl):	Modu� perla FormatNroff
Name:		perl-HTML-FormatNroff
Version:	0.11
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/FormatNroff-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-HTML-Tree
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-FormatNroff formats HTML as nroff man page.

%description -l pl
HTML-FormatNroff formatuje HTML jako stron� man.

%prep
%setup -q -n FormatNroff-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/FormatNroff
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ToDo}.gz

%{perl_sitelib}/HTML/*.pm
%{perl_sitearch}/auto/HTML/FormatNroff

%{_mandir}/man3/*
