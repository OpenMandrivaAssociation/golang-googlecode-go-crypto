# https://github.com/golang/crypto
%global forgeurl        https://github.com/golang/crypto
%global goipath         golang.org/x/crypto
%global commit          e84da0312774c21d64ee2317962ef669b27ffb41
%global x_name          golang-golangorg-crypto

%gometa

Name:           golang-googlecode-go-crypto
Version:        0
Release:        0.26%{?dist}
Summary:        Supplementary Go cryptography libraries
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package -n %{x_name}-devel
Summary:       %{summary}

BuildRequires: golang(golang.org/x/sys/cpu)
BuildRequires: golang(golang.org/x/sys/unix)

%description -n %{x_name}-devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%install
%goinstall

%check
%gochecks # -d chacha20poly1305 -d ocsp -d ssh

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files -n %{x_name}-devel -f devel.file-list
%license LICENSE
%doc *.md AUTHORS CONTRIBUTORS

%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.26.20181026gite84da03
- Bump to commit e84da0312774c21d64ee2317962ef669b27ffb41

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.25.gita49355c
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Sun Aug 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.24.gita49355c
- Rebuild to accomodate golist rebuild
  resolves: #1615497

* Mon Jul 16 2018 Steve Miller (copart) <code@rellims.com> - 0-0.23.gita49355c
- Bump to upstream a49355c7e3f8fe157a85be2f77e6e269a0f89602

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.git88942b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.21.20180324git9419663
- Bump to upstream 88942b9c40a4c9d203b82b3731787b672d6e809b

* Tue Mar 06 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.20.git9419663
- Bump to upstream 9419663f5a44be8b34ca85f08abc5fe1be11f8a3

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.20170329gite4e2799
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gite4e2799
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gite4e2799
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gite4e2799
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gite4e2799
- Bump to upstream e4e2799dd7aab89f583e1d898300d96367750991
  resolves: #1474536

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git81372b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git81372b2
- Bump to upstream 81372b2fc2f10bef2a7f338da115c315a56b2726
  related: #1231618

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitc10c31b
- Polish the spec file
  related: #1231618

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.gitc10c31b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.gitc10c31b
- Bump to upstream c10c31b5e94b6f7a0283272dc2bb27163dcea24b
  related: #1231618

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitc57d4a7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.gitc57d4a7
- Fix sed for import path
  related: #1231618

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitc57d4a7
- Choose the correct devel subpackage
  related: #1231618

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitc57d4a7
- Update spec file to spec-2.0
  related: #1231618

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitc57d4a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git%{shortcommit}
- Repository has moved to github.com/golang/crypto, updating spec file accordingly
  resolves: #1231618

* Sun Dec 14 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hg69e2a90ed92d
- Correct Source0 URL
- Correct paths for golang.org/x/crypto/*

* Thu Dec 04 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.hg69e2a90ed92d
- First package for Fedora
  resolves: #1148704
