%define real_name Net-ext

Summary:	Net-ext module for perl 
Name:		perl-%{real_name}
Version:	1.011
Release: %mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
#BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net-ext module for perl

%prep
%setup -q -n %{real_name}-%{version} 

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
%dir %{perl_vendorlib}/*/auto/Net/Gen
%dir %{perl_vendorlib}/*/auto/Net/UNIX
%dir %{perl_vendorlib}/*/auto/Net/Inet
%dir %{perl_vendorlib}/*/auto/Net/UDP
%{perl_vendorlib}/*/auto/Net/Gen/*
%{perl_vendorlib}/*/auto/Net/UNIX/*
%{perl_vendorlib}/*/auto/Net/Inet/*
%{perl_vendorlib}/*/auto/Net/UDP/*
%{perl_vendorlib}/*/Net/*.pm
%dir %{perl_vendorlib}/*/Net/UNIX
%dir %{perl_vendorlib}/*/Net/TCP
%{perl_vendorlib}/*/Net/UNIX/*
%{perl_vendorlib}/*/Net/TCP/*
%{_mandir}/*/*

