%define	enable_xprint 0

Name: xman
Version: 1.1.4
Release: 1
Summary: Manual page display program for the X Window System
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

# Not really required, but configure checks for /etc/man.config
# to know if should or not use it.
BuildRequires: man
BuildRequires: xaw-devel >= 1.0.1
%if %{enable_xprint}
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: pkgconfig(xp) >= 1.0.0
%endif
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q

%build
%global optflags %{optflags} -Wno-error -Wno-tautological-pointer-compare
%configure \
%if %{enable_xprint}
		--enable-xprint
%else
		--disable-xprint
%endif
%make

%install
%makeinstall_std

%files
%{_bindir}/xman
%{_datadir}/X11/xman.help
%{_datadir}/X11/app-defaults/Xman
%{_mandir}/man1/xman.*
