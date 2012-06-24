%define	_rc alpha2
%define	_rel 0.1
Summary:	Video-conferencing for KDE
Summary(pl):	Wideokonferencje dla KDE
Name:		konference
Version:	0.1
Release:	0.%{_rc}.%{_rel}
License:	GPL
Group:		Applications/Multimedia
Source0:	http://download.berlios.de/konference/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	89e721b9172673b73e7eb44bf1a22522
Patch0:		%{name}-llh.patch
URL:		http://developer.berlios.de/projects/konference/
BuildRequires:	arts-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel
BuildRequires:	linux-libc-headers
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	sip-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konference is (or better: will be) a video-conferencing application
for KDE.

Since the rewrite (2005/01/25) it supports SIP as the signalling
protocol. No longer H323 folks.

%description -l pl
Konference jest aplikacj� wideokonferencji dla KDE.

Od czasu przepisania kodu (25.01.2005), obs�uguje SIP jako protok�
sygna�owy zamiast H323.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
    --enable-libsuffix=64 \
%endif
    --%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
    --with-qt-libraries=%{_libdir}

%{__make} \
	CXXLD=%{_host_cpu}-%{_vendor}-%{_os}-g++ \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/kde3/lib*
%{_datadir}/apps/*
%{_datadir}/config.kcfg/konference.kcfg
%{_datadir}/services/konference_part.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/*.desktop
