Summary:	Ammonite is a portion of the Eazel Services authentication framework
Summary(pl.UTF-8):	Część schematu autoryzacji używanego w usługach Eazel
Name:		ammonite
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ammonite/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	92653cf5e4e0b8d6e4e1fbc606aeea8a
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.11.0
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.8
BuildRequires:	gnome-libs >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel >= 0.6.0
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var/lib

%description
Ammonite is a non-caching client-side HTTP proxy with a set of special
features required by Eazel to communicate with Eazel Services.
Ammonite provides the user authentication and encryption features used
by Eazel Services. It is part of the GNOME project, and its source
code can be found in the GNOME CVS repository.

%description -l pl.UTF-8
Ammonite jest nie-keszującym serwerem proxy HTTP po stronie klienta ze
specjalnymi możliwościami koniecznymi by móc korzystać z Usług Eazel.
Ammonite dostarcza użytkownikowi możliwość autentyfikacji oraz
szyfrowania danych.

%package devel
Summary:	Header files and libraries
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki statyczne
Group:		Development/Libraries

%description devel
Header files and libraries

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki statyczne.

%prep
%setup -q

%build
%{__gettextize}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/vfs/modules/*
%{_datadir}/nautilus/certs/*
%{_pixmapsdir}/nautilus/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*/*
%{_datadir}/idl/*
%{_datadir}/oaf/*
%{_libdir}/*.a
%attr(755,root,root) %{_libdir}/*.sh
