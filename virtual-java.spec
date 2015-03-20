Name: virtual-java
Version: %VERSION%
Release: %RELEASE%
Group: Development/Languages
Summary: Virtual package which provides java but uses the Sun/Oracle JDK
License: None
BuildArch: noarch
Provides: java-1.7.0-openjdk java java-1.7.0 java-1.7.0-openjdk(x86-64) java-fonts java-openjdk jre jre-1.7.0 jre-1.7.0-openjdk jre-openjdk lib.so(SUNWprivate_1.1)(64bit) libjavagtk.so()(64bit) libjavagtk.so(SUNWprivate_1.1)(64bit) libjsoundalsa.so()(64bit) libjsoundalsa.so(SUNWprivate_1.1)(64bit) libpulse-java.so()(64bit) libsplashscreen.so()(64bit) libsplashscreen.so(SUNWprivate_1.1)(64bit) java-devel java-1.7.0-openjdk-devel java7-1.7.0-devel java7-devel java7-devel-openjdk java7-sdk java7-sdk-1.7.0 java7-sdk-1.7.0-openjdk java7-sdk-openjdk lib.so()(64bit) lib.so(SUNWprivate_1.1)(64bit) libjli.so()(64bit) libjli.so(SUNWprivate_1.1)(64bit) libunpack.so()(64bit) libunpack.so(SUNWprivate_1.1)(64bit) java-1.7.0-openjdk-devel(x86-64)
Requires: jdk > %VERSION%

%description
Virtual package which provides java but uses the Sun/Oracle JDK

%prep

%build

%pre

%post
/usr/sbin/alternatives --install /usr/bin/java java /usr/java/default/bin/java 20000

%postun
/usr/sbin/alternatives --remove java /usr/java/default/bin/java

%install

%files

%changelog
