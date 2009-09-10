Name:          jajuk
Summary:       Jajuk Advanced Jukebox
Version:       1.8.1
Release:       %mkrel 3
License:       GPL
Group:	       Sound
Source0:       %name-sources-%version.zip
patch0:	       jajuk-1.7.3-fix-build.patch
URL: 	       http://jajuk.info/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
#BuildArch:     noarch

BuildRequires: ant
BuildRequires: jfreechart = 1.0.11
BuildRequires: jakarta-commons-codec = 1.3
BuildRequires: vorbisspi = 1.0.2
#BuildRequires: qdwizard = 1.9
BuildRequires: jakarta-commons-logging = 1.1
BuildRequires: jakarta-commons-collections = 3.2.1
BuildRequires: jlayer = 1.0

Requires:      jfreechart = 1.0.11
Requires:      jakarta-commons-codec = 1.3
Requires:      vorbisspi = 1.0.2
#Requires:      qdwizard = 2.1
Requires:      jakarta-commons-logging = 1.1
Requires:      jakarta-commons-collections = 3.2.1
Requires:      jlayer = 1.0

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
%_datadir/jajuk/bin/jajuk.jar
%_datadir/jajuk/lib/DEPENDENCIES.txt
%_datadir/jajuk/lib/DERIVATED.txt
%_datadir/jajuk/lib/LICENSE-Apache.txt
%_datadir/jajuk/lib/LICENSE-BSD.txt
%_datadir/jajuk/lib/LICENSE-CREATIVE-COMMONS.txt
%_datadir/jajuk/lib/LICENSE-GPL.txt
%_datadir/jajuk/lib/LICENSE-LGPL.txt
%if "lib" == "lib64"
%exclude %_datadir/jajuk/lib/lib32/libunix-java.so
%else
%exclude %_datadir/jajuk/lib/lib64/libunix-java.so
%endif
%exclude %_datadir/jajuk/lib/JIntellitype.dll
%_datadir/jajuk/lib/*.jar
%_iconsdir/jajuk-icon-shortcut_64x64.png

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-src-%version
%patch0 -p1
%__rm -fr lib/jfreechart-1.0.1.jar
ln -s %{_javadir}/jfreechart-1.0.11.jar lib/jfreechart-1.0.11.jar

%__rm -fr lib/commons-codec-1.3.jar
ln -s %{_javadir}/commons-codec-1.3.jar lib/commons-codec-1.3.jar

%__rm -fr lib/vorbisspi-1.0.1.jar
ln -s %{_javadir}/vorbisspi1.0.2.jar lib/vorbisspi1.0.2.jar

#%__rm -fr lib/qdwizard-1.9.jar
#ln -s %{_javadir}/qdwizard-1.9.jar lib/qdwizard-1.9.jar

%__rm -fr lib/commons-logging-1.0.jar
ln -s %{_javadir}/commons-logging-1.1.jar lib/commons-logging-1.1.jar

%__rm -fr lib/commons-collections-3.2.jar
ln -s %{_javadir}/commons-collections-3.2.1.jar lib/commons-collections-3.2.1.jar

%__rm -fr lib/jlayer-1.0.jar
ln -s %{_javadir}/jlayer-1.0.jar lib/jlayer-1.0.jar

%build
cd src/scripts
ant

%install
install -dm 755 %buildroot%_datadir/jajuk/bin
install -pm 644 build/jajuk/bin/jajuk.jar $RPM_BUILD_ROOT%_datadir/jajuk/bin/jajuk.jar
%__rm -fr build/jajuk/lib/windows
install -dm 755 %buildroot%_datadir/jajuk/lib
mv -f build/jajuk/lib/* $RPM_BUILD_ROOT%_datadir/jajuk/lib/
install -dm 755 %buildroot%_bindir
install -pm 644 build/jajuk/jajuk $RPM_BUILD_ROOT%_bindir

install -dm 755 %buildroot%_iconsdir
install -pm 644 build/jajuk/jajuk-icon-shortcut_64x64.png $RPM_BUILD_ROOT%_iconsdir

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Jajuk
Comment=Jajuk Advanced Jukebox
Exec=jajuk
Icon=jajuk-icon-shortcut_64x64
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

%clean
rm -fr %buildroot
