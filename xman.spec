%define	enable_xprint	0

Name: xman
Version: 1.0.3
Release: %mkrel 6
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

Patch3: 0003-Add-bzip2-manpage-extension-support.patch
Patch4: 0004-Add-lzma-manpage-extension-support.patch

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q -n %{name}-%{version}

%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure2_5x	--x-includes=%{_includedir}\
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
