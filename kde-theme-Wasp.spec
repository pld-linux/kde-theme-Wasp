#$Revision: 1.12 $, $Date: 2004-11-04 13:10:53 $
# TODO: (someone please do it, as I dont know evolution)
# + add evolution theme

%define		_name	Wasp
%define		_color_ver	0.4
Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	2.6.1
Release:	2
License:	Design Science License (DSL)
Group:		Themes
Source0:	http://pyavitz.home.comcast.net/kde/%{_name}.SVG.Icons-v%{version}.tar.bz2
# Source0-md5:	ffe038b797cf9a7572b396ec5c618c4b
Source1:	dsl.txt
URL:		http://www.kde-look.org/content/show.php?content=9763
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Wasp Icons for KDE, originally released on GNOME as part of the GNOME
Themes Extras Project.

%description -l pl
Wasp Icons dla KDE, oryginalnie wydany dla GNOME jako czê¶æ projektu
GNOME THemes Extras.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
Icon theme based on BeOS/Zeta icons. It creates a cartoon and
colorful, yet serious look.

%description -n kde-icons-%{_name} -l pl
Motyw ikon oparty o ikony z BeOS/Zeta, tworzy kreskówkowy i kolorowy,
ale wci±¿ powa¿ny wygl±d.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl):	Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Two Beos looking decorations for kwin.

%description -n kde-decoration-icewm-%{_name} -l pl
Dwie dekoracje podobne do Beos.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for %{_name} theme
Summary(pl):	Schemat kolorów dla motywu %{_name}
Group:		Themes
Version:	%{_color_ver}
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Three color schemes with gray window background and yellow/dark
blue/green selection backgrounds.

%description -n kde-colorscheme-%{_name} -l pl
Trzy schematy kolorów z szarym t³em okna i ¿ó³tym, ciemnoniebieskim
lub zielonym kolorem zaznaczenia.

%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:	Extending color scheme for %{_name} theme for thinkeramik style
Summary(pl):	Rozszerzenia schematów kolorów dla motywu %{_name} do stylu thinkeramik
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-thinkeramik >= 3.2.1-2

%description -n kde-colorscheme-%{_name}-thinkeramik
Three extending colorschemes with light blue/blue/dark
blue/green/yellow colors for active tab marker, progress bar
background, slider and scrollbar.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl
Trzy rozszerzenia schematów kolorów z jasnoniebieskimi, niebieskimi,
ciemnoniebieskimi, ¿ó³tymi lub zielonymi kolorami wyróznika aktywnej
karty, suwaka, paska przewijania oraz t³a paska postêpu.

%package -n kde-colorscheme-%{_name}-activeheart
Summary:	Extending color scheme for %{_name} theme for activeheart style
Summary(pl):	Rozszerzenia schematów kolorów dla motywu %{_name} do stylu activeheart
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-ActiveHeart >= 1.2.1-2

%description -n kde-colorscheme-%{_name}-activeheart
Three extending colorschemes with blue/dark blue/green colors for
active tab marker, progress bar background, slider and scrollbar.

%description -n kde-colorscheme-%{_name}-activeheart -l pl
Trzy rozszerzenia schematów kolorów z niebieskimi, ciemnoniebieskimi
lub zielonymi kolorami wyróznika aktywnej karty, t³a paska postêpu,
suwaka oraz paska przewijania.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl):	Obrazki dla u¿ytkowników w KDM - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdm

%description -n kdm-user-pictures-%{_name}
Two user pictures with a person on surfboard. One in yellow (normal
user) and in red (root).

%description -n kdm-user-pictures-%{_name} -lpl
Dwa obrazki u¿ytkowników z osob± na desce surfingowej. Jedna ubrana na
¿ó³to (zwyk³y u¿ytkownik) i jedna na czerwono (root).


%package -n gdm-theme-%{_name}
Summary:	A Wasp theme for the GNOME Display Manager
Summary(pl):	Motyw Wasp do GDM
Group:		Themes
Requires:	gdm

%description -n gdm-theme-%{_name}
Three login screens for GDM with a cartoon computer icon in the center
and a login prompt under it. One with a yellow background, second
yellow with a gray area in the top left corner and third with a gray
background and yellow area in the top left corner.

%description -n gdm-theme-%{_name} -l pl
Trzy ekrany logowania do GDM z kreskówkow± ikon± komputera w ¶rodku i
polem do logowania umieszczonym pod ni±. Jeden z nich ma ca³e ¿ó³te
t³o, drugi ¿ó³te t³o i szary wycinek w lewym górnym rogu, a trzeci
szare t³o i ¿ó³ty wycinek.

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl):	Ekran startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Two splash screens (yellow and blue) with a "kde loading" bubble text
in the top left corner and a cartoon looking, Beos-like computer icon
to the right, and of course the standrad progress/icon bars.

%description -n kde-splash-%{_name} -l pl
Dwa ekrany startowe (niebieski i ¿ó³ty) z dymkiem z tekstem "kde
loading" w lewym górnym rogu oraz kreskówkow± ikon± komputera po
prawej, no i oczywi¶cie standardowymi paskami postêpu i ikon.

%package -n kde-kside-%{_name}
Summary:	Kicker side image from %{_name}
Summary(pl):	Boczny pasek do menu KDE z motywu %{_name}
Group:		Themes
Obsoletes:	kde-kside
Provides:	kde-kside
Requires:	kdebase-kicker >= 9:3.1.90.030726-2

%description -n kde-kside-%{_name}
A kicker side image with the "Wasp" text and a part of a cartoon
looging computer icon.

%description -n kde-kside-%{_name} -l pl
Pasek boczny do menu KDE z napisem "Wasp" oraz fragmentem kreskówkowej
ikony komputera.

%package -n kopete-emoticons-%{_name}
Summary:	Kopete emoticons from %{_name} theme
Summary(pl):	Emotikony do kopete z tematu %{_name}
Group:		Themes
Requires:	kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Round, convex, dark yellow emoticons with dark red faces.

%description -n kopete-emoticons-%{_name} -l pl
Okr±g³e, wypuk³e, ciemno¿ó³te emotikony z ciemnoczerwonymi twarzami.

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
