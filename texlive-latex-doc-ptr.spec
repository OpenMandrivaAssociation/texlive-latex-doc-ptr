# revision 15878
# category Package
# catalog-ctan /info/latex-doc-ptr
# catalog-date 2009-06-03 15:14:30 +0200
# catalog-license pd
# catalog-version 2009-03-24
Name:		texlive-latex-doc-ptr
Version:	20090324
Release:	9
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
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr/Makefile
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr/README
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr/latex-doc-ptr.pdf
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr/latex-doc-ptr.sty
%doc %{_texmfdistdir}/doc/latex/latex-doc-ptr/latex-doc-ptr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090324-2
+ Revision: 753179
- Rebuild to reduce used resources

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090324-1
+ Revision: 722016
- latex-doc-ptr
- texlive-latex-doc-ptr
- texlive-latex-doc-ptr
- texlive-latex-doc-ptr
- texlive-latex-doc-ptr

