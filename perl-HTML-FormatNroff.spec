%include	/usr/lib/rpm/macros.perl
Summary:	FormatNroff perl module
Summary(pl):	Modu³ perla FormatNroff
Name:		perl-HTML-FormatNroff
Version:	0.11
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/FormatNroff-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-FormatNroff formats HTML as nroff man page.

%description -l pl
HTML-FormatNroff formatuje HTML jako stronê man.

%prep
%setup -q -n FormatNroff-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/*.pm
%{_mandir}/man3/*
