#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	PAR
%define	pnam	Packer
Summary:	PAR::Packer - PAR Packager
#Summary(pl.UTF-8):	
Name:		perl-PAR-Packer
Version:	1.045
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PAR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a3333754b0112ee8fe80083042b89a3b
Patch0:		x32.patch
URL:		http://search.cpan.org/dist/PAR-Packer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Archive-Zip >= 1
BuildRequires:	perl-Getopt-ArgvFile >= 1.07
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-Module-ScanDeps >= 0.78
BuildRequires:	perl-PAR >= 1.014
BuildRequires:	perl-PAR-Dist >= 0.22
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
This module implements the App::Packer::Backend interface, for generating
stand-alone executables, perl scripts and PAR files.

# %description -l pl.UTF-8
# TODO

%package tkpp
Summary:	tkpp - frontend to pp written in Perl/Tk
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description tkpp
Tkpp is a GUI frontend to pp, which can turn perl scripts into stand-alone
PAR files, perl scripts or executables.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1 \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/{,par-}pp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/par*
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/PAR/*
%{perl_vendorlib}/App/Packer/*
%{_mandir}/man3/*
%{_mandir}/man1/p*

%files tkpp
%attr(755,root,root) %{_bindir}/tkpp
%{_mandir}/man1/tkpp*
