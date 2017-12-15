Name:       desktop-file-utils
Summary:    Utilities for manipulating .desktop files
Version:    0.23
Release:    1
Group:      Development/Tools
License:    GPLv2+
URL:        http://www.freedesktop.org/software/desktop-file-utils
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0) >= 2.8.0

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.

%package doc
Summary: Documentation for %{name}
Group: Documentation

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
autoreconf -vfi

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/desktop-file-edit
%{_bindir}/desktop-file-install
%{_bindir}/desktop-file-validate
%{_bindir}/update-desktop-database


%files doc
%doc AUTHORS README COPYING NEWS
%{_mandir}/man1/*.1.gz
