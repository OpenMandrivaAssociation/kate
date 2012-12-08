Name:		kate
Summary:	Advanced text editor
Version:	4.9.4
Group:		Graphical desktop/KDE
Release:	1
Epoch:		3
License:	GPLv2 LGPLv2
URL:		http://kate-editor.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	subversion-devel
BuildRequires:	binutils-devel
BuildRequires:	boost-devel
BuildRequires:	libltdl-devel
Requires:	konsole >= 1:%{version}
Requires:	katepart = %{EVRD}
Requires:	kate-extensions = %{EVRD}
Conflicts:	kdelibs4-core < 2:4.6.90

%description
A fast and advanced text editor with nice plugins for KDE 4.

%files
%doc kate/COPYING.LIB kate/AUTHORS
%{_kde_bindir}/kate
%{_kde_bindir}/ktesnippets_editor
%{_kde_libdir}/libkdeinit4_kate.so
%{_kde_libdir}/kde4/katebacktracebrowserplugin.so
%{_kde_libdir}/kde4/katefilebrowserplugin.so
%{_kde_libdir}/kde4/katefiletemplates.so
%{_kde_libdir}/kde4/kategdbplugin.so
%{_kde_libdir}/kde4/katekonsoleplugin.so
%{_kde_libdir}/kde4/katemailfilesplugin.so
%{_kde_libdir}/kde4/kateopenheaderplugin.so
%{_kde_libdir}/kde4/katequickdocumentswitcherplugin.so
%{_kde_libdir}/kde4/katesearchplugin.so
%{_kde_libdir}/kde4/katesymbolviewerplugin.so
%{_kde_libdir}/kde4/katetabbarextensionplugin.so
%{_kde_libdir}/kde4/katetextfilterplugin.so
%{_kde_libdir}/kde4/plasma_applet_katesession.so
%{_kde_libdir}/kde4/katebuildplugin.so
%{_kde_libdir}/kde4/katectagsplugin.so
%{_kde_libdir}/kde4/kate_kttsd.so
%{_kde_libdir}/kde4/katexmlcheckplugin.so
%{_kde_libdir}/kde4/katesnippets_tngplugin.so
%{_kde_libdir}/kde4/katetabifyplugin.so
%{_kde_libdir}/kde4/katexmltoolsplugin.so
%{_kde_libdir}/kde4/katefiletreeplugin.so
%{_kde_libdir}/kde4/katesqlplugin.so
%{_kde_configdir}/ktexteditor_codesnippets_core.knsrc
%{_kde_applicationsdir}/kate.desktop
%{_kde_applicationsdir}/ktesnippets_editor.desktop
%{_kde_appsdir}/kate
%{_kde_appsdir}/katexmltools
%{_kde_appsdir}/kconf_update/kate-2.4.upd
%{_kde_appsdir}/ktexteditor_snippets
%{_kde_configdir}/katefiletemplates.knsrc
%{_kde_configdir}/katemoderc
%{_kde_configdir}/katerc
%{_kde_iconsdir}/hicolor/*/apps/*.*
%exclude %{_kde_iconsdir}/hicolor/scalable/apps/ktexteditorautobrace.svgz
%{_kde_iconsdir}/oxygen/*/actions/*
%{_kde_services}/katebacktracebrowserplugin.desktop
%{_kde_services}/katefilebrowserplugin.desktop
%{_kde_services}/katefiletemplates.desktop
%{_kde_services}/kategdbplugin.desktop
%{_kde_services}/katekonsoleplugin.desktop
%{_kde_services}/katemailfilesplugin.desktop
%{_kde_services}/kateopenheader.desktop
%{_kde_services}/katequickdocumentswitcher.desktop
%{_kde_services}/katesearch.desktop
%{_kde_services}/katesymbolviewer.desktop
%{_kde_services}/katetabbarextension.desktop
%{_kde_services}/katetextfilter.desktop
%{_kde_services}/plasma-applet-katesession.desktop
%{_kde_services}/katebuildplugin.desktop
%{_kde_services}/katectagsplugin.desktop
%{_kde_services}/kate_kttsd.desktop
%{_kde_services}/katexmlcheck.desktop
%{_kde_services}/katesnippets_tngplugin.desktop
%{_kde_services}/katetabifyplugin.desktop
%{_kde_services}/katexmltools.desktop
%{_kde_services}/katesql.desktop
%{_kde_services}/katefiletreeplugin.desktop
%{_kde_servicetypes}/kateplugin.desktop
%{_kde_mandir}/man1/kate.1.*
%{_kde_datadir}/mime/packages/ktesnippets.xml
%{_kde_docdir}/*/*/kate

#-----------------------------------------------------------------------------

%package -n katepart
Summary:	Kate KPart
Group:		Graphical desktop/KDE
Conflicts:	kdelibs4-core < 2:4.6.90

%description -n katepart
This package contains the Kate KPart component.

%files -n katepart
%{_kde_libdir}/kde4/katepart.so
%{_kde_appsdir}/katepart
%{_kde_configdir}/katepartpluginsrc
%{_kde_services}/katepart.desktop

#-----------------------------------------------------------------------------
%package -n kwrite
Summary:	Simple text editor for KDE 4
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
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
%{_kde_bindir}/kwrite
%{_kde_libdir}/libkdeinit4_kwrite.so
%{_kde_applicationsdir}/kwrite.desktop
%{_kde_appsdir}/kwrite
%{_kde_docdir}/*/*/kwrite

#------------------------------------------------------------------------------

%package -n ktexteditor
Summary:	Ktexteditor
Group:		Graphical desktop/KDE
Obsoletes:	kate-extensions < %{EVRD}
Provides:	kate-extensions = %{EVRD}

%description -n ktexteditor
Ktexteditor package

%files -n ktexteditor
%{_kde_libdir}/kde4/ktexteditor_autobrace.so
%{_kde_libdir}/kde4/ktexteditor_exporter.so
%{_kde_libdir}/kde4/ktexteditor_hlselection.so
%{_kde_libdir}/kde4/ktexteditor_iconinserter.so
%{_kde_libdir}/kde4/ktexteditor_insanehtml_le.so
%{_kde_libdir}/kde4/ktexteditor_insertfile.so
%{_kde_libdir}/kde4/ktexteditor_kdatatool.so
%{_kde_libdir}/kde4/ktexteditor_python-encoding.so
%{_kde_appsdir}/ktexteditor_exporter
%{_kde_appsdir}/ktexteditor_iconinserter
%{_kde_appsdir}/ktexteditor_insanehtml_le
%{_kde_appsdir}/ktexteditor_insertfile
%{_kde_appsdir}/ktexteditor_kdatatool
%{_kde_services}/ktexteditor_autobrace.desktop
%{_kde_services}/ktexteditor_autobrace_config.desktop
%{_kde_services}/ktexteditor_exporter.desktop
%{_kde_services}/ktexteditor_hlselection.desktop
%{_kde_services}/ktexteditor_iconinserter.desktop
%{_kde_services}/ktexteditor_insanehtml_le.desktop
%{_kde_services}/ktexteditor_insertfile.desktop
%{_kde_services}/ktexteditor_kdatatool.desktop
%{_kde_services}/ktexteditor_python-encoding.desktop
%{_kde_iconsdir}/hicolor/scalable/apps/ktexteditorautobrace.svgz

#------------------------------------------------------------------------------

%define kateinterfaces_major 4
%define libkateinterfaces %mklibname kateinterfaces %{kateinterfaces_major}

%package -n %{libkateinterfaces}
Summary:	Runtime library for Kate
Group:		System/Libraries

%description -n %{libkateinterfaces}
Runtime library for Kate.

%files -n %{libkateinterfaces}
%{_kde_libdir}/libkateinterfaces.so.%{kateinterfaces_major}*

#------------------------------------------------------------------------------

%define libkatepartinterfaces_major 4
%define libkatepartinterfaces %mklibname katepartinterfaces %{libkatepartinterfaces_major}

%package -n %{libkatepartinterfaces}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkatepartinterfaces}
Runtime library for Kate.

%files -n %{libkatepartinterfaces}
%{_kde_libdir}/libkatepartinterfaces.so.%{libkatepartinterfaces_major}*

#--------------------------------------------------------------------------------

%define ktexteditor_codesnipets_major 0
%define libktexteditor_codesnipets %mklibname ktexteditor-codesnippets %{ktexteditor_codesnipets_major}

%package -n %{libktexteditor_codesnipets}
Summary:	Ktexteditory Library
Group:		System/Libraries
Obsoletes:	%{_lib}ktexteditor_codesnippets_core0 < %{EVRD}

%description -n %{libktexteditor_codesnipets}
Ktexteditory codesnipets library.

%files -n %{libktexteditor_codesnipets}
%{_kde_libdir}/libktexteditor_codesnippets_core.so.%{ktexteditor_codesnipets_major}*

#---------------------------------------------------------------------

%package devel
Summary:	Header files for kate
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	pkgconfig(hunspell)
Requires:	pkgconfig(libxslt)
Requires:	subversion-devel
Requires:	binutils-devel
Requires:	boost-devel
Requires:	libltdl-devel
Requires:	antlr-tool
Requires:	antlr-C++
Requires:	%{libkateinterfaces} = %{EVRD}
Requires:	%{libktexteditor_codesnipets} = %{EVRD}
Requires:	%{libkatepartinterfaces} = %{EVRD}
Conflicts:	kdesdk4-devel < 1:4.6.90
Conflicts:	kdelibs4-devel < 2:4.6.90

%description  devel
This package includes the header files you will need to compile applications
against kate.

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/libkateinterfaces.so
%{_kde_libdir}/libkatepartinterfaces.so
%{_kde_libdir}/libktexteditor_codesnippets_core.so

#---------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0
- Add URL

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Tue Jul 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- New version 4.8.95
- Artistic Comment extension is removed in upstream, fix file list

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.1-69.1mib2010.2
- New version 4.8.1
- Add Obsoletes for libktexteditor_codesnippets_core0
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 3:4.8.0-69.2mib2010.2
+ Revision: 770515
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Wed Feb 01 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:4.8.0-2
+ Revision: 770515
- add required epoch to satisfy dependencies
- add rpmlintrc config to filter out some errors

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762451
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758043
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 748825
- Fix file list
- Fix file list
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739354
- New upstream tarball

* Sun Dec 04 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-2
+ Revision: 737681
- Remove kate-extensions which is exactly the same as ktexteditor ( thanks to Per Oyvind )

* Sat Dec 03 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2:4.7.80-1
+ Revision: 737547
- drop no longer provided files from %%files

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball 4.7.80

* Sat Sep 10 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 699184
- Fix file list
- imported package kate

