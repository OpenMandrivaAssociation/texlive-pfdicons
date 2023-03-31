Name:		texlive-pfdicons
Version:	60089
Release:	2
Summary:	Draw process flow diagrams in chemical engineering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pfdicons
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pfdicons.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pfdicons.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides TikZ shapes to represent commonly
encountered unit operations for depiction in process flow
diagrams (PFDs) and, to a lesser extent, process and
instrumentation diagrams (PIDs). The package was designed with
undergraduate chemical engineering students and faculty in
mind, and the number of units provided should cover--in
Turton's estimate--about 90 percent of all fluid processing
operations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pfdicons
%doc %{_texmfdistdir}/doc/latex/pfdicons

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
