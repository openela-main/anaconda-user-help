Summary:          Content for the Anaconda built-in help system
Name:             anaconda-user-help
URL:              https://access.redhat.com/documentation
Version:          8.8.3
Release:          1%{?dist}.openela.0.3
Epoch:            1
BuildArch:        noarch

# The tarball is created from the Installation Guide
# git repository with git archive from the corresponding
# anaconda-user-help-x.x.x git tag.

Source0:          %{name}-%{version}.tar.gz

Patch1:           0001-Debrand-Anaconda-help-screen.patch

License:          CC-BY-SA

%description
This package provides content for the Anaconda built-in help system.

%prep
%setup -q
%patch1 -p1

%install
mkdir -p %{buildroot}%{_datadir}/anaconda/help
cp -r * %{buildroot}%{_datadir}/anaconda/help/

%files
%{_datadir}/anaconda/help/*

%changelog
* Thu Jan 25 2024 Release Engineering <releng@openela.org> - 8.8.3.openela.0.3
- Move, rename, brand files for OpenELA

* Tue Feb 14 2023 Martin Kolman <mkolman@redhat.com> - 8.8.3-1
- fix anchor files
  Related: rhbz#1949071

* Thu Feb 02 2023 Martin Kolman <mkolman@redhat.com> - 8.8.2-1
- fix anchor files
  Related: rhbz#1949071

* Tue Jan 24 2023 Martin Kolman <mkolman@redhat.com> - 8.8.1-1
- update help content for RHEL 8.8
  Resolves: rhbz#1949071

* Fri Aug 19 2022 Martin Kolman <mkolman@redhat.com> - 8.7.1-1
- update help content for RHEL 8.7
  Resolves: rhbz#1949071

* Fri Sep 4 2020 Martin Kolman <mkolman@redhat.com> - 8.3.3-1
- add missing help content for installation progress screen
  Related: rhbz#1861374

* Fri Aug 21 2020 Martin Kolman <mkolman@redhat.com> - 8.3.1-1
- update help content for RHEL 8.3
  Resolves: rhbz#1861374

* Fri Feb 21 2020 Martin Kolman <mkolman@redhat.com> - 8.2.3-1
- final help content fixes for 8.2 GA
  Related: rhbz#1788855

* Wed Feb 12 2020 Martin Kolman <mkolman@redhat.com> - 8.2.2-1
- post 8.2 Beta help content fixes
  Related: rhbz#1788855

* Mon Jan 27 2020 Martin Kolman <mkolman@redhat.com> - 8.2.1-1
- initial help content update for RHEL 8.2
- add help content for the "Connect to Red Hat" spoke
- drop content for the superseded "System Purpose" spoke
  Resolves: rhbz#1788855

* Mon Jan 28 2019 Martin Kolman <mkolman@redhat.com> - 8.1.1-1
- initial help content update for RHEL 8.1
  Related: rhbz#1715415

* Mon Jan 28 2019 Martin Kolman <mkolman@redhat.com> - 8.0.9-1
- fix broken links
  Related: rhbz#1668443

* Tue Dec 11 2018 Martin Kolman <mkolman@redhat.com> - 8.0.7-1
- remove remaining Fedora references
  Related: rhbz#1644240

* Tue Oct 16 2018 Martin Kolman <mkolman@redhat.com> - 8.0.6-1
- update help content for RHEL8 Beta
  Related: rhbz#1634756

* Mon Oct 15 2018 Martin Kolman <mkolman@redhat.com> - 8.0.4-1
- update help content for RHEL8 Beta
  Related: rhbz#1634756

* Thu Oct 11 2018 Martin Kolman <mkolman@redhat.com> - 8.0.3-1
- update help content for RHEL8 Beta
  Related: rhbz#1634756

* Fri Oct 05 2018 Martin Kolman <mkolman@redhat.com> - 8.0.2-1
- add initial RHEL8 help content
  Resolves: rhbz#1634756
- adapt spec file to new help content
  Related: rhbz#1634756

* Wed Aug 01 2018 Martin Kolman <mkolman@redhat.com> - 8.0.1-1
- fix version for RHEL
- add RHEL help placeholders instead of help content for now

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Martin Kolman <mkolman@redhat.com> - 26.1-4
- Add help for blivet-gui spoke (#1439565) (vtrefny)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Martin Kolman <mkolman@redhat.com> - 26.1-2
- Add lynx dependency to fix xml to plain text conversion (mkolman)

* Thu Oct 27 2016 Martin Kolman <mkolman@redhat.com> - 26.1-1
- Generate plain text variants of the help content files (mkolman)
- Add a plain text version of of the placeholder (mkolman)
- Fix some typos (mkolman)
- Use /usr/bin/python3 in conversion script header (mkolman)
- Update help content (mkolman)
- Fix link to the installation guide git repository (mkolman)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Martin Kolman <mkolman@redhat.com> - 22.4-1
- Add help content for the Kdump spoke (mkolman)

* Wed Dec 10 2014 Martin Kolman <mkolman@redhat.com> - 22.1-1
- Initial release (mkolman)
