
%define realname   Math-Random
%define version    0.71
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Random Number Generators
Source:     http://www.cpan.org/modules/by-module/Math/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel




%description
*Math::Random* is a *Perl* port of the *C* version of *randlib*, which is a
suite of routines for generating random deviates. See the "RANDLIB" manpage
for more information.

This port supports all of the distributions from which the *Fortran* and
*C* versions generate deviates. The major functionalities that are excluded
are the multiple generators/splitting facility and antithetic random number
generation. These facilities, along with some of the distributions which
_are_ included, are probably not of interest except to the very
sophisticated user. If there is sufficient interest, the excluded
facilities will be included in a future release. The code to perform the
excluded facilities is available as *randlib* in *Fortran* and *C* source.

Default Routines
    The routines which are exported by default are the only ones that the
    average Perl programmer is likely to need.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README README
%{_mandir}/man3/*
%perl_vendorlib/*


