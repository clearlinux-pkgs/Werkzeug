#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Werkzeug
Version  : 0.12.1
Release  : 35
URL      : http://pypi.debian.net/Werkzeug/Werkzeug-0.12.1.tar.gz
Source0  : http://pypi.debian.net/Werkzeug/Werkzeug-0.12.1.tar.gz
Summary  : The Swiss Army knife of Python web development
Group    : Development/Tools
License  : BSD-3-Clause OFL-1.1
Requires: Werkzeug-python
Requires: termcolor
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=================
Werkzeug Examples
=================
This directory contains various example applications and example code of
Werkzeug powered applications.

%package python
Summary: python components for the Werkzeug package.
Group: Default
Provides: werkzeug-python

%description python
python components for the Werkzeug package.


%prep
%setup -q -n Werkzeug-0.12.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489773460
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489773460
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
