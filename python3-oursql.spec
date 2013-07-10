%define		module  oursql
Summary:	Set of MySQL bindings for python 3.x
Summary(pl.UTF-8):	Zestaw dowiązań do MySQLa dla Pythona
Name:		python3-%{module}
Version:	0.9.3
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	https://launchpad.net/oursql/py3k/py3k-0.9.3/+download/%{module}-%{version}.zip
# Source0-md5:	1c19d9ecbfc96e071f6da463a0fc9109
URL:		http://launchpad.net/oursql/py3k/
BuildRequires:	mysql-devel
BuildRequires:	python3-2to3
BuildRequires:	python3-Cython
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oursql is a set of MySQL bindings for python 2.4+ with a focus on
wrapping the `MYSQL_STMT API`__ to provide real parameterization and
real server-side cursors. MySQL 4.1.2 or better is required.

Python 3.x version.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python3} setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py \
	install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README
%attr(755,root,root) %{py3_sitedir}/*.so
%{py3_sitedir}/*.egg-info
