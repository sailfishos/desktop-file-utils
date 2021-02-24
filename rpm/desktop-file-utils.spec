Name:       desktop-file-utils
Summary:    Utilities for manipulating .desktop files
Version:    0.26
Release:    1
License:    GPLv2+
URL:        http://www.freedesktop.org/software/desktop-file-utils
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0) >= 2.8.0
BuildRequires:  meson

Patch0: 0001-Avoid-warnings-on-x-url-handler-mimetypes.patch

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.

%package doc
Summary: Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%meson
%meson_build

%install
rm -rf %{buildroot}
%meson_install

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/desktop-file-edit
%{_bindir}/desktop-file-install
%{_bindir}/desktop-file-validate
%{_bindir}/update-desktop-database
%exclude %{_datadir}/emacs/site-lisp/desktop-entry-mode.el

%files doc
%doc AUTHORS README COPYING NEWS
%{_mandir}/man1/*.1.gz
