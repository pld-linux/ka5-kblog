%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kblog
Summary:	Kblog
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	3
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ab9c274085303fea307f4e026cdfcfa2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kxmlrpcclient-devel >= %{kframever}
BuildRequires:	kf5-syndication-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlog provides client-side support for web application remote blogging
APIs.. KBlog is a library for calling functions on Blogger 1.0,
MetaWeblog, MovableType and GData compatible blogs. It calls the APIs
using KXmlRpcClient and Syndication. It supports asynchronous sending
and fetching of posts and, if supported on the server, multimedia
files.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kblog.categories
/etc/xdg/kblog.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5Blog.so.5
%attr(755,root,root) %{_libdir}/libKF5Blog.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KBlog
%{_includedir}/KF5/kblog_version.h
%{_libdir}/cmake/KF5Blog
%attr(755,root,root) %{_libdir}/libKF5Blog.so
%{_libdir}/qt5/mkspecs/modules/qt_KBlog.pri
