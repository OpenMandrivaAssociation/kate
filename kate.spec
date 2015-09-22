%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Advanced text editor
Name:		kate
Version:	15.08.1
Release:	1
Epoch:		3
License:	GPLv2+ LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://kate-editor.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1:	kwriteroot.desktop
Source10:	%{name}.rpmlintrc
Patch0:		kate-4.12.90-python_library_realpath.patch
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
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)
Requires:	konsole >= 1:%{version}
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
BuildRequires:	pkgconfig(libgit2)
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
%{_datadir}/icons/hicolor/128x128/apps/kate.png
%{_datadir}/icons/hicolor/16x16/apps/kate.png
%{_datadir}/icons/hicolor/22x22/actions/debug-kategdb.png
%{_datadir}/icons/hicolor/22x22/apps/kate.png
%{_datadir}/icons/hicolor/32x32/apps/kate.png
%{_datadir}/icons/hicolor/48x48/apps/kate.png
%{_datadir}/icons/hicolor/64x64/apps/kate.png
%{_datadir}/icons/hicolor/scalable/apps/kate.svgz
%{_datadir}/appdata/org.kde.kate.appdata.xml
%{_mandir}/man1/kate.1.xz
%doc %{_docdir}/HTML/en/kate


#-----------------------------------------------------------------------------

%package -n katepart
Summary:	Kate KPart
Group:		Graphical desktop/KDE
Conflicts:	kdelibs4-core < 2:4.6.90
Conflicts:	kate < 3:4.10.5-2

%description -n katepart
This package contains the Kate KPart component.

%files -n katepart
%{_sysconfdir}/xdg/katerc
%{_sysconfdir}/xdg/ktexteditor_codesnippets_core.knsrc
%{_libdir}/libkdeinit5_kate.so
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
%{_datadir}/kservices5/katesymbolviewerplugin.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.katesessions.desktop
%{_datadir}/kservices5/plasma-dataengine-katesessions.desktop
%{_datadir}/kxmlgui5/kate/kateui.rc
%{_datadir}/kxmlgui5/katebuild/ui.rc
%{_datadir}/kxmlgui5/katecloseexceptplugin/ui.rc
%{_datadir}/kxmlgui5/katectags/ui.rc
%{_datadir}/kxmlgui5/katefiletree/ui.rc
%{_datadir}/kxmlgui5/kategdb/ui.rc
%{_datadir}/kxmlgui5/katekonsole/ui.rc
%{_datadir}/kxmlgui5/kateopenheaderplugin/ui.rc
%{_datadir}/kxmlgui5/kateproject/ui.rc
%{_datadir}/kxmlgui5/katesearch/ui.rc
%{_datadir}/kxmlgui5/katesnippets/ui.rc
%{_datadir}/kxmlgui5/katesql/ui.rc
%{_datadir}/kxmlgui5/katesymbolviewer/ui.rc
%{_datadir}/kxmlgui5/katexmltools/ui.rc
%{_datadir}/kxmlgui5/tabswitcher/ui.rc
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/KateSessionsItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/Menu.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/contents/ui/katesessions.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.katesessions/metadata.desktop
%{_datadir}/plasma/services/org.kde.plasma.katesessions.operations
%doc %{_docdir}/HTML/en/katepart

#-----------------------------------------------------------------------------
%package extensions
Summary:	Extensions for the Kate editor
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}

%description extensions
Extensions for the Kate editor

%files extensions
%{_libdir}/qt5/plugins/ktexteditor/katebacktracebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katebuildplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katecloseexceptplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katectagsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefilebrowserplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katefiletreeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kategdbplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katekonsoleplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kateopenheaderplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kateprojectplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katereplicodeplugin.so
%{_libdir}/qt5/plugins/ktexteditor/kterustcompletionplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesearchplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesnippetsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesqlplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katesymbolviewerplugin.so
%{_libdir}/qt5/plugins/ktexteditor/katexmltoolsplugin.so
%{_libdir}/qt5/plugins/ktexteditor/ktexteditor_lumen.so
%{_libdir}/qt5/plugins/ktexteditor/tabswitcherplugin.so
%{_datadir}/icons/hicolor/16x16/actions/sql-field-pk.png
%{_datadir}/icons/hicolor/16x16/actions/sql-field-red.png
%{_datadir}/icons/hicolor/16x16/actions/sql-field.png
%{_datadir}/icons/hicolor/16x16/actions/sql-table.png
%{_datadir}/icons/hicolor/16x16/actions/sql-view.png
%{_datadir}/kxmlgui5/katereplicodeplugin
%{_datadir}/kxmlgui5/kterustcompletion

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

%files -n kwrite
%{_bindir}/kwrite
%{_libdir}/libkdeinit5_kwrite.so
%{_datadir}/applications/kwriteroot.desktop
%{_datadir}/applications/org.kde.kwrite.desktop
%{_datadir}/kxmlgui5/kwrite/kwriteui.rc
%{_datadir}/appdata/org.kde.kwrite.appdata.xml
%doc %{_docdir}/HTML/en/kwrite

#---------------------------------------------------------------

%prep
%setup -q
#apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/kwriteroot.desktop
