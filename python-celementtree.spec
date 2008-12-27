%define module		cElementTree
%define name		python-celementtree
%define version		1.0.5
%define date_version	20051216
%define rel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %rel
Summary:        Add-on to the standard ElementTree package
Group: 		Development/Python
License:	Python license
URL:            http://effbot.org/zone/element-index.htm
Source0:        http://effbot.org/downloads/%{module}-%{version}-%{date_version}.tar.bz2
Requires:	python-elementtree
%py_requires -d
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is an add-on to the standard ElementTree package, which adds a very fast
and memory-efficient alternative implementation of the ElementTree API.

%prep
%setup -q -n %{module}-%{version}-%{date_version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record INSTALLED_FILES


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc samples README* CHANGES*



