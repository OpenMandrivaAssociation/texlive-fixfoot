%global tl_name fixfoot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3a
Release:	%{tl_revision}.1
Summary:	Multiple use of the same footnote text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixfoot
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixfoot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a \DeclareFixedFootnote command to provide a single command for
a frequently-used footnote. The package ensures that only one instance
of the footnote text appears on each page (LaTeX needs to be run several
times to achieve this).

