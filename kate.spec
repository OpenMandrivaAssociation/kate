%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Advanced text editor
Name:		kate
Version:	21.12.0
Release:	1
Epoch:		3
License:	GPLv2+ LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://kate-editor.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	kwriteroot.desktop
Source10:	%{name}.rpmlintrc
Patch0:		https://gitweb.frugalware.org/frugalware-current/raw/master/source/kde5/kate/allow-root.patch
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)
Requires:	konsole >= 1:16.04.1
Requires:	katepart = %{EVRD}
Requires:	kate-extensions = %{EVRD}
Conflicts:	kdelibs4-core < 2:4.6.90
Obsoletes:	%{_lib}ktexteditor-codesnippets0 < 3:4.10.0
# For optional features
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	pkgconfig(libgit2) >= 0.26.0
# May come back once there's python-kde5
Obsoletes:	python-kate < %{EVRD}
# Likely gone for good
Obsoletes:	ktexteditor < %{EVRD}
Obsoletes:	kate-devel < %{EVRD}

%description
A fast and advanced text editor with nice plugins for KDE 5.

%files
%{_bindir}/kate
%{_datadir}/applications/org.kde.kate.desktop
%{_iconsdir}/hicolor/*/apps/kate.*[gz]
%{_datadir}/metainfo/org.kde.kate.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.katesessions.appdata.xml
%{_mandir}/man1/kate.1.*

#-----------------------------------------------------------------------------

%package -n katepart
Summary:	Kate KPart
Group:		Graphical desktop/KDE
Conflicts:	kdelibs4-core < 2:4.6.90
Conflicts:	kate < 3:4.10.5-2

%description -n katepart
This package contains the Kate KPart component.

%files -n katepart -f all.lang
%dir %{_libdir}/qt5/plugins/ktexteditor
%{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_katesessions.so
%dir %{_datadir}/kateproject
%{_datadir}/kateproject/kateproject.example
%dir %{_datadir}/katexmltools
%{_datadir}/katexmltools/html4-loose.dtd.xml
%{_datadir}/katexmltools/html4-strict.dtd.xml
%{_datadir}/katexmltools/kcfg.dtd.xml
%{_datadir}/katexmltools/kde-docbook.dtd.xml
%{_datadir}/katexmltools/kpartgui.dtd.xml
%{_datadir}/katexmltools/language.dtd.xml
%{_datadir}/katexmltools/simplify_dtd.xsl
%{_datadir}/katexmltools/testcases.xml
%{_datadir}/katexmltools/xhtml1-frameset.dtd.xml
%{_datadir}/katexmltools/xhtml1-strict.dtd.xml
%{_datadir}/katexmltools/xhtml1-transitional.dtd.xml
%{_datadir}/katexmltools/xslt-1.0.dtd.xml
%{_datadir}/kservices5/plasma-dataengine-katesessions.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.katesessions.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/KateSessionsItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/katesessions.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/metadata.json
%{_datadir}/plasma/services/org.kde.plasma.katesessions.operations

#-----------------------------------------------------------------------------
%package extensions
Summary:	Extensions for the Kate editor
Group:		Graphical desktop/KDE
Requires:	%{name}

%description extensions
Extensions for the Kate editor.

%files extensions -f plugins_lang
%{_libdir}/qt5/plugins/ktexteditor/katebacktracebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katebuildplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katecloseexceptplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katecolorpickerplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katectagsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefilebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefiletreeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kategdbplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kategitblameplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katekonsoleplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kateprojectplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katereplicodeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesearchplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesnippetsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesqlplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesymbolviewerplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katexmltoolsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/tabswitcherplugin.so
%{_libdir}/qt5/plugins/ktexteditor/textfilterplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katexmlcheckplugin.so
%{_libdir}/qt5/plugins/ktexteditor/ktexteditorpreviewplugin.so
%{_libdir}/qt5/plugins/ktexteditor/externaltoolsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/lspclientplugin.so
%{_libdir}/qt5/plugins/ktexteditor/compilerexplorer.so
%{_libdir}/qt5/plugins/ktexteditor/latexcompletionplugin.so

#-----------------------------------------------------------------------------

%package -n kwrite
Summary:	Simple text editor for KDE 5
Group:		Graphical desktop/KDE
Requires:	katepart = %{EVRD}
Suggests:	kate-extensions

%description -n kwrite
KWrite is a text editor for KDE, based on the Kate's editor component.
Features :
    Syntax highlighting according to the file type
    Word completion
    Auto-identation
    Plugin support
    Vi input mode

%files -n kwrite -f kwrite_lang
%{_bindir}/kwrite
%{_datadir}/applications/kwriteroot.desktop
%{_datadir}/applications/org.kde.kwrite.desktop
%{_datadir}/metainfo/org.kde.kwrite.appdata.xml
%{_iconsdir}/hicolor/*/apps/kwrite.*[gz]

#---------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/kwriteroot.desktop

%find_lang kate-ctags-plugin
%find_lang kate-replicode-plugin
%find_lang kate --with-man --with-html
%find_lang katepart --with-html
%find_lang katebacktracebrowserplugin
%find_lang katebuild-plugin
%find_lang katecloseexceptplugin
%find_lang katefilebrowserplugin
%find_lang katefiletree
%find_lang kategdbplugin
%find_lang katekonsoleplugin
%find_lang kateproject
%find_lang katesearch
%find_lang katesnippetsplugin
%find_lang katesql
%find_lang katesymbolviewer
%find_lang katetextfilter
%find_lang katexmlcheck
%find_lang katexmltools
%find_lang ktexteditorpreviewplugin
%find_lang kwrite --with-html
%find_lang lspclient
%find_lang plasma_applet_org.kde.plasma.katesessions
%find_lang tabswitcherplugin
%find_lang kateexternaltoolsplugin
%find_lang katecolorpickerplugin
%find_lang kategitblameplugin
mv kwrite.lang kwrite_lang
cat *plugin.lang >plugins_lang
rm *plugin.lang
cat *.lang >all.lang
