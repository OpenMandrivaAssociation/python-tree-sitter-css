Name:		python-tree-sitter-css
Version:	0.25.0
Release:	1
Summary:	Tree-sitter css grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-css
Source0:	https://files.pythonhosted.org/packages/38/37/7d60171240d4c5ba330f05b725dfb5e5fd5b7cbe0aa98ef9e77f77f868f5/tree_sitter_css-0.25.0.tar.gz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for css, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_css-0.25.0

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_css*
