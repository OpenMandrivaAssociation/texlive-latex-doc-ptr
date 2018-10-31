Name:		texlive-latex-doc-ptr
Version:	20180303
Release:	2
Summary:	A direction-finder for LaTeX documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-doc-ptr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A two-page set of recommendations for users who need on-line
documentation of LaTeX. The document supports the need for
documentation of LaTeX itself, in distributions. For example,
it could be used in the command texdoc latex, in the TeX live
distribution.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
