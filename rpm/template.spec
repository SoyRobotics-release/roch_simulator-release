Name:           ros-indigo-roch-gazebo
Version:        1.0.12
Release:        0%{?dist}
Summary:        ROS roch_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-gazebo-plugins
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-gazebo-ros-control
Requires:       ros-indigo-hector-gazebo-plugins
Requires:       ros-indigo-map-server
Requires:       ros-indigo-pointcloud-to-laserscan
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roch-bringup
Requires:       ros-indigo-roch-control
Requires:       ros-indigo-roch-description
Requires:       ros-indigo-roch-navigation
Requires:       ros-indigo-rostopic
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
SawYer roch Simulator bringup

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 1.0.12-0
- Autogenerated by Bloom

* Thu Mar 23 2017 Carl <wzhang@softrobtech.com> - 1.0.11-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Carl <wzhang@softrobtech.com> - 1.0.10-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Carl <wzhang@softrobtech.com> - 1.0.9-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Carl <wzhang@softrobtech.com> - 1.0.8-1
- Autogenerated by Bloom

* Tue Jan 24 2017 Carl <wzhang@softrobtech.com> - 1.0.8-0
- Autogenerated by Bloom

