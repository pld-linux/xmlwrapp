Summary:	libxml2 C++ wrapper
Summary(pl):	Wi±zania C++ dla libxml2
Name:		xmlwrapp
Version:	0.5.0
Release:	1
License:	BSD-like
Group:		Libraries
Vendor:		Peter J Jones <pjones@pmade.org>
Source0:	http://pmade.org/software/xmlwrapp/download/%{name}-%{version}.tar.gz
# Source0-md5:	b8a07e77f8f8af9ca96bccab7d9dd310
# Source0-size:	110002
URL:		http://pmade.org/software/xmlwrapp/
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel >= 1.0.23
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmlwrapp is a modern style C++ library for working with XML data. It
provides a simple and easy to use interface for the very powerful
libxml2 XML parser and the libxslt XSLT engine.

%description -l pl
xmlwrapp jest nowoczesn± bibliotek± napisan± w C++, s³u¿±c± do pracy z
danymi w formacie XML. Dostarcza ona proste i ³atwe w u¿yciu
miêdzymordzie do libxml2 oraz libxslt.

%package devel
Summary:	Development files for xmlwrapp
Summary(pl):	Pliki nag³ówkowe dla xmlwrapp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for xmlwrapp.

%description devel -l pl
Pliki nag³ówkowe dla xmlwrapp.

%package static
Summary:	Static libraries for xmlwrapp
Summary(pl):	Biblioteki statyczne dla xmlwrapp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for xmlwrapp.

%description static -l pl
Biblioteki statyczne dla xmlwrapp.

%prep
%setup -q

%build
CXX="%{__cxx}" \
%{__perl} ./configure.pl \
	--prefix $RPM_BUILD_ROOT%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%{__perl} -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT{%{_bindir}/*,%{_pkgconfigdir}/*}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cd examples
for f in * ; do
	test -d $f || continue
	install $f/example.cxx $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f.cc
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
# TODO: process this docbook, generate doxygen stuff
%doc README docs/CREDITS docs/TODO docs/manual docs/project
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*
%{_pkgconfigdir}/%{name}.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
