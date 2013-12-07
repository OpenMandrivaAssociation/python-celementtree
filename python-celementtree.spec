%define module		cElementTree
%define date_version	20051216

Summary:	Add-on to the standard ElementTree package
Name:		python-celementtree
Version:	1.0.5
Release:	11
Group:		Development/Python
License:	Python license
Url:		http://effbot.org/zone/element-index.htm
Source0:	http://effbot.org/downloads/%{module}-%{version}-%{date_version}.tar.bz2
Patch0:		celementtree-1.0.5-external-libexpat.patch
BuildRequires:	pkgconfig(expat)
Requires:	python-elementtree
%py_requires -d

%description
This is an add-on to the standard ElementTree package, which adds a very fast
and memory-efficient alternative implementation of the ElementTree API.

%prep
%setup -qn %{module}-%{version}-%{date_version}
%apply_patches

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot} --record INSTALLED_FILES

%files -f INSTALLED_FILES
%doc samples README* CHANGES*

