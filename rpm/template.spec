Name:           ros-indigo-hector-localization
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS hector_localization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_localization
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-hector-pose-estimation
Requires:       ros-indigo-hector-pose-estimation-core
Requires:       ros-indigo-message-to-tf
BuildRequires:  ros-indigo-catkin

%description
The hector_localization stack is a collection of packages, that provide the full
6DOF pose of a robot or platform. It uses various sensor sources, which are
fused using an Extended Kalman filter. Acceleration and angular rates from an
inertial measurement unit (IMU) serve as primary measurements. The usage of
other sensors is application-dependent. The hector_localization stack currently
supports GPS, magnetometer, barometric pressure sensors and other external
sources that provide a geometry_msgs/PoseWithCovariance message via the
poseupdate topic.

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
* Sun Dec 21 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.1.5-0
- Autogenerated by Bloom

