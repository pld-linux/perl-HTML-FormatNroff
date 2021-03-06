%define		pdir	HTML
%define		pnam	FormatNroff
Summary:	FormatNroff - format HTML as nroff man page
Summary(pl.UTF-8):	FormatNroff - formatowanie HTML-u jako strony podręcznika man w nroff-ie
Name:		perl-HTML-FormatNroff
Version:	0.11
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/FormatNroff-%{version}.tar.gz
# Source0-md5:	62f8fca5c5dd0a4203e7ecea50758190
URL:		http://search.cpan.org/dist/HTML-FormatNroff/
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::FormatNroff Perl module is a formatter that outputs nroff
source for the nroff text processor, using man macros, and tbl
commands for table processing.

%description -l pl.UTF-8
Moduł Perla HTML::FormatNroff formatuje źródło w HTML-u wyprowadzając
wynik w postaci źródła dla procesora tekstu nroff. Używa makr mana, a
do przetwarzania tabel - poleceń tbl

%prep
%setup -q -n FormatNroff-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
