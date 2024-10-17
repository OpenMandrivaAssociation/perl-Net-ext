%define upstream_name       Net-ext
%define upstream_version    1.011

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5
Summary:    Net-ext module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
# http://rt.cpan.org/Public/Bug/Display.html?id=43071
Patch:      Net-ext-fix-segfault.patch
BuildRequires:	perl-devel
#BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net-ext module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/*/*



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.11.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.11.0-2mdv2011.0
+ Revision: 556018
- rebuild for perl 5.12

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.0-1mdv2010.0
+ Revision: 438679
- use new perl_version macro
- fix 5.10 compatibility (RT patch)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.011-4mdv2008.0
+ Revision: 25449
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.011-3mdv2008.0
+ Revision: 25278
- rebuild


* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.011-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.011-1mdk
- initial Mandriva package

