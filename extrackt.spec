%define name extrackt
%define version 0.0.2
%define release %mkrel 1


Summary:	Extrackt is essentially an audio CD ripper and encoder
Name:		%{name}
Version:	%{version}
Release:	%release
License: BSD
Group:		Apllications/Audio
URL: http://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
BuildRequires: edje-devel >= 0.5.0.038, ecore-devel >= 0.9.9.038
BuildRequires: eet-devel >= 0.9.10.038
BuildRequires: evas-devel >= 0.9.9.038
BuildRequires: etk-devel >= 0.1.0.003
BuildRequires: enhance-devel >= 0.0.1
Buildrequires: edje >= 0.5.0.038
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Extrackt is essentially an audio CD ripper and encoder. It allows you to
choose your ripper and encoder based on templates which give Extrackt the
ability to use multiple built in and user defined ones. Extrackt is logically
split into a frontend (gui) and a backend (ripping / encoding / cddb etc.)
and allows for frontends to be written using any toolkit like Etk, Ewl, Gtk,
or even pure Evas / Edje (not to mention ncurses or simlpe shell ones).

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure2_5x
make

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
        needs="X11" \
        section="Multimedia/Audio" \
        title="Extrackt" \
        longtitle="Extrackt CD ripper and encoder" \
        command="%{_bindir}/%name" \
        icon="%name.png" \
        startup_notify="true" \
        xdg="true"
EOF

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
%doc AUTHORS ChangeLog COPYING* INSTALL README
%{_bindir}/%{name}
