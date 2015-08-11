Name: virtual-java
Version: %VERSION%
Release: %RELEASE%
Group: Development/Languages
Summary: Virtual package which provides java but uses the Sun/Oracle JDK
License: None
BuildArch: noarch
Provides: java-1_8_0-openjdk
Provides: java
Provides: java-1.8.0
Provides: java-1.8.0-64
Provides: java-1_8_0-openjdk(x86-64)
Provides: java-64
Provides: java-fonts
Provides: java-openjdk
Provides: java-openjdk-64
Provides: jre
Provides: jre-1.8.0
Provides: jre-1.8.0-64
Provides: jre-1.8.0-openjdk
Provides: jre-1.8.0-openjdk-64
Provides: jre-64
Provides: jre-openjdk
Provides: jre-openjdk-64
Provides: jre1.3.x
Provides: jre1.4.x
Provides: jre1.5.x
Provides: jre1.6.x
Provides: jre1.7.x
Provides: jre1.8.x
Provides: libawt_xawt.so()(64bit)
Provides: libawt_xawt.so(SUNWprivate_1.1)(64bit)
Provides: libicedtea-sound.so.1.0.1()(64bit)
Provides: libjawt.so()(64bit)
Provides: libjawt.so(SUNWprivate_1.1)(64bit)
Provides: libjsoundalsa.so()(64bit)
Provides: libjsoundalsa.so(SUNWprivate_1.1)(64bit)
Provides: libsplashscreen.so()(64bit)
Provides: libsplashscreen.so(SUNWprivate_1.1)(64bit)
Provides: java-1_8_0-openjdk-devel
Provides: java-1.8.0-devel
Provides: java-1_8_0-openjdk-devel(x86-64)
Provides: java-devel
Provides: java-devel-openjdk
Provides: java-sdk
Provides: java-sdk-1.8.0
Provides: java-sdk-1.8.0-openjdk
Provides: java-sdk-openjdk
Provides: lib.so(SUNWprivate_1.1)(64bit)
Provides: libjawt.so()(64bit)
Provides: libjawt.so(SUNWprivate_1.1)(64bit)
Provides: libjli.so()(64bit)
Provides: libjli.so(SUNWprivate_1.1)(64bit)
Provides: libunpack.so(SUNWprivate_1.1)(64bit)

Requires: java > %VERSION%

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
