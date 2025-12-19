%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Advanced text editor
Name:		kate
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+ LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://kate-editor.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kate/-/archive/%{gitbranch}/kate-%{gitbranchd}.tar.bz2#/kate-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kate-%{version}.tar.xz
%endif
Source1:	kwriteroot.desktop
Patch0:		https://gitweb.frugalware.org/frugalware-current/raw/%{gitbranchd}/source/kde5/kate/allow-root.patch
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6WidgetsTools)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6MoreTools)
BuildRequires:	vulkan-devel
BuildRequires:	cmake(KUserFeedbackQt6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	pkgconfig(gpgmepp)
BuildRequires:	%mklibname -d KF6IconWidgets
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)
Requires:	konsole
Requires:	katepart = %{EVRD}
Requires:	%{name}-extensions = %{EVRD}
# For optional features
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	pkgconfig(libgit2) >= 0.26.0
# Just to prevent pulling in the KF5 version
BuildRequires:	plasma6-xdg-desktop-portal-kde

%rename plasma6-kate

%description
A fast and advanced text editor with nice plugins for KDE 6.

%files
%{_bindir}/exec_inspect.sh
%{_bindir}/kate
%{_libdir}/libkateprivate.so.*
%{_datadir}/applications/org.kde.kate.desktop
%{_iconsdir}/hicolor/*/apps/kate.*[gz]
%{_datadir}/metainfo/org.kde.kate.appdata.xml
%{_qtdir}/plugins/kf6/ktexteditor/katefilebrowserplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katesqlplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/templateplugin.so
%{_qtdir}/plugins/kf6/kio/kio_kateexec.so
%{_mandir}/man1/kate.1.*

#-----------------------------------------------------------------------------

%package -n katepart
Summary:	Kate KPart
Group:		Graphical desktop/KDE
%rename plasma6-katepart

%description -n katepart
This package contains the Kate KPart component.

%files -n katepart -f all.lang
%dir %{_qtdir}/plugins/kf6/ktexteditor
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

#-----------------------------------------------------------------------------
%package extensions
Summary:	Extensions for the Kate editor
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
%rename plasma6-kate-extensions

%description extensions
Extensions for the Kate editor.

%files extensions -f plugins_lang
%{_qtdir}/plugins/kf6/ktexteditor/bookmarksplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/cmaketoolsplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/compilerexplorer.so
%{_qtdir}/plugins/kf6/ktexteditor/eslintplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/externaltoolsplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/formatplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katebacktracebrowserplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katebuildplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katecloseexceptplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katecolorpickerplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katectagsplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katefiletreeplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/kategdbplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/kategpgplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/kategitblameplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katekonsoleplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/kateprojectplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katereplicodeplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katesearchplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katesnippetsplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katesymbolviewerplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katexmlcheckplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/katexmltoolsplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/keyboardmacrosplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/ktexteditorpreviewplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/latexcompletionplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/lspclientplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/openlinkplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/rainbowparens.so
%{_qtdir}/plugins/kf6/ktexteditor/tabswitcherplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/textfilterplugin.so
%{_qtdir}/plugins/kf6/ktexteditor/rbqlplugin.so

#-----------------------------------------------------------------------------

%package -n kwrite
Summary:	Simple text editor for KDE 5
Group:		Graphical desktop/KDE
Requires:	katepart = %{EVRD}
Suggests:	%{name}-extensions
%rename plasma6-kwrite

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
%autosetup -p1 -n kate-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

desktop-file-install    --remove-category="Development;" \
                        --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/org.kde.kate.desktop

install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/kwriteroot.desktop

%find_lang formatplugin
%find_lang kate-ctags-plugin
%find_lang kate-replicode-plugin
%find_lang kate --with-man --with-html
%find_lang katecompilerexplorer
%find_lang katepart --with-html
%find_lang katebacktracebrowserplugin
%find_lang katebuild-plugin
%find_lang katebookmarksplugin
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
%find_lang tabswitcherplugin
%find_lang kateexternaltoolsplugin
%find_lang katecolorpickerplugin
%find_lang kategpgplugin
%find_lang kategitblameplugin
%find_lang katekeyboardmacros
%find_lang rainbowparens
%find_lang rbqlplugin
mv kwrite.lang kwrite_lang
cat *plugin.lang >plugins_lang
rm *plugin.lang
cat *.lang >all.lang
