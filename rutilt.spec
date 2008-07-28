%define name rutilt
%define oname RutilT
%define version 0.16
%define distname %{oname}v%{version}
%define release %mkrel 3

Summary: Wireless configuration utility
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://cbbk.free.fr/bonrom/files/%{distname}.tar.gz
License: GPL
Group: Networking/Other
Url: http://cbbk.free.fr/bonrom/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel kernel-source

%description
RutilT is a Gtk+2 utility for Linux that helps you configure your
wireless devices. Although primarily written for the rt2x00 project,
it is designed to work with any device.

%prep
%setup -q -n %{distname}

%build
./configure.sh --kernel_sources=%{_prefix}/src/linux --prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_bindir}/%{name}_helper
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}*
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/*.png
%{_datadir}/apps/%{name}/set_ip.sh
%{_iconsdir}/hicolor/*/apps/%{name}.png
