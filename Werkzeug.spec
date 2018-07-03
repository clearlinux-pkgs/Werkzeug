#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Werkzeug
Version  : 0.14.1
Release  : 57
URL      : http://pypi.debian.net/Werkzeug/Werkzeug-0.14.1.tar.gz
Source0  : http://pypi.debian.net/Werkzeug/Werkzeug-0.14.1.tar.gz
Summary  : The comprehensive WSGI web application library.
Group    : Development/Tools
License  : BSD-3-Clause OFL-1.1
Requires: Werkzeug-python3
Requires: Werkzeug-license
Requires: Werkzeug-python
Requires: Sphinx
Requires: termcolor
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
========
        
        Werkzeug is a comprehensive `WSGI`_ web application library. It began as
        a simple collection of various utilities for WSGI applications and has
        become one of the most advanced WSGI utility libraries.

%package legacypython
Summary: legacypython components for the Werkzeug package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Werkzeug package.


%package license
Summary: license components for the Werkzeug package.
Group: Default

%description license
license components for the Werkzeug package.


%package python
Summary: python components for the Werkzeug package.
Group: Default
Requires: Werkzeug-python3
Provides: werkzeug-python

%description python
python components for the Werkzeug package.


%package python3
Summary: python3 components for the Werkzeug package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Werkzeug package.


%prep
%setup -q -n Werkzeug-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530378322
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530378322
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/Werkzeug
cp LICENSE %{buildroot}/usr/share/doc/Werkzeug/LICENSE
cp werkzeug/debug/shared/FONT_LICENSE %{buildroot}/usr/share/doc/Werkzeug/werkzeug_debug_shared_FONT_LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/Werkzeug/LICENSE
/usr/share/doc/Werkzeug/werkzeug_debug_shared_FONT_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
