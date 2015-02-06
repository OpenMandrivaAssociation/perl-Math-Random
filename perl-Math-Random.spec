%define upstream_name    Math-Random
%define upstream_version 0.71

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:    Random Number Generators
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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



%changelog
* Tue Jan 24 2012 Stéphane Téletchéa <steletch@mandriva.org> 0.710.0-3
+ Revision: 768089
- Convert to new rpm numbering scheme
- Rebuild for new perl

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-2mdv2011.0
+ Revision: 555264
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.710.0-1mdv2010.0
+ Revision: 401633
- rebuild using %%perl_convert_version
- fixed license field

* Tue Feb 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.71-1mdv2009.1
+ Revision: 342095
- import perl-Math-Random


* Tue Feb 17 2009 cpan2dist 0.71-1mdv
- initial mdv release, generated with cpan2dist

