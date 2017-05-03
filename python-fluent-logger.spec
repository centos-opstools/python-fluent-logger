# Created by pyp2rpm-3.2.1
%global pypi_name fluent-logger

%if 0%{?fedora}
%global with_python3 1
%else
%global with_python3 0
%endif

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        2%{?dist}
Summary:        A Python logging handler for Fluentd event collector

License:        ASL 2.0
URL:            https://github.com/fluent/fluent-logger-python
# Files from pypi don't include tests
# Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source0:        https://github.com/fluent/fluent-logger-python/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description
A Python structured logger for Fluentd Many web/mobile applications generate
huge amount of event logs (c,f. login, logout, purchase, follow, etc). To
analyze these event logs could be really valuable for improving the service.
However, the challenge is collecting these logs easily and reliably.

%package -n     python2-%{pypi_name}
Summary:        A Python logging handler for Fluentd event collector
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-msgpack
BuildRequires:  python-msgpack
%description -n python2-%{pypi_name}
A Python structured logger for Fluentd Many web/mobile applications generate
huge amount of event logs (c,f. login, logout, purchase, follow, etc). To
analyze these event logs could be really valuable for improving the service.
However, the challenge is collecting these logs easily and reliably.

%package -n python2-%{pypi_name}-tests
Summary:        tests for python-fluentd-logger

Requires:       python2-%{pypi_name} = %{version}-%{release}
%description -n python2-%{pypi_name}-tests
%{summary}

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        A Python logging handler for Fluentd event collector
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-msgpack
Requires:       python3-msgpack
%description -n python3-%{pypi_name}
A Python structured logger for Fluentd Many web/mobile applications generate
huge amount of event logs (c,f. login, logout, purchase, follow, etc). To
analyze these event logs could be really valuable for improving the service.
However, the challenge is collecting these logs easily and reliably.

%package -n python3-%{pypi_name}-tests
Summary:        tests for python-fluentd-logger

Requires:       python3-%{pypi_name} = %{version}-%{release}
%description -n python3-%{pypi_name}-tests
%{summary}

%endif

%prep
%autosetup -n %{pypi_name}-python-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if 0%{?with_python3}
%py3_install

# install -tests
mkdir -p %{buildroot}/%{python3_sitelib}/fluent/tests
install tests/*  %{buildroot}/%{python3_sitelib}/fluent/tests
%endif

%py2_install
# install -tests
mkdir -p %{buildroot}/%{python2_sitelib}/fluent/tests
install tests/*  %{buildroot}/%{python2_sitelib}/fluent/tests


%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license COPYING
%{python2_sitelib}/fluent
%exclude %{python2_sitelib}/fluent/tests
%{python2_sitelib}/fluent_logger-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}-tests
%{python2_sitelib}/fluent/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{python3_sitelib}/fluent
%exclude %{python3_sitelib}/fluent/tests
%{python3_sitelib}/fluent_logger-%{version}-py?.?.egg-info


%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/fluent/tests
%endif

%changelog
* Tue May 2 2017 Matthias Runge <mrunge@redhat.com> - 0.5.0-2
- use python2-setuptools
- specify COPYING file as license
- create a -test subpackage

* Wed Apr 26 2017 Matthias Runge <mrunge@redhat.com> - 0.5.0-1
- Initial package.
