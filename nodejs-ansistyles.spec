%define		pkg	ansistyles
Summary:	Functions that surround a string with ansistyle codes so it prints in style
Name:		nodejs-%{pkg}
Version:	0.1.3
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/thlorenz/ansistyles
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	f0d628c13689293af7bfd7184c8f5de5
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functions that surround a string with ansistyle codes so it prints in
style.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
