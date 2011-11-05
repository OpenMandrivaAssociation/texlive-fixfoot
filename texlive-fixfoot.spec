# revision 17131
# category Package
# catalog-ctan /macros/latex/contrib/fixfoot
# catalog-date 2010-02-20 00:32:21 +0100
# catalog-license lppl
# catalog-version 0.3a
Name:		texlive-fixfoot
Version:	0.3a
Release:	1
Summary:	Multiple use of the same footnote text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixfoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a \DeclareFixedFootnote command to provide a single
command for a frequently-used footnote. The package ensures
that only one instance of the footnote text appears on each
page (LaTeX needs to be run several times to achieve this).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixfoot/fixfoot.sty
%doc %{_texmfdistdir}/doc/latex/fixfoot/README
%doc %{_texmfdistdir}/doc/latex/fixfoot/fixfoot.pdf
%doc %{_texmfdistdir}/doc/latex/fixfoot/fixfoot.tex
%doc %{_texmfdistdir}/doc/latex/fixfoot/testfix.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
