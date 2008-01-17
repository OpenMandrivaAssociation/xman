%define	enable_xprint	0

Name: xman
Version: 1.0.3
Release: %mkrel 4
Summary: Manual page display program for the X Window System
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xman xorg/app/xman
# cd xorg/app/xman
# git-archive --format=tar --prefix=xman-1.0.3/ xman-1.0.3 | bzip2 -9 > xman-1.0.3.tar.bz2
########################################################################
Source: %{name}-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xman-1.0.3..origin/mandriva+custom
Patch1: 0001-Allow-xman-to-be-cross-build-by-adding-a-.-configure.patch
Patch2: 0002-Replace-static-ChangeLog-with-dist-hook-to-generate.patch
Patch3: 0003-Add-bzip2-manpage-extension-support.patch
Patch4: 0004-Add-lzma-manpage-extension-support.patch
########################################################################

BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros		>= 1.1.5
# Not really required, but configure checks for /etc/man.config
# to know if should or not use it.
BuildRequires: man
BuildRequires: libxaw-devel		>= 1.0.4
%if %{enable_xprint}
BuildRequires: libxprintutil-devel	>= 1.0.1
%endif

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
%if %{enable_xprint}
		--enable-xprint\
%else
		--disable-xprint\
%endif
		--x-libraries=%{_libdir}

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
