%define module		cElementTree
%define date_version	20051216

Summary:        Add-on to the standard ElementTree package
Name: 		python-celementtree
Version: 	1.0.5
Release: 	%mkrel 4
Group: 		Development/Python
License:	Python license
URL:            http://effbot.org/zone/element-index.htm
Source0:        http://effbot.org/downloads/%{module}-%{version}-%{date_version}.tar.bz2
Patch0:		celementtree-1.0.5-external-libexpat.patch
Requires:	python-elementtree
%py_requires -d
BuildRequires:	expat-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is an add-on to the standard ElementTree package, which adds a very fast
and memory-efficient alternative implementation of the ElementTree API.

%prep
%setup -q -n %{module}-%{version}-%{date_version}
%patch0 -p1

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
