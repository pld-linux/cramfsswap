Summary:	swap endianess of a cram filesystem (cramfs)
Name:		cramfsswap
Version:	1.4.2
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://ftp.debian.org/debian/pool/main/c/cramfsswap/%{name}_%{version}.tar.xz
# Source0-md5:	f7813518fe788ae2e4fa6fd1a019c9e1
URL:		http://kju.de/projekte/cramfsswap/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cramfs is a highly compressed and size optimized Linux filesystem
which is mainly used for embedded applications. The problem with
cramfs is that it is endianness sensitive, meaning you can't mount a
cramfs for a big endian target on a little endian machine and vice
versa. This is often especially a problem in the development phase.

cramfsswap solves that problem by allowing you to swap to endianness
of a cramfs filesystem.

%prep
%setup -q

%build
%{__make} cramfsswap \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags}" \
	CFLAGS="%{rpmcflags}"
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
