Summary:	Video-conferencing for KDE
Name:		konference
%define	_rc alpha2
Version:	0.1
%define	_rel 0.1
Release:	0.%{_rc}.%{_rel}
License:	GPL
Group:		Applications/Multimedia
URL:		http://developer.berlios.de/projects/konference/
Source0:	http://download.berlios.de/konference/konference-0.1alpha2.tar.gz
# Source0-md5:	89e721b9172673b73e7eb44bf1a22522
BuildRequires:	arts-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
# some kind of llh
#BuildRequires:	linux-libc-headers
#BuildRequires:	sip-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konference is (or better: will be) a video-conferencing application
for KDE.

Since the rewrite (2005/01/25) it supports SIP as the signalling
protocol. No longer H323 folks.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
    --enable-libsuffix=64 \
%endif
    --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
    --with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/HTML/*/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/kde3/lib*
%{_datadir}/apps/*
%{_datadir}/config.kcfg/konference.kcfg
%{_datadir}/services/konference_part.desktop
%{_iconsdir}/hicolor/*/apps/*.png
