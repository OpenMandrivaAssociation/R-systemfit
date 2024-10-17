%global packname  systemfit
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.1.14
Release:          2
Summary:          Estimating Systems of Simultaneous Equations
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/systemfit_1.1-14.tar.gz
Requires:         R-Matrix R-car R-lmtest R-plm R-MASS R-sem
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-Matrix R-car R-lmtest R-plm R-MASS R-sem

%description
This package contains functions for fitting simultaneous systems of linear
and nonlinear equations using Ordinary Least Squares (OLS), Weighted Least
Squares (WLS), Seemingly Unrelated Regressions (SUR), Two-Stage Least
Squares (2SLS), Weighted Two-Stage Least Squares (W2SLS), and Three-Stage
Least Squares (3SLS).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
