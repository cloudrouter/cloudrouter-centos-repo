%define cr_display_name CloudRouter
%define cr_name cloudrouter
%define cr_version 4
%define cr_gpg_key RPM-GPG-KEY-CLOUDROUTER-PRIMARY

%define base_display_name CentOS 7
%define base_name centos

Summary:	%{cr_display_name} repository files for %{base_display_name}
Name:		%{cr_name}-%{base_name}-repo
Version:	%{cr_version}
Release:	1
License:	AGPLv3
Group:		System Environment/Base
Source0:	%{cr_name}.repo
Source1:	%{cr_gpg_key}
BuildArch:	noarch
Provides:   cloudrouter-repo
Conflicts:  %{cr_name}-release-%{base_name}


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
* Mon Oct 10 2016 John Siegrist <john@complects.com> - 4-1
- Updated the version for CRv4.

* Wed Mar 30 2016 John Siegrist <john@complects.com> - 3-2
- Updated the CRv3 Repo URL back to the old scheme.

* Wed Dec 30 2015 John Siegrist <john@complects.com> - 3-1
- Updated the version for CRv3.

* Tue Sep 01 2015 John Siegrist <john@complects.com> - 2-4
- Added dependency on epel-release so the CloudRouter dependencies in EPEL7 are accessible.

* Thu Aug 27 2015 John Siegrist <john@complects.com> - 2-3
- Added support for virtual package "cloudrouter-repo".

* Fri Aug 14 2015 John Siegrist <john@complects.com> - 2-2
- Fixed GPG key verification for RPMs downloaded from the CloudRouter repository.

* Mon Aug 10 2015 John Siegrist <jsiegrist@iix.net> - 2-1
- Initial commit of the CentOS-specific CloudRouter after splitting the cloudrouter-repo project into separate ones for Fedora and CentOS.
