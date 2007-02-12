# TODO:
# - (someone please do it, as I dont know evolution) add evolution theme

%define		_name	Wasp
%define		_color_ver	0.4
Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):   Motyw ikon do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	2.6.1
Release:	4
License:	Design Science License (DSL)
Group:		Themes
Source0:	http://pyavitz.home.comcast.net/kde/%{_name}.SVG.Icons-v%{version}.tar.bz2
# Source0-md5:	ffe038b797cf9a7572b396ec5c618c4b
Source1:	dsl.txt
URL:		http://www.kde-look.org/content/show.php?content=9763
Requires:	kde-icons-%{_name}
Requires:	kde-decoration-icewm-%{_name}
Requires:	kde-colorscheme-%{_name}-thinkeramik
Requires:	kde-colorscheme-%{_name}-activeheart
Requires:	kde-colorscheme-%{_name}
Requires:	kde-splash-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Wasp Icons for KDE, originally released on GNOME as part of the GNOME
Themes Extras Project.

%description -l pl.UTF-8
Wasp Icons dla KDE, oryginalnie wydany dla GNOME jako część projektu
GNOME THemes Extras.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl.UTF-8):   Motyw ikon do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
Icon theme based on BeOS/Zeta icons. It creates a cartoon and
colorful, yet serious look.

%description -n kde-icons-%{_name} -l pl.UTF-8
Motyw ikon oparty o ikony z BeOS/Zeta, tworzy kreskówkowy i kolorowy,
ale wciąż poważny wygląd.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl.UTF-8):   Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Two Beos looking decorations for kwin.

%description -n kde-decoration-icewm-%{_name} -l pl.UTF-8
Dwie dekoracje podobne do Beos.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for %{_name} theme
Summary(pl.UTF-8):   Schemat kolorów dla motywu %{_name}
Group:		Themes
Version:	%{_color_ver}
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Three color schemes with gray window background and yellow/dark
blue/green selection backgrounds.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Trzy schematy kolorów z szarym tłem okna i żółtym, ciemnoniebieskim
lub zielonym kolorem zaznaczenia.

%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:	Extending color scheme for %{_name} theme for thinkeramik style
Summary(pl.UTF-8):   Rozszerzenia schematów kolorów dla motywu %{_name} do stylu thinkeramik
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-thinkeramik >= 3.2.1-2

%description -n kde-colorscheme-%{_name}-thinkeramik
Three extending colorschemes with light blue/blue/dark
blue/green/yellow colors for active tab marker, progress bar
background, slider and scrollbar.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl.UTF-8
Trzy rozszerzenia schematów kolorów z jasnoniebieskimi, niebieskimi,
ciemnoniebieskimi, żółtymi lub zielonymi kolorami wyróznika aktywnej
karty, suwaka, paska przewijania oraz tła paska postępu.

%package -n kde-colorscheme-%{_name}-activeheart
Summary:	Extending color scheme for %{_name} theme for activeheart style
Summary(pl.UTF-8):   Rozszerzenia schematów kolorów dla motywu %{_name} do stylu activeheart
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-ActiveHeart >= 1.2.1-2

%description -n kde-colorscheme-%{_name}-activeheart
Three extending colorschemes with blue/dark blue/green colors for
active tab marker, progress bar background, slider and scrollbar.

%description -n kde-colorscheme-%{_name}-activeheart -l pl.UTF-8
Trzy rozszerzenia schematów kolorów z niebieskimi, ciemnoniebieskimi
lub zielonymi kolorami wyróznika aktywnej karty, tła paska postępu,
suwaka oraz paska przewijania.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl.UTF-8):   Obrazki dla użytkowników w KDM - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdm

%description -n kdm-user-pictures-%{_name}
Two user pictures with a person on surfboard. One in yellow (normal
user) and in red (root).

%description -n kdm-user-pictures-%{_name} -l pl.UTF-8
Dwa obrazki użytkowników z osobą na desce surfingowej. Jedna ubrana na
żółto (zwykły użytkownik) i jedna na czerwono (root).


%package -n gdm-theme-%{_name}
Summary:	A Wasp theme for the GNOME Display Manager
Summary(pl.UTF-8):   Motyw Wasp do GDM
Group:		Themes
Requires:	gdm

%description -n gdm-theme-%{_name}
Three login screens for GDM with a cartoon computer icon in the center
and a login prompt under it. One with a yellow background, second
yellow with a gray area in the top left corner and third with a gray
background and yellow area in the top left corner.

%description -n gdm-theme-%{_name} -l pl.UTF-8
Trzy ekrany logowania do GDM z kreskówkową ikoną komputera w środku i
polem do logowania umieszczonym pod nią. Jeden z nich ma całe żółte
tło, drugi żółte tło i szary wycinek w lewym górnym rogu, a trzeci
szare tło i żółty wycinek.

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl.UTF-8):   Ekran startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Two splash screens (yellow and blue) with a "kde loading" bubble text
in the top left corner and a cartoon looking, Beos-like computer icon
to the right, and of course the standrad progress/icon bars.

%description -n kde-splash-%{_name} -l pl.UTF-8
Dwa ekrany startowe (niebieski i żółty) z dymkiem z tekstem "kde
loading" w lewym górnym rogu oraz kreskówkową ikoną komputera po
prawej, no i oczywiście standardowymi paskami postępu i ikon.

%package -n kde-kside-%{_name}
Summary:	Kicker side image from %{_name}
Summary(pl.UTF-8):   Boczny pasek do menu KDE z motywu %{_name}
Group:		Themes
Obsoletes:	kde-kside
Provides:	kde-kside
Requires:	kdebase-desktop >= 9:3.1.90.030726-2

%description -n kde-kside-%{_name}
A kicker side image with the "Wasp" text and a part of a cartoon
looging computer icon.

%description -n kde-kside-%{_name} -l pl.UTF-8
Pasek boczny do menu KDE z napisem "Wasp" oraz fragmentem kreskówkowej
ikony komputera.

%package -n kopete-emoticons-%{_name}
Summary:	Kopete emoticons from %{_name} theme
Summary(pl.UTF-8):   Emotikony do kopete z tematu %{_name}
Group:		Themes
Requires:	kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Round, convex, dark yellow emoticons with dark red faces.

%description -n kopete-emoticons-%{_name} -l pl.UTF-8
Okrągłe, wypukłe, ciemnożółte emotikony z ciemnoczerwonymi twarzami.

%prep
cd $RPM_BUILD_DIR
rm -rf Wasp
mkdir Wasp
cd Wasp
install %{SOURCE1} ./

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_datadir}/apps/{kopete/pics/emoticons,kdisplay/{color-schemes,styleconfs}}}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/{kwin/icewm-themes,kicker/pics,ksplash/Themes}
install -d $RPM_BUILD_ROOT%{_datadir}/{gdm/themes,apps/kdm/pics/users}
%{__tar} xfj %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}
##mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras ./
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/emoticons/Gossip $RPM_BUILD_ROOT%{_datadir}/apps/kopete/pics/emoticons/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/color-scheme/kde/*.*rc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/color-scheme/activeheart/*.*rc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/styleconfs/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/color-scheme/thinkeramik/*.*rc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/styleconfs/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/icewm/BeWB-0.3 $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/icewm/BeWasp $RPM_BUILD_ROOT%{_datadir}/apps/kwin/icewm-themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/kside/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kicker/pics/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/splash/Gonx $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/
mv $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/splash/Wasp $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/

# mv extras/evolution <WHERE>
mv -f $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/kdm/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/
mv -f $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/gdm/Wasp $RPM_BUILD_ROOT%{_datadir}/gdm/themes/
mv -f $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/gdm/Wasp.G $RPM_BUILD_ROOT%{_datadir}/gdm/themes/
mv -f $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras/gdm/Wasp.Y $RPM_BUILD_ROOT%{_datadir}/gdm/themes/
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/Wasp/extras

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n gdm-theme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/*

%files -n kde-icons-%{_name}
%defattr(644,root,root,755)
%doc Wasp/dsl.txt
%{_iconsdir}/Wasp

%files -n kdm-user-pictures-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/*

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
%{_datadir}/apps/kdisplay/styleconfs/thinkeramik_*.kcmrc

%files -n kde-colorscheme-%{_name}-activeheart
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/styleconfs/activeheart_*.kcmrc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-splash-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*
