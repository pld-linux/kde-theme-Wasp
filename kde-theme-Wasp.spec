#$Revision: 1.3 $, $Date: 2004-04-16 19:27:22 $
# TODO: (someone please do it, as I dont know kdm/gdm/evolution)
# + add kdm icons
# + add gdm styles
# + add evolution theme

%define         _name Wasp

Summary:        KDE icons - %{_name}
Summary(pl):    Motyw ikon do KDE - %{_name}
Name:           kde-theme-%{_name}
Version:	2.6.1
Release:        0.1
License:        DPL
Group:          Themes
Source0:        http://pyavitz.home.comcast.net/kde/%{_name}.SVG.Icons-v%{version}.tar.bz2
# Source0-md5:	ffe038b797cf9a7572b396ec5c618c4b
Source1:	http://www.dsl.org/copyleft/dsl.txt
URL:		http://www.kde-look.org/content/show.php?content=9763
Requires:       kdelibs
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%description
%{_name} is

%description -l pl
%{_name} to temat ikon

%package -n kde-icons-%{_name}
Summary:        KDE icon theme - %{_name}
Summary(pl):    Motyw ikon do KDE - %{_name}
Group:          Themes
Requires:       kdelibs

%description -n kde-icons-%{_name}
Icon theme based on BeOS/Zeta icons.

%description -n kde-icons-%{_name} -l pl
Motyw ikon oparty o ikony z BeOS/Zeta.

%package -n kde-decoration-icewm-%{_name}
Summary:        Icewm window decoration for kwin - %{_name}
Summary(pl):    Dekoracja icewm dla kwin - %{_name}
Group:          Themes
Requires:       kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Icewm window decoration for kwin - %{_name}.

%description -n kde-decoration-icewm-%{_name} -l pl
Dekoracja icewm dla kwin - %{_name}.

%package -n kde-colorscheme-%{_name}
Summary:        Color scheme for %{_name} theme
Summary(pl):    Schemat kolorów dla motywu %{_name}
Group:          Themes
Requires:       kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for %{_name} theme.

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów dla motywu %{_name}.

%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:        Color scheme for %{_name} theme to go with thinkeramik style
Summary(pl):    Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik
Group:          Themes
Requires:       kdebase-core
Requires:	kde-style-thinkeramik

%description -n kde-colorscheme-%{_name}-thinkeramik
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl
Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik.


%package -n kde-splash-%{_name}
Summary:        Splash screen %{_name} theme
Summary(pl):    Obrazek startowy dla motywu %{_name}
Group:          Themes
Requires:       kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Splash screen %{_name} theme.

%description -n kde-splash-%{_name} -l pl
Obrazek startowy dla motywu %{_name}.

%package -n kde-kside-%{_name}
Summary:        Kicker sidebar from %{_name}
Summary(pl):    Boczny pasek do menu kde z motywu %{_name}
Group:          Themes
Obsoletes:      kde-kside
Provides:       kde-kside
Requires:       kdebase-kicker >= 9:3.1.90.030726-2

%description -n kde-kside-%{_name}
Kicker sidebar from %{_name}.

%description -n kde-kside-%{_name} -l pl
Boczny pasek do menu kde z motywu %{_name}.

%package -n kopete-emoticons-%{_name}
Summary:        Kopete emoticons from %{_name} theme
Summary(pl):    Emotikony do kopete z tematu %{_name}
Group:          Themes
Requires:       kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Kopete emoticons from %{_name} theme.

%description -n kopete-emoticons-%{_name} -l pl
Emotikony do kopete z tematu %{_name}.

%prep
cd $RPM_BUILD_DIR
mkdir Wasp
cd Wasp
install %{SOURCE1} ./

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_datadir}/apps/kopete/pics/emoticons,%{_datadir}/apps/kdisplay/color-schemes}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/{kwin/icewm-themes,kicker/pics,ksplash/Themes}
%{__tar} xfj  %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}
##mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras ./
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/emoticons/Gossip $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/color-scheme/*.*rc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/icewm/BeWB-0.3 $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/icewm/BeWasp $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/kside/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kicker/pics/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/splash/Gonx	$RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/splash/Wasp   $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/splash/WaspWare   $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/
# mv extras/evolution <WHERE>
# mv extras/kdm/*.png <WHERE>
# mv extras/gdm/Wasp <WHERE>
# mv extras/gdm/Wasp.G <WHERE>
# mv extras/gdm/Wasp.Y <WHERE>
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras


%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%doc dsl.txt
%{_iconsdir}/Wasp

%files -n kde-decoration-icewm-%{_name} 
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n kde-kside-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kicker/pics/*

%files -n kopete-emoticons-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kopete/pics/emoticons/*

%files -n kde-colorscheme-%{_name}-thinkeramik
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcmrc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-splash-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*
