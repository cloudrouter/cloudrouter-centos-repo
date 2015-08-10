%define cr_display_name CloudRouter
%define cr_name cloudrouter
%define cr_version 2

%define base_display_name CentOS 7
%define base_name centos
%define base_version 7

Summary:	%{cr_display_name} repository files for %{base_display_name}
Name:		%{cr_name}-%{base_name}-repo
Version:	%{cr_version}
Release:	1
License:	AGPLv3
Group:		System Environment/Base
Source0:	%{cr_name}.repo
Source1:	RPM-GPG-KEY-%{cr_name}-%{cr_version}-primary
BuildArch:	noarch
Conflicts:	%{cr_name}-%{base_name}-release

%description
%{cr_display_name} repository files for %{base_display_name}.

%prep
%setup -q  -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -dm 755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Install repo
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Mon Aug 10 2015 John Siegrist <jsiegrist@iix.net> - 2-1
- Initial commit of the CentOS-specific CloudRouter after splitting the cloudrouter-repo project into separate ones for Fedora and CentOS.
