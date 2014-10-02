Name:           ros-indigo-message-to-tf
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS message_to_tf package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/message_to_tf
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-topic-tools

%description
message_to_tf translates pose information from different kind of common_msgs
message types to tf. Currently the node supports nav_msgs/Odometry,
geometry_msgs/PoseStamped and sensor_msgs/Imu messages as input. The resulting
transform is divided into three subtransforms with intermediate frames for the
footprint and the stabilized base frame (without roll and pitch).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Oct 02 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.1.5-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.1.4-0
- Autogenerated by Bloom

