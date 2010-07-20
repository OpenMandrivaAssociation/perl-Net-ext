%define upstream_name       Net-ext
%define upstream_version    1.011

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Summary:    Net-ext module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
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

