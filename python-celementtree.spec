%define module		elementtree
%define date_version	20050316
%define debug_package	%nil

Summary:	Add-on to the standard ElementTree package
Name:		python2-celementtree
Version:	1.2.6
Release:	5
Group:		Development/Python
License:	Python license
Url:		http://effbot.org/zone/element-index.htm
Source0:	http://effbot.org/downloads/%{module}-%{version}-%{date_version}.tar.gz
BuildRequires:	pkgconfig(expat)
BuildRequires:  python2-devel
Requires:	python-elementtree

%description
This is an add-on to the standard ElementTree package, which adds a very fast
and memory-efficient alternative implementation of the ElementTree API.

%prep
%setup -qn %{module}-%{version}-%{date_version}
%apply_patches

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --root=%{buildroot}

%files
%doc samples README* CHANGES*
%{python2_sitelib}/*.egg*
%{python2_sitelib}/%{module}/*
