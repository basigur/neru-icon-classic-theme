Name:			neru-classic-icon
Version:		2.9
Release:         	1
Summary:         	Classic theme icons Neru fork
Group:           	Graphical desktop/Other
License:         	LGPLv3
URL:             	https://github.com/basigur/neru-icon-classic-theme/
Source0:         	https://github.com/basigur/neru-icon-classic-theme/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
BuildArch:       	noarch
Requires(post):		gtk-update-icon-cache


%description
%{summary} by basigur & RamilSadrlimanov@ro_spo.


%prep
%setup -qn neru-icon-classic-theme-%{version}


%build


%install
find . -type f -exec chmod 0644 {} \;
find . -type d -exec chmod 0755 {} \;
install -d %{buildroot}%{_datadir}/icons
cp -R neru*classic/ %{buildroot}%{_datadir}/icons/


%files
%defattr(-,root,root)
%{_datadir}/icons/neru-dark-classic
%{_datadir}/icons/neru-dark-black-classic
%{_datadir}/icons/neru-dark-brown-classic
%{_datadir}/icons/neru-dark-cyan-classic
%{_datadir}/icons/neru-dark-grey-classic
%{_datadir}/icons/neru-dark-green-classic
%{_datadir}/icons/neru-dark-magenta-classic
%{_datadir}/icons/neru-dark-orange-classic
%{_datadir}/icons/neru-dark-pink-classic
%{_datadir}/icons/neru-dark-red-classic
%{_datadir}/icons/neru-dark-yellow-classic
%{_datadir}/icons/neru-light-classic
%{_datadir}/icons/neru-light-black-classic
%{_datadir}/icons/neru-light-brown-classic
%{_datadir}/icons/neru-light-cyan-classic
%{_datadir}/icons/neru-light-grey-classic
%{_datadir}/icons/neru-light-green-classic
%{_datadir}/icons/neru-light-magenta-classic
%{_datadir}/icons/neru-light-orange-classic
%{_datadir}/icons/neru-light-pink-classic
%{_datadir}/icons/neru-light-red-classic
%{_datadir}/icons/neru-light-yellow-classic
%{_datadir}/icons/neru-classic
%doc AUTHORS README.md
%license LICENSE


%post
 for _color in black brown cyan grey green magenta orange pink red yellow
   do
gtk-update-icon-cache -q /usr/share/icons/neru-light-"${_color}"-classic
gtk-update-icon-cache -q /usr/share/icons/neru-dark-"${_color}"-classic
gtk-update-icon-cache -q /usr/share/icons/neru-light-classic
gtk-update-icon-cache -q /usr/share/icons/neru-dark-classic
gtk-update-icon-cache -q /usr/share/icons/neru-classic
   done



%preun
if [ $1 -eq 0 ]; then
 for _color in black brown cyan grey green magenta orange pink red yellow
   do
rm -f /usr/share/icons/neru-light-"${_color}"-classic/icon-theme.cache
rm -f /usr/share/icons/neru-dark-"${_color}"-classic/icon-theme.cache
rm -f /usr/share/icons/neru-light-classic/icon-theme.cache
rm -f /usr/share/icons/neru-dark-classic/icon-theme.cache
rm -f /usr/share/icons/neru-classic/icon-theme.cache
   done
fi


