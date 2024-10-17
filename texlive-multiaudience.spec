Name:		texlive-multiaudience
Version:	60688
Release:	2
Summary:	Several versions of output from the same source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multiaudience
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to generate several versions of the same
document for different audiences.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/multiaudience
%{_texmfdistdir}/tex/latex/multiaudience
%doc %{_texmfdistdir}/doc/latex/multiaudience

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
