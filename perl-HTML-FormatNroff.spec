%include	/usr/lib/rpm/macros.perl
Summary:	FormatNroff perl module
Summary(pl):	Modu³ perla FormatNroff
Name:		perl-HTML-FormatNroff
Version:	0.11
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/FormatNroff-%{version}.tar.gz
# Source0-md5:	62f8fca5c5dd0a4203e7ecea50758190
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-HTML-Tree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::FormatNroff formats HTML as nroff man page.

%description -l pl
HTML::FormatNroff formatuje HTML jako stronê man.

%prep
%setup -q -n FormatNroff-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
