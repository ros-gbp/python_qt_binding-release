%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-python-qt-binding
Version:        0.4.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS python_qt_binding package

License:        BSD
URL:            http://ros.org/wiki/python_qt_binding
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-qt5-devel
Requires:       ros-noetic-catkin
Requires:       sip
BuildRequires:  python3-qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-rosbuild
BuildRequires:  sip
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This stack provides Python bindings for Qt. There are two providers: pyside and
pyqt. PySide is released under the LGPL. PyQt is released under the GPL. Both
the bindings and tools to build bindings are included from each available
provider. For PySide, it is called &quot;Shiboken&quot;. For PyQt, this is
called &quot;SIP&quot;. Also provided is adapter code to make the user's Python
code independent of which binding provider was actually used which makes it very
easy to switch between these.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Jun 11 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.3-1
- Autogenerated by Bloom

* Thu May 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.2-1
- Autogenerated by Bloom

* Mon Mar 02 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.1-1
- Autogenerated by Bloom

* Fri Feb 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.0-1
- Autogenerated by Bloom

