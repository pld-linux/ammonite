Summary:	Ammonite is a portion of the Eazel Services authentication framework.
Summary(pl):	Czê¶æ schematu autoryzacji u¿ywanego w us³ugach Eazel.
Name:		ammonite
Version:	1.0.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.gnome.org/
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	glib-devel >= 1.2.8
BuildRequires:	GConf-devel >= 0.11.0
BuildRequires:	libxml-devel
BuildRequires:	oaf-devel >= 0.6.0
BuildRequires:	gnome-libs >= 1.2.0
BuildRequires:	popt-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var/lib

%description
Ammonite is a non-caching client-side HTTP proxy with a set of special
features required by Eazel to communicate with Eazel Services.
Ammonite provides the user authentication and encryption features used
by Eazel Services. It is part of the GNOME project, and its source
code can be found in the GNOME CVS repository.

%description -l pl
Ammonite jest nie-keszuj±cym serwerem proxy HTTP po stronie klienta ze
specjalnymi mo¿liwo¶ciami koniecznymi by móc korzystaæ z Us³ug Eazel.
Ammonite dostarcza u¿ytkonikowi mo¿liwo¶æ autentyfikacji oraz
szyfrowania danych.

%package devel
Summary:	Header files and libraries
Summary(pl):	Pliki nag³ówkowe i biblioteki statyczne
Group:		Development/Libraries

%description devel
Header files and libraries

%description devel -l pl
Pliki nag³ówkowe i biblioteki statyczne.

%prep
%setup -q

%build
gettextize --copy --force
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
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
