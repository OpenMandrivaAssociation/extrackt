%define name extrackt
%define version 0.0.2
%define release %mkrel 8

Summary:	Essentially an audio CD ripper and encoder
Name:		%{name}
Version:	%{version}
Release:	%release
License: BSD
Group:		Sound
URL: http://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
BuildRequires: edje-devel >= 0.9.9.050, ecore-devel >= 0.9.9.050
BuildRequires: eet-devel >= 1.1.0
BuildRequires: evas-devel >= 0.9.9.050
BuildRequires: etk-devel >= 0.1.0.042
BuildRequires: enhance-devel >= 0.0.1
Buildrequires: edje >= 0.9.9.050
BuildRequires: imagemagick
BuildRequires: desktop-file-utils
Requires: vorbis-tools, cdparanoia
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Extrackt is essentially an audio CD ripper and encoder. It allows you to
choose your ripper and encoder based on templates which give Extrackt the
ability to use multiple built in and user defined ones. Extrackt is logically
split into a frontend (gui) and a backend (ripping / encoding / cddb etc.)
and allows for frontends to be written using any toolkit like Etk, Ewl, Gtk,
or even pure Evas / Edje (not to mention ncurses or simlpe shell ones).

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS INSTALL README
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/extrackt.png
%{_datadir}/%name
