Name:          jajuk
Summary:       Jajuk Advanced Jukebox
Version:       1.4.4
Release:       %mkrel 1
License:       GPL
Group:	       Sound
Source0:       %name-sources-1.4.4.tar.bz2
patch0:	       jajuk-1.4.4-fix-build.patch
URL: 	       http://jajuk.info/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ant
BuildRequires: jfreechart
BuildRequires: jakarta-commons-codec
BuildRequires: vorbisspi
BuildRequires: qdwizard

%description
Jajuk is software that organizes and plays music. 
It is a full-featured application geared towards advanced users 
with large or scattered music collections. Using multiple perspectives, 
the software is designed to be intuitive and provide different ways to 
perform the same task. 

%files 
%defattr(-,root,root)
%_bindir/jajuk
%{_datadir}/applications/mandriva-%{name}.desktop
%_prefix/lib/jajuk/bin/jajuk.jar
%_prefix/lib/jajuk/lib/DEPENDENCIES.txt
%_prefix/lib/jajuk/lib/DERIVATED.txt
%_prefix/lib/jajuk/lib/LICENSE-Apache.txt
%_prefix/lib/jajuk/lib/LICENSE-BSD.txt
%_prefix/lib/jajuk/lib/LICENSE-CREATIVE-COMMONS.txt
%_prefix/lib/jajuk/lib/LICENSE-GPL.txt
%_prefix/lib/jajuk/lib/LICENSE-LGPL.txt
%_prefix/lib/jajuk/lib/linux/*.jar
%_prefix/lib/jajuk/lib/linux/*/*.so
%_prefix/lib/jajuk/lib/linux/x86/libtray.so
%_prefix/lib/jajuk/lib/*.jar
%_prefix/lib/jajuk/bin/jajuk-help.jar
%_prefix/lib/jajuk/bin/jajuk-help_fr.jar
%_iconsdir/jajuk-icon-shortcut_64x64.png

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-src-%version
%patch0 -p0
%__rm -fr lib/jfreechart-1.0.1.jar
ln -s %{_javadir}/jfreechart-1.0.5.jar lib/jfreechart-1.0.5.jar

%__rm -fr lib/commons-codec-1.3.jar
ln -s %{_javadir}/commons-codec-1.3.jar lib/commons-codec-1.3.jar

%__rm -fr lib/vorbisspi-1.0.1.jar
ln -s %{_javadir}/vorbisspi1.0.2.jar lib/vorbisspi1.0.2.jar

%__rm -fr lib/qdwizard-1.9.jar
ln -s %{_javadir}/qdwizard-1.9.jar lib/qdwizard-1.9.jar

%build
cd src/scripts
#%{ant}
ant
%install
install -dm 755 %buildroot%_prefix/lib/jajuk/bin
install -pm 644 build/jajuk/bin/jajuk.jar $RPM_BUILD_ROOT%_prefix/lib/jajuk/bin/jajuk.jar
%__rm -fr build/jajuk/lib/windows
install -dm 755 %buildroot%_prefix/lib/jajuk/lib
mv -f build/jajuk/lib/* $RPM_BUILD_ROOT%_prefix/lib/jajuk/lib/
install -dm 755 %buildroot%_bindir
install -pm 644 build/jajuk/jajuk $RPM_BUILD_ROOT%_bindir

install -pm 644 jajuk-help.jar  $RPM_BUILD_ROOT%_prefix/lib/jajuk/bin/jajuk-help.jar
install -pm 644 jajuk-help_fr.jar $RPM_BUILD_ROOT%_prefix/lib/jajuk/bin/jajuk-help_fr.jar

install -dm 755 %buildroot%_iconsdir
install -pm 644 build/jajuk/jajuk-icon-shortcut_64x64.png $RPM_BUILD_ROOT%_iconsdir

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Jajuk
Comment=Jajuk Advanced Jukebox
Exec=jajuk
Icon=jajuk-icon_64x64
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

%clean
rm -fr %buildroot
