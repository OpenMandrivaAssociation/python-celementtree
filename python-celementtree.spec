%define module		cElementTree
%define date_version	20051216

Summary:        Add-on to the standard ElementTree package
Name: 		python-celementtree
Version: 	1.0.5
Release: 	%mkrel 9
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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-7mdv2011.0
+ Revision: 667915
- mass rebuild

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1.0.5-6mdv2011.0
+ Revision: 589934
- rebuild for python 2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-5mdv2010.1
+ Revision: 523762
- rebuilt for 2010.1

* Sat Aug 22 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-4mdv2010.0
+ Revision: 419731
- P0: use system expat lib (gentoo)

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 1.0.5-3mdv2009.1
+ Revision: 319835
- rebuild for new python

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0.5-2mdv2009.0
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2008.0
+ Revision: 67516
- rebuild


* Fri Jan 05 2007 Michael Scherer <misc@mandriva.org> 1.0.5-1mdv2007.0
+ Revision: 104360
- update to 1.0.5
- use %%rel for mkrel

* Thu Dec 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.2-4mdv2007.1
+ Revision: 96892
- Rebuild against new python
- Rebuild for new python
- import python-celementtree-1.0.2-1mdk

