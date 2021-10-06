#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Werkzeug
Version  : 2.0.2
Release  : 84
URL      : https://files.pythonhosted.org/packages/83/3c/ecdb36f49ab06defb0d5a466cfeb4ae90a55d02cfef379f781da2801a45d/Werkzeug-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/3c/ecdb36f49ab06defb0d5a466cfeb4ae90a55d02cfef379f781da2801a45d/Werkzeug-2.0.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/83/3c/ecdb36f49ab06defb0d5a466cfeb4ae90a55d02cfef379f781da2801a45d/Werkzeug-2.0.2.tar.gz.asc
Summary  : The comprehensive WSGI web application library.
Group    : Development/Tools
License  : BSD-3-Clause OFL-1.1
Requires: Werkzeug-license = %{version}-%{release}
Requires: Werkzeug-python = %{version}-%{release}
Requires: Werkzeug-python3 = %{version}-%{release}
Requires: dataclasses
Requires: watchdog
BuildRequires : buildreq-distutils3
BuildRequires : dataclasses
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : watchdog

%description
This directory contains modules that have code but that are
not excutable.  For example routing definitions to play around
in the python interactive prompt.

%package license
Summary: license components for the Werkzeug package.
Group: Default

%description license
license components for the Werkzeug package.


%package python
Summary: python components for the Werkzeug package.
Group: Default
Requires: Werkzeug-python3 = %{version}-%{release}
Provides: werkzeug-python

%description python
python components for the Werkzeug package.


%package python3
Summary: python3 components for the Werkzeug package.
Group: Default
Requires: python3-core
Provides: pypi(werkzeug)

%description python3
python3 components for the Werkzeug package.


%prep
%setup -q -n Werkzeug-2.0.2
cd %{_builddir}/Werkzeug-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633537092
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Werkzeug
cp %{_builddir}/Werkzeug-2.0.2/LICENSE.rst %{buildroot}/usr/share/package-licenses/Werkzeug/c4dbdbc12926d4d52c9156e690640f372615c234
cp %{_builddir}/Werkzeug-2.0.2/src/werkzeug/debug/shared/FONT_LICENSE %{buildroot}/usr/share/package-licenses/Werkzeug/81e5605d07c08e95048556f1795931cc038d01e6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Werkzeug/81e5605d07c08e95048556f1795931cc038d01e6
/usr/share/package-licenses/Werkzeug/c4dbdbc12926d4d52c9156e690640f372615c234

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
