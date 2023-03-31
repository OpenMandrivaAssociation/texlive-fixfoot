Name:		texlive-fixfoot
Version:	17131
Release:	2
Summary:	Multiple use of the same footnote text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixfoot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a \DeclareFixedFootnote command to provide a single
command for a frequently-used footnote. The package ensures
that only one instance of the footnote text appears on each
page (LaTeX needs to be run several times to achieve this).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixfoot/fixfoot.sty
%doc %{_texmfdistdir}/doc/latex/fixfoot/README
%doc %{_texmfdistdir}/doc/latex/fixfoot/fixfoot.pdf
%doc %{_texmfdistdir}/doc/latex/fixfoot/fixfoot.tex
%doc %{_texmfdistdir}/doc/latex/fixfoot/testfix.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
