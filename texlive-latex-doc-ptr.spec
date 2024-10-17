Name:		texlive-latex-doc-ptr
Version:	72417
Release:	1
Summary:	A direction-finder for LaTeX documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-doc-ptr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-doc-ptr.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
