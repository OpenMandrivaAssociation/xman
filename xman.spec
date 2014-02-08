%define	enable_xprint	0

Name: xman
Version: 1.1.2
Release: 2
Summary: Manual page display program for the X Window System
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-root

# Not really required, but configure checks for /etc/man.config
# to know if should or not use it.
BuildRequires: man
BuildRequires: libxaw-devel >= 1.0.1
%if %{enable_xprint}
BuildRequires: libxprintutil-devel >= 1.0.1
-BuildRequires: libxp-devel >= 1.0.0
%endif
BuildRequires: x11-util-macros >= 1.0.1

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
%if %{enable_xprint}
		--enable-xprint
%else
		--disable-xprint
%endif
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xman
%{_datadir}/X11/xman.help
%{_datadir}/X11/app-defaults/Xman
%{_mandir}/man1/xman.*


%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 699281
- update to new version 1.1.2

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 671342
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 592500
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464744
- New version: 1.1.0
  Lzma and bzip2 patches integrated upstream

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.3-7mdv2009.1
+ Revision: 366706
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-6mdv2009.0
+ Revision: 226062
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-5mdv2008.1
+ Revision: 166687
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-4mdv2008.1
+ Revision: 154425
- Updated BuildRequires and resubmit package.
  Switched to store patches in git repository (in branch mandriva+custom),
  and extract tarball with git-archive.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1.0.3-3mdv2008.1
+ Revision: 106450
- rebuild for new lzma

* Mon Oct 29 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 103565
- Add lzma support and defaults to no xprint support.

* Fri Aug 10 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 61656
- fix man extension
- new release


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:09:36 (59517)
- rebuild to fix libXaw.so.8 dependency

* Tue Jun 06 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-06 19:37:48 (36717)
- added patch: support man pages compressed using bzip2

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:34:52 (31402)
- fill in more missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

