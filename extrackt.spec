%define name extrackt
%define version 0.0.2
%define release %mkrel 4


Summary:	Essentially an audio CD ripper and encoder
Name:		%{name}
Version:	%{version}
Release:	%release
License: BSD
Group:		Sound
URL: http://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
Source1:	extrackt.desktop
BuildRequires: edje-devel >= 0.5.0.038, ecore-devel >= 0.9.9.041
BuildRequires: eet-devel >= 0.9.10.041
BuildRequires: evas-devel >= 0.9.9.041
BuildRequires: etk-devel >= 0.1.0.003
BuildRequires: enhance-devel >= 0.0.1
Buildrequires: edje >= 0.5.0.038
BuildRequires: ImageMagick
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
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Audio" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

mkdir -p %buildroot{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 data/images/extrackt_icon.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/extrackt_icon.png %buildroot%_iconsdir/%name.png
convert -resize 16x16 data/images/extrackt_icon.png %buildroot%_miconsdir/%name.png


mkdir -p %buildroot%{_datadir}/pixmaps
cp data/images/extrackt_icon.png %buildroot%{_datadir}/pixmaps/%name.png

%post 
%{update_menus} 

%postun 
%{clean_menus} 


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS INSTALL README
%{_bindir}/%{name}
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png
%_datadir/pixmaps/*.png
%{_datadir}/applications/*
%{_datadir}/%name
