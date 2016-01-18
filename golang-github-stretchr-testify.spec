Name     : golang-github-stretchr-testify 
Version  : 1.0
Release  : 3
URL      : https://github.com/stretchr/testify/archive/v1.0.tar.gz
Source0  : https://github.com/stretchr/testify/archive/v1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-stretchr-objx

%description
Testify - Thou Shalt Write Tests
================================
[![Build Status](https://travis-ci.org/stretchr/testify.svg)](https://travis-ci.org/stretchr/testify)

%prep
%setup -q -n testify-1.0

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/stretchr/testify
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/stretchr/testify/assert/assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/errors.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/forward_assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/forward_assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/http_assertions.go
/usr/lib/golang/src/github.com/stretchr/testify/assert/http_assertions_test.go
/usr/lib/golang/src/github.com/stretchr/testify/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/http/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/http/test_response_writer.go
/usr/lib/golang/src/github.com/stretchr/testify/http/test_round_tripper.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/mock.go
/usr/lib/golang/src/github.com/stretchr/testify/mock/mock_test.go
/usr/lib/golang/src/github.com/stretchr/testify/package_test.go
/usr/lib/golang/src/github.com/stretchr/testify/require/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/require/forward_requirements.go
/usr/lib/golang/src/github.com/stretchr/testify/require/forward_requirements_test.go
/usr/lib/golang/src/github.com/stretchr/testify/require/requirements.go
/usr/lib/golang/src/github.com/stretchr/testify/require/requirements_test.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/doc.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/interfaces.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/suite.go
/usr/lib/golang/src/github.com/stretchr/testify/suite/suite_test.go
