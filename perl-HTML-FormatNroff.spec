%include	/usr/lib/rpm/macros.perl
Summary:	FormatNroff - format HTML as nroff man page
Summary(pl):	FormatNroff - formatowanie HTML-u jako strony podrêcznika man w nroff-ie
Name:		perl-HTML-FormatNroff
Version:	0.11
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/FormatNroff-%{version}.tar.gz
# Source0-md5:	62f8fca5c5dd0a4203e7ecea50758190
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-HTML-Tree
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::FormatNroff Perl mudule is a formatter that outputs nroff
source for the nroff text processor, using man macros, and tbl
commands for table processing.

%description -l pl
Modu³ Perla HTML::FormatNroff formatuje ¼ród³o w HTML-u wyprowadzaj±c
wynik w postaci ¼ródla dla procesora tekstu nroff. U¿ywa makr mana, a
do przetwarzania tabel - poleceñ tbl

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
