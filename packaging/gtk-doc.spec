Name:           gtk-doc
Version:        1.19
Release:        0
Summary:        GTK+ DocBook Documentation Generator
License:        GPL-2.0+
Group:          Productivity/Publishing/SGML
Url:            http://www.gtk.org/gtk-doc/
Source:         http://download.gnome.org/sources/gtk-doc/1.19/%{name}-%{version}.tar.bz2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxml2-tools
BuildRequires:  libxslt
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  sgml-skel
BuildRequires:  xsltproc
Requires:       docbook-xsl-stylesheets
Requires:       docbook_4
Requires:       libxml2-tools
Requires:       libxslt
Requires:       libxslt-tools

%description
Gtkdoc is a set of Perl scripts that generate API reference
documentation in DocBook format.  It can extract documentation from
source code comments in a manner similar to Java-doc.  It is used to
generate the documentation for GLib, Gtk+, and GNOME.

%prep
%setup -q

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/gtk-doc/html
mv -v doc/README doc/doc.README

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING-DOCS ChangeLog NEWS README TODO doc/*
%{_bindir}/gtkdoc-*
%{_bindir}/gtkdocize
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/sgml/gtk-doc/
