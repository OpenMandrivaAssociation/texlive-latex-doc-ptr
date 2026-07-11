%global tl_name latex-doc-ptr
%global tl_revision 77050

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A direction-finder for LaTeX resources available online
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-doc-ptr
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A brief set of recommendations for users who need online documentation
of LaTeX. The document supports the need for documentation of LaTeX
itself, in distributions. For example, it could be used in the command
texdoc latex, in the TeX Live distribution.

