#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PAR
%define	pnam	Packer
Summary:	PAR::Packer - PAR Packager
#Summary(pl.UTF-8):	
Name:		perl-PAR-Packer
Version:	0.982
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f78dcc541758efca6f3c3b98e1124ae
URL:		http://search.cpan.org/dist/PAR-Packer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Archive-Zip >= 1
BuildRequires:	perl-Getopt-ArgvFile >= 1.07
BuildRequires:	perl-Module-ScanDeps >= 0.78
BuildRequires:	perl-PAR >= 0.977
BuildRequires:	perl-PAR-Dist >= 0.22
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the App::Packer::Backend interface, for generating
stand-alone executables, perl scripts and PAR files.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/PAR/*
%{perl_vendorlib}/App/Packer/*
%{_mandir}/man?/*
