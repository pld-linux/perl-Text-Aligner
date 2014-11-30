#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Aligner
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Aligner - justify strings to various alignment styles
Summary(pl.UTF-8):	Text::Aligner - justowanie łańcuchów z różnymi stylami wyrównania
Name:		perl-Text-Aligner
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	73088eaeae1e6c627398db1e7cc76717
URL:		http://search.cpan.org/dist/Text-Aligner/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Justify strings to various alignment styles.

%description -l pl.UTF-8
Justowanie łańcuchów z różnymi stylami wyrównania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%doc README
%{perl_vendorlib}/Text/Aligner.pm
%{_mandir}/man3/*
