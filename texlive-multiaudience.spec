%global tl_name multiaudience
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	Several versions of output from the same source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multiaudience
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiaudience.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to generate several versions of the same document
for different audiences.

