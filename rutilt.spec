%define name rutilt
%define oname RutilT
%define version 0.14
%define distname %{oname}v%{version}
%define release %mkrel 1

Summary: Wireless configuration utility
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://cbbk.free.fr/bonrom/
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

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}_helper
%{_datadir}/%{name}/set_ip.sh
