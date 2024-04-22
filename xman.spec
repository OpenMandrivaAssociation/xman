%define enable_xprint 0

Name: xman
Version: 1.2.0
Release: 1
Summary: Manual page display program for the X Window System
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
Source: https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

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
%autosetup -p1

%build
%global optflags %{optflags} -Wno-error -Wno-tautological-pointer-compare
%configure \
%if %{enable_xprint}
		--enable-xprint
%else
		--disable-xprint
%endif
%make_build

%install
%make_install

%files
%{_bindir}/xman
%{_datadir}/X11/xman.help
%{_datadir}/X11/app-defaults/Xman
%doc %{_mandir}/man1/xman.*
