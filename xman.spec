Name: xman
Version: 1.0.3
Release: %mkrel 1
Summary: Manual page display program for the X Window System
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# Fix xman to work with bzipped pages
Patch0: xman-1.0.2-bzip2_support.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xman is a manual page display program for the X Window System.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .bzip2

%build
%configure2_5x	--x-includes=%{_includedir}\
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


